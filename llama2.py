from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

# Prompt to Llama 3.2 1B Model on Raspberry Pi 5 Ollama (4bit Quantized)
  
# """
# Here's 22:30 sensor readings:

# Room B4: Temperature 25C, Humidity 5%, no one in this room for 30 minutes, TV is still on, air conditioner is on, Lights on.
# Room B5: Temperature 15C, Humidity 10%, people in the room, TV is on, air conditioner is off, Lights on.
# Evaluate the situation, and decide the Next Best Action,
# Output your IoT Instruction in the following format.  For each instruction, use the following format

# >> <Room Name>: <Device Name> - <Command> 
# >> <Room Name>: <Device Name> - <Command>
# >> ...

# After all instructions listed, explain your rationale very very concisely, and say "all instructions have been successfully sent out and my rationale logged for system records and improvements."
# """

# Response from Llama 3.2 1B Model on Raspberry Pi 5 Ollama (4bit Quantized) TTFT 30 seconds

result = """
I'm llama 3.2 1Billion Model . 
Here are the IoT instructions to resolve the situation:

>> B4: Heating System - Adjust Temperature
>> B5: LED Lighting - Turn Off

Now, let's evaluate the situation:

In Room B4, both occupants have been present for 30 minutes, which suggests that everyone is still sleeping. Since the TV and air conditioner are still on, it's likely that someone is trying to get comfortable or adjust the temperature temporarily.

In Room B5, there are two people present after 20 minutes, indicating that they are actively participating in activities. If the air conditioner is turned off, the occupants may not want the heating system to be on unnecessarily. The lights remain on, which could be wasting energy if it's not essential.

To resolve this situation, I recommend adjusting the temperature and switching off any unnecessary systems. Here's the optimized sequence:

>> B4: Heating System - Turn Off
>> B5: No Action (as there are still two people awake)

Next best action

I would suggest turning off the TV in Room B4 to minimize further energy consumption while also ensuring that no one is left alone.

I have successfully sent out all instructions and my rationale logged for system records and improvements.
2024-11-17 09:25:06,214 - INFO - Playing voice: Here are the IoT instructions to resolve the situation:

>> B4: Heating System - Adjust Temperature
>> B5: LED Lighting - Turn Off

Now, let's evaluate the situation:

In Room B4, both occupants have been present for 30 minutes, which suggests that everyone is still sleeping. Since the TV and air conditioner are still on, it's likely that someone is trying to get comfortable or adjust the temperature temporarily.

In Room B5, there are two people present after 20 minutes, indicating that they are actively participating in activities. If the air conditioner is turned off, the occupants may not want the heating system to be on unnecessarily. The lights remain on, which could be wasting energy if it's not essential.

To resolve this situation, I recommend adjusting the temperature and switching off any unnecessary systems. Here's the optimized sequence:

>> B4: Heating System - Turn Off
>> B5: No Action (as there are still two people awake)

Next best action

I would suggest turning off the TV in Room B4 to minimize further energy consumption while also ensuring that no one is left alone.

I have successfully sent out all instructions and my rationale logged for system records and improvements.
"""

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
            api_key=os.getenv("ELEVENLAB_API_KEY")
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