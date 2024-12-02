
## Background

Over the 24 hours of Meta Llama Impact Hackathon London, I managed to have build a completely working prototype Edge AI for elderly people living indepently to save energy.  Coined by my team mate Lorraine David, Climatic AI (last 3 characters CAI :), is the name we submitted here at the end of the hackathon.

### Rough cut video presentation: click below to open Youtube video

<a href="http://www.youtube.com/watch?feature=player_embedded&v=aPSZSrSpPsQ" target="_new">
 <img src="https://img.youtube.com/vi/aPSZSrSpPsQ/0.jpg" alt="Climatic AI - Energy Saver" width="480" height="360" border="10" />
</a>

> Super intelligent AI Agent monitors IoT environmental sensors and people proximities, advanced reasoning engine powered by Meta Llama 3.2 1B on a Raspberry Pi to look after people's safety, comfortableness, and energy savings automatically.

***Chapters in the 3-minute video:***
1. Problem statement: thousands of death caused by energy cost crisis in UK between 2022-2023.
2. Working Demo of Raspberry Pi 5 8GB running Llama 3.2 1B/8bit and 3B/4-bit (Completely Local on the edge device - via Docker Container / Ollama)
3. Voice TTS via ElevenLab API (Internet Access required)
4. Working demo of environment sensors reading (running entirely on the edge device - via Home Assistant Docker Container)
5. Working demo of learn and emulate the LG TV remote controller at the hackathon venue, and LLM instructed turning on and off of the TV via a cheap pair of Infra-red receiver and transmitter on the IoT Device.

### Main source code used in the hackathon:

| # | Code | Description |
| --- | --- | --- |
| 1 | `llama1.py` | local Llama 3.2 1B and 3B running on Raspberry Pi 5 8GB |
| 2 | `llama2.py` | ElevenLab Voice TTS API sample reading out of LLM 3.2 output including its reasoning rationale |

### PS: 1 December 2024 Update

***Post Hackathon Development Updates:***

| # | Description | Photos |
| --- | --- | --- |
| 0 | Various mockups of the final AIoT product (using various Text2SQL image generator) | ![image (1)](https://github.com/user-attachments/assets/b3449643-0c7d-4222-8633-cada1cb7f48d) |
|  |  | ![image (6)](https://github.com/user-attachments/assets/676ade2c-8db5-455a-8b83-ba724c510b27) |
| 1 | Round LED monitor to simulate final product, dual monitor setup as a dev environment for UI / UX design (Three.js running via Chronium Browser | ![dev-setup1](https://github.com/user-attachments/assets/0eddc744-e9d5-447b-962c-fd2ecd0545a7) |
| 2 | Another dual monitor (one for dedicated metrics monitoring) setup for LLM edge computing optmization, Bigger round shapped LED screen for better illustration, External Speaker for Hi-Fi voice and Music / Streaming use case, Piper TTS working on the edge. | ![dev-setup0](https://github.com/user-attachments/assets/cf9cb992-6a6b-4136-837d-d2576748b4a0) |

***Planned evaluations in the coming week:***

1. Vision Model calling via Internet (already tested not possible to run on the edge)
2. non LLM/VLM Computer Vision via Pi Camera on the edge device (e.g. OpenCV, POSE, ...)
3. ASR test via dual microphone, 6-microphone array (to test under noisy, weak volume scenarios)
4. ...

Charles Cai
