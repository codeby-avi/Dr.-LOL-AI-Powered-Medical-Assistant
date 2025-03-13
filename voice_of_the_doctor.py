
#Step1a: Setup Text to Speech–TTS–model with gTTS
import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)


input_text="Hi this is AI with Avinash!"
#text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

#Step1b: Setup Text to Speech–TTS–model with ElevenLabs
import elevenlabs
from elevenlabs.client import ElevenLabs

#ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    client=ElevenLabs(api_key="sk_5f44f7f8a47d8145f85163c9980ab0218922174d2362c59c")
    audio=client.generate(
        text= input_text,
        voice= "Aria",
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)

#text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3") 

#Step2: Use Model for Text output to Voice

import subprocess
import platform
from pydub import AudioSegment

AudioSegment.converter = "C:\ffmpeg\ffmpeg-7.1-essentials_build\bin\ffmpeg.exe"

import os
import platform
import pygame
import subprocess
from gtts import gTTS

def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"

    # Generate speech and save as MP3
    audioobj = gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

    # Initialize pygame mixer and play audio
    try:
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(output_filepath)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():  # Wait for the audio to finish
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

input_text = "Hi, this is Dr. LOL Because laughter is the best medicine!!"
# text_to_speech_with_gtts(input_text, "gtts_testing_autoplay.mp3")


def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key="sk_5f44f7f8a47d8145f85163c9980ab0218922174d2362c59c")
    
    # Generate speech using ElevenLabs API
    audio = client.generate(
        text=input_text,
        voice="Aria",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )

    # Save the generated speech
    elevenlabs.save(audio, output_filepath)

    # Play audio using pygame
    try:
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(output_filepath)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():  # Wait for the audio to finish
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

text_to_speech_with_elevenlabs("Hi, this is Dr. LOL Because laughter is the best medicine!!", "elevenlabs_testing_autoplay.mp3")