# Awesome AI Video Ads

**63 open-source repos to make a video ad with AI. 3 that check whether it will sell.**

The repos below that make video have **1,527,694 GitHub stars** between them. The ones that check a video ad before you spend money on it have **118**.

Making a video ad is close to free now. Knowing which one will sell is not. This list maps the open-source stack for both, grouped by the job each tool does in an ad pipeline.

Stars and licenses: GitHub API, 15 Oct 2026, refreshed with `build.py`. Code licenses only: model weights often have their own license, so check it before you run an ad made with them.

## Contents

- [Agents that edit and assemble the video](#agents-that-edit-and-assemble-the-video) — 8 repos, 246.5K stars
- [Short-video and UGC factories](#short-video-and-ugc-factories) — 8 repos, 172.1K stars
- [Open video models](#open-video-models) — 12 repos, 273.3K stars
- [Voice: text-to-speech and cloning](#voice-text-to-speech-and-cloning) — 12 repos, 387.5K stars
- [Faces, avatars and lip-sync](#faces-avatars-and-lip-sync) — 8 repos, 87.8K stars
- [Translate and dub](#translate-and-dub) — 8 repos, 69.2K stars
- [Transcribe, cut and caption](#transcribe-cut-and-caption) — 7 repos, 291.3K stars
- [Check whether the ad will sell](#check-whether-the-ad-will-sell) — 3 repos, 118 stars
- [On Hugging Face](#on-hugging-face)

## Agents that edit and assemble the video

| Repo | Stars | What it does for an ad | Code license |
|---|---:|---|---|
| [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | 68.4K | Agentic video production: script to finished cut with a coding agent | AGPL-3.0 |
| [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | 64.2K | Make videos in React code; the base layer of many AI video agents. Own license: larger companies need a paid one | Not detected, see repo |
| [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | 64K | HeyGen's HTML-to-video renderer built for agents | Apache-2.0 |
| [browser-use/video-use](https://github.com/browser-use/video-use) | 29K | Edit real footage with a coding agent | MIT |
| [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | 12K | Claude Code / Codex skill for product videos on Remotion | Apache-2.0 |
| [remotion-dev/skills](https://github.com/remotion-dev/skills) | 5.2K | Official Remotion skills for Claude Code and other agents | Not detected, see repo |
| [0xsline/OpenChatCut](https://github.com/0xsline/OpenChatCut) | 2.4K | Chat-driven video editor with a multi-track timeline | AGPL-3.0 |
| [nateherkai/herk-edit-kit](https://github.com/nateherkai/herk-edit-kit) | 1.5K | Edit Reels and Shorts with Claude Code or Codex | Not detected, see repo |

## Short-video and UGC factories

| Repo | Stars | What it does for an ad | Code license |
|---|---:|---|---|
| [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) | 131K | Topic or keyword in, finished short video out | MIT |
| [FujiwaraChoki/MoneyPrinter](https://github.com/FujiwaraChoki/MoneyPrinter) | 14.1K | The original automated YouTube Shorts maker | MIT |
| [RayVentura/ShortGPT](https://github.com/RayVentura/ShortGPT) | 8K | Framework for automated Shorts and TikTok channels | MIT |
| [mutonby/openshorts](https://github.com/mutonby/openshorts) | 6.6K | Long video in, 9:16 clips with face tracking out | MIT |
| [YILS-LIN/short-video-factory](https://github.com/YILS-LIN/short-video-factory) | 5.6K | Batch product-marketing shorts, desktop app | AGPL-3.0 |
| [Anil-matcha/AI-Youtube-Shorts-Generator](https://github.com/Anil-matcha/AI-Youtube-Shorts-Generator) | 5.4K | Long YouTube video to vertical clips | MIT |
| [xixihhhh/clipforge](https://github.com/xixihhhh/clipforge) | 1K | One product photo to a selling short video | AGPL-3.0 |
| [Anil-matcha/Open-AI-UGC](https://github.com/Anil-matcha/Open-AI-UGC) | 367 | AI UGC-style videos with avatars | MIT |

## Open video models

| Repo | Stars | What it does for an ad | Code license |
|---|---:|---|---|
| [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | 137.6K | The node editor most people run open video models in | GPL-3.0 |
| [hpcaitech/Open-Sora](https://github.com/hpcaitech/Open-Sora) | 29.9K | Open text- and image-to-video model | Apache-2.0 |
| [Wan-Video/Wan2.2](https://github.com/Wan-Video/Wan2.2) | 17.9K | Alibaba's open video model family | Apache-2.0 |
| [lllyasviel/FramePack](https://github.com/lllyasviel/FramePack) | 17.3K | Long image-to-video on consumer GPUs | Apache-2.0 |
| [zai-org/CogVideo](https://github.com/zai-org/CogVideo) | 13.1K | CogVideoX text- and image-to-video | Apache-2.0 |
| [Tencent-Hunyuan/HunyuanVideo](https://github.com/Tencent-Hunyuan/HunyuanVideo) | 12.6K | Tencent's open video model | Not detected, see repo |
| [MiniMax-AI/MiniMax-H3](https://github.com/MiniMax-AI/MiniMax-H3) | 10K | MiniMax's open video model (the Hailuo team) | Not detected, see repo |
| [Lightricks/LTX-2](https://github.com/Lightricks/LTX-2) | 9.8K | Audio + video in one model, with a LoRA trainer | Not detected, see repo |
| [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video) | 9.2K | Meituan's long-video model | MIT |
| [SkyworkAI/SkyReels-V2](https://github.com/SkyworkAI/SkyReels-V2) | 7.7K | Long-form film generation | Not detected, see repo |
| [Tencent-Hunyuan/HunyuanVideo-1.5](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5) | 4.6K | Lighter HunyuanVideo for smaller GPUs | Not detected, see repo |
| [genmoai/mochi](https://github.com/genmoai/mochi) | 3.8K | Genmo's open video model | Apache-2.0 |

## Voice: text-to-speech and cloning

| Repo | Stars | What it does for an ad | Code license |
|---|---:|---|---|
| [RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) | 62.8K | Clone a voice from about a minute of audio | MIT |
| [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice) | 54.8K | Microsoft's open voice model, long multi-speaker audio | MIT |
| [2noise/ChatTTS](https://github.com/2noise/ChatTTS) | 39.9K | Conversational text-to-speech | AGPL-3.0 |
| [OpenBMB/VoxCPM](https://github.com/OpenBMB/VoxCPM) | 39.3K | Multilingual TTS with voice design | Apache-2.0 |
| [myshell-ai/OpenVoice](https://github.com/myshell-ai/OpenVoice) | 37.9K | Instant voice cloning across languages | MIT |
| [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) | 33.1K | Multilingual TTS and cloning | Not detected, see repo |
| [resemble-ai/chatterbox](https://github.com/resemble-ai/chatterbox) | 27K | TTS with emotion control | MIT |
| [index-tts/index-tts](https://github.com/index-tts/index-tts) | 24.5K | Zero-shot TTS with duration control (handy for dubbing) | Not detected, see repo |
| [QwenAudio/CosyVoice](https://github.com/QwenAudio/CosyVoice) | 24K | Multilingual voice generation from the Qwen team | Apache-2.0 |
| [nari-labs/dia](https://github.com/nari-labs/dia) | 19.4K | Two-speaker dialogue in one pass | Apache-2.0 |
| [SWivid/F5-TTS](https://github.com/SWivid/F5-TTS) | 15.4K | Fast zero-shot voice cloning | MIT |
| [hexgrad/kokoro](https://github.com/hexgrad/kokoro) | 9.3K | Tiny 82M TTS that runs anywhere | Apache-2.0 |

## Faces, avatars and lip-sync

| Repo | Stars | What it does for an ad | Code license |
|---|---:|---|---|
| [KlingAIResearch/LivePortrait](https://github.com/KlingAIResearch/LivePortrait) | 19.2K | Animate a portrait from a driving video | Not detected, see repo |
| [duixcom/Duix-Avatar](https://github.com/duixcom/Duix-Avatar) | 15.9K | Offline avatar (digital human) video toolkit | Not detected, see repo |
| [OpenTalker/SadTalker](https://github.com/OpenTalker/SadTalker) | 14.1K | Talking head from one photo and audio | Not detected, see repo |
| [Rudrabha/Wav2Lip](https://github.com/Rudrabha/Wav2Lip) | 13.2K | The classic lip-sync model | Not detected, see repo |
| [MeiGen-AI/InfiniteTalk](https://github.com/MeiGen-AI/InfiniteTalk) | 8.1K | Unlimited-length talking video, image or video in | Apache-2.0 |
| [TMElyralab/MuseTalk](https://github.com/TMElyralab/MuseTalk) | 6.7K | Real-time lip-sync | Not detected, see repo |
| [bytedance/LatentSync](https://github.com/bytedance/LatentSync) | 6.1K | ByteDance's diffusion lip-sync | Apache-2.0 |
| [antgroup/echomimic](https://github.com/antgroup/echomimic) | 4.3K | Audio-driven portrait animation | Apache-2.0 |

## Translate and dub

| Repo | Stars | What it does for an ad | Code license |
|---|---:|---|---|
| [jianchang512/pyvideotrans](https://github.com/jianchang512/pyvideotrans) | 19.4K | Translate a video, add dubbing and subtitles | GPL-3.0 |
| [Huanshere/VideoLingo](https://github.com/Huanshere/VideoLingo) | 18.8K | Subtitle cutting, translation, alignment and dubbing | Apache-2.0 |
| [krillinai/OpenCreator](https://github.com/krillinai/OpenCreator) | 13.1K | Video translation and dubbing (formerly KrillinAI) | Apache-2.0 |
| [buxuku/SmartSub](https://github.com/buxuku/SmartSub) | 5.7K | Desktop app: subtitles, translation, cloned-voice dubbing | MIT |
| [liuzhao1225/YouDub-webui](https://github.com/liuzhao1225/YouDub-webui) | 5.7K | Localize and dub videos end to end | Apache-2.0 |
| [Kedreamix/Linly-Dubbing](https://github.com/Kedreamix/Linly-Dubbing) | 3.4K | Multilingual AI dubbing | Apache-2.0 |
| [ThioJoe/Auto-Synced-Translated-Dubs](https://github.com/ThioJoe/Auto-Synced-Translated-Dubs) | 1.7K | Dubs synced to the original subtitle timing | AGPL-3.0 |
| [R3gm/SoniTranslate](https://github.com/R3gm/SoniTranslate) | 1.4K | Synchronized video translation | Apache-2.0 |

## Transcribe, cut and caption

| Repo | Stars | What it does for an ad | Code license |
|---|---:|---|---|
| [openai/whisper](https://github.com/openai/whisper) | 110.5K | Speech recognition behind most auto-captions | MIT |
| [FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg) | 65.2K | The engine under nearly every video pipeline | Not detected, see repo |
| [ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp) | 54.4K | Whisper on a laptop CPU | MIT |
| [SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper) | 25.9K | Whisper, several times faster | MIT |
| [m-bain/whisperX](https://github.com/m-bain/whisperX) | 24.6K | Word-level timestamps for captions | BSD-2-Clause |
| [WyattBlue/auto-editor](https://github.com/WyattBlue/auto-editor) | 5.5K | Cut silences and dead air automatically | Unlicense |
| [Breakthrough/PySceneDetect](https://github.com/Breakthrough/PySceneDetect) | 5.2K | Find every cut and scene change | BSD-3-Clause |

## Check whether the ad will sell

| Repo | Stars | What it does for an ad | Code license |
|---|---:|---|---|
| [google-marketing-solutions/abcds-detector](https://github.com/google-marketing-solutions/abcds-detector) | 74 | Scores a video against YouTube's ABCD framework with Gemini (from Google Marketing Solutions; not an official Google product) | Apache-2.0 |
| [creatify-ai/ad-creative-evaluator](https://github.com/creatify-ai/ad-creative-evaluator) | 31 | Claude skill: three AI personas score an ad on 8 dimensions | MIT |
| [AdReadyAI/adready-ai](https://github.com/AdReadyAI/adready-ai) | 13 | Pre-launch ad scorecard; per its README, scoring isn't implemented yet | MIT |

Know another open-source tool that checks a video ad before launch? Open a pull request.

Want a check right now: [Quelta](https://quelta.ai/?utm_source=github&utm_medium=awesome&utm_campaign=awesome-ai-video-ads) reviews a vertical video ad for a platform, country and audience age, scores it 0–100 and timecodes every mistake. Free, 5 reviews a day, no sign-up.

## On Hugging Face

| Model | Likes | Downloads, last 30 days |
|---|---:|---:|
| [hexgrad/Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) | 7.3K | 10.5M |
| [MiniMaxAI/MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3) | 6.1K | 3.8M |
| [Lightricks/LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) | 7.8K | 1.8M |
| [ResembleAI/chatterbox](https://huggingface.co/ResembleAI/chatterbox) | 1.8K | 1.6M |
| [microsoft/VibeVoice-1.5B](https://huggingface.co/microsoft/VibeVoice-1.5B) | 2.5K | 603.7K |
| [IndexTeam/IndexTTS-2](https://huggingface.co/IndexTeam/IndexTTS-2) | 790 | 12.8K |
| [Wan-AI/Wan2.2-I2V-A14B](https://huggingface.co/Wan-AI/Wan2.2-I2V-A14B) | 908 | 10.1K |
| [tencent/HunyuanVideo-1.5](https://huggingface.co/tencent/HunyuanVideo-1.5) | 1.1K | 1.3K |

## Contributing

Pull requests welcome. Add the repo to the right section with one line on what it does for an ad. Repos that only do face swaps of real people are left out on purpose.

Maintained by [Quelta](https://quelta.ai/?utm_source=github&utm_medium=awesome&utm_campaign=awesome-ai-video-ads).
