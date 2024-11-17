from openai import OpenAI
import os

from dotenv import load_dotenv
load_dotenv()

# Raspberry Pi 5 Local Ollama 
client = OpenAI(
    api_key="123", 
    base_url="http://172.20.10.2:11434/v1"
)

# # NEBIUS
# client = OpenAI(
#     api_key=os.getenv("NEBIUS_API_KEY")
#     base_url=os.getenv("NETBIUS_BASE_URL")
# )

# # Grop
# client = OpenAI(
#     api_key=os.getenv("GROQ_API_KEY")
#     base_url=os.getenv("GROQ_BASE_URL")
# )


models = client.models.list().data
print("Available models are:\n")
for model in models:
    print(model.id)

# Raspberry Pi 5 Ollama (4bit Quantized)
model = "llama3.2:1b"

# completion = client.chat.completions.create(
#     model = model,
#     messages = [
#         {"role": "system", "content": "You are a helpful assistant."},
#         {
#             "role": "user",
#             "content": "Write a haiku about recursion in why sky is blue."
#         }
#     ]
# )

completion = client.chat.completions.create(
    model = model,
    messages = [
        {"role": "system", "content":         
"""
You are a helpful assistant configured with IoT sensors and actuators (e.g. automatic remote control of TVs, refrigerators, lights, and switches of some appliances) at a care home for elder people, you are instructed to consider people's safety and comfort, while saving energy as much as possible.
Mrs and Mr Rainey live in Room B4 (Living room) and B5 (Bedroom) who are in their later sixties .
"""},
        {
            "role": "user",
            "content": 
"""
Here's 22:30 sensor readings:

Room B4: Temperature 25C, Humidity 5%, no one in this room for 30 minutes, TV is still on, air conditioner is on, Lights on.
Room B5: Temperature 15C, Humidity 10%, people in the room, TV is on, air conditioner is off, Lights on.
Evaluate the situation, and decide the Next Best Action,
Output your IoT Instruction in the following format.  For each instruction, use the following format

>> <Room Name>: <Device Name> - <Command> 
>> <Room Name>: <Device Name> - <Command>
>> ...

After all instructions listed, explain your rationale very very concisely, and say "all instructions have been successfully sent out and my rationale logged for system records and improvements."
"""
        }
    ]
)

result = completion.choices[0].message.content
print(result)


from elevenlabs import play
from elevenlabs.client import ElevenLabs, Voice, VoiceSettings
import logging
import asyncio

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("debug.log"), logging.StreamHandler()],
)

async def speak(text: str):
    try:
        logging.info(f"Playing voice: {text}")
        client = ElevenLabs(
            api_key=os.getenv("ELEVEN_API_KEY")
        )

        audio = client.generate(
            text=text,
            voice=Voice(
                voice_id="XB0fDUnXU5powFXDhCwa",
                settings=VoiceSettings(
                    stability=0.5,
                    similarity_boost=0.75,
                    style=0.0,
                    use_speaker_boost=False,
                ),
            ),
            model="eleven_turbo_v2_5",
        )
        await play(audio)

    except Exception as e:
        logging.error(f"Error occurred: {e}")

asyncio.run(speak(result))