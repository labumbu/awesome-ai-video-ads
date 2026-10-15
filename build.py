"""Build README.md and stats.json for the awesome-ai-video-ads list.

Reads repos.json, pulls live stars and licenses from the GitHub API (via `gh`)
and likes/downloads from the Hugging Face API, then writes both files next to
this script. Run: python3 build.py
"""
import datetime
import json
import pathlib
import subprocess
import urllib.request

HERE = pathlib.Path(__file__).parent
QUELTA_URL = "https://quelta.ai/?utm_source=github&utm_medium=awesome&utm_campaign=awesome-ai-video-ads"


def gh_repo(full_name):
    out = subprocess.run(
        ["gh", "api", f"repos/{full_name}", "--jq",
         "{stars: .stargazers_count, license: (.license.spdx_id // \"-\"), pushed: .pushed_at, url: .html_url}"],
        capture_output=True, text=True, check=True,
    )
    return json.loads(out.stdout)


def hf_model(model_id):
    req = urllib.request.Request(f"https://huggingface.co/api/models/{model_id}", headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.load(resp)
    return {"likes": data.get("likes", 0), "downloads": data.get("downloads", 0)}


def short(n):
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1000:
        return f"{n / 1000:.1f}K".replace(".0K", "K")
    return str(n)


def main():
    src = json.loads((HERE / "repos.json").read_text())
    today = datetime.date.today()
    stats = {"date": today.isoformat(), "categories": [], "hf": []}
    make_total = check_total = make_count = check_count = 0

    for cat in src["categories"]:
        rows = []
        for full_name, note in cat["repos"]:
            info = gh_repo(full_name)
            info["license"] = {"NOASSERTION": "Not detected, see repo", "-": "Not detected, see repo"}.get(info["license"], info["license"])
            rows.append({"repo": full_name, "note": note, **info})
        rows.sort(key=lambda r: r["stars"], reverse=True)
        total = sum(r["stars"] for r in rows)
        if cat.get("check"):
            check_total += total
            check_count += len(rows)
        else:
            make_total += total
            make_count += len(rows)
        stats["categories"].append({**{k: v for k, v in cat.items() if k != "repos"}, "total": total, "repos": rows})

    for model_id in src["huggingface"]:
        try:
            stats["hf"].append({"model": model_id, **hf_model(model_id)})
        except Exception as err:  # a renamed or gated model shouldn't break the build
            print(f"skip HF {model_id}: {err}")

    stats.update(make_total=make_total, make_count=make_count, check_total=check_total, check_count=check_count)
    (HERE / "stats.json").write_text(json.dumps(stats, indent=1))

    date_str = today.strftime("%-d %b %Y")
    lines = [
        "# Awesome AI Video Ads",
        "",
        f"**{make_count} open-source repos to make a video ad with AI. {check_count} that check whether it will sell.**",
        "",
        f"The repos below that make video have **{make_total:,} GitHub stars** between them. "
        f"The ones that check a video ad before you spend money on it have **{check_total:,}**.",
        "",
        "Making a video ad is close to free now. Knowing which one will sell is not. "
        "This list maps the open-source stack for both, grouped by the job each tool does in an ad pipeline.",
        "",
        f"Stars and licenses: GitHub API, {date_str}, refreshed with `build.py`. Code licenses only: model weights often have "
        "their own license, so check it before you run an ad made with them.",
        "",
        "## Contents",
        "",
    ]
    for cat in stats["categories"]:
        anchor = cat["title"].lower().replace(" ", "-").replace(":", "").replace(",", "")
        lines.append(f"- [{cat['title']}](#{anchor}) — {len(cat['repos'])} repos, {short(cat['total'])} stars")
    lines.append("- [On Hugging Face](#on-hugging-face)")
    lines.append("")

    for cat in stats["categories"]:
        lines += [f"## {cat['title']}", "", "| Repo | Stars | What it does for an ad | Code license |", "|---|---:|---|---|"]
        for r in cat["repos"]:
            lines.append(f"| [{r['repo']}]({r['url']}) | {short(r['stars'])} | {r['note']} | {r['license']} |")
        lines.append("")
        if cat.get("check"):
            lines += [
                "Know another open-source tool that checks a video ad before launch? Open a pull request.",
                "",
                f"Want a check right now: [Quelta]({QUELTA_URL}) reviews a vertical video ad for a platform, country "
                "and audience age, scores it 0–100 and timecodes every mistake. Free, 5 reviews a day, no sign-up.",
                "",
            ]

    lines += ["## On Hugging Face", "", "| Model | Likes | Downloads, last 30 days |", "|---|---:|---:|"]
    for m in sorted(stats["hf"], key=lambda m: m["downloads"], reverse=True):
        lines.append(f"| [{m['model']}](https://huggingface.co/{m['model']}) | {short(m['likes'])} | {short(m['downloads'])} |")
    lines += [
        "",
        "## Contributing",
        "",
        "Pull requests welcome. Add the repo to the right section with one line on what it does for an ad. "
        "Repos that only do face swaps of real people are left out on purpose.",
        "",
        f"Maintained by [Quelta]({QUELTA_URL}).",
        "",
    ]
    (HERE / "README.md").write_text("\n".join(lines))
    print(f"make: {make_count} repos, {make_total:,} stars | check: {check_count} repos, {check_total:,} stars")
    for cat in stats["categories"]:
        print(f"  {cat['short']}: {len(cat['repos'])} repos, {cat['total']:,}")
    for m in stats["hf"]:
        print(f"  HF {m['model']}: {m['likes']} likes, {m['downloads']:,} dl")


if __name__ == "__main__":
    main()
