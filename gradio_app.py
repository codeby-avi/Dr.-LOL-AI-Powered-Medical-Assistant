
# VoiceBot UI with Gradio Modern Design
import os
import gradio as gr

from brain_of_the_doctor import encode_image, analyze_image_with_query
from voice_of_the_patient import record_audio, transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_gtts, text_to_speech_with_elevenlabs

# System prompt
system_prompt = """You have to act as a professional doctor, i know you are not but this is for learning purpose. 
            What's in this image?. Do you find anything wrong with it medically? 
            If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
            your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
            Donot say 'In the image I see' but say 'With what I see, I think you have ....'
            Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
            Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""


def process_inputs(audio_filepath, image_filepath):
    GROQ_API_KEY = "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"
    speech_to_text_output = transcribe_with_groq(audio_filepath=audio_filepath, stt_model="whisper-large-v3")

    # Handle the image input
    if image_filepath:
        doctor_response = analyze_image_with_query(query=system_prompt + speech_to_text_output, encoded_image=encode_image(image_filepath), model="llama-3.2-11b-vision-preview")
    else:
        doctor_response = "No image provided for me to analyze"

    voice_of_doctor = text_to_speech_with_elevenlabs(input_text=doctor_response, output_filepath="final.mp3")

    return speech_to_text_output, doctor_response, voice_of_doctor


# Modern UI using Gradio Blocks
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    # Title and description
    gr.Markdown(
        """
        # 🩺 Dr. LOL – Because laughter is the best medicine! 😂
            Created by Avinash Chavan 🚀✨
        """
    )

    with gr.Row():
        # Input column
        with gr.Column():
            gr.Markdown("### 🎤 Record Your Voice")
            audio_input = gr.Audio(sources=["microphone"], type="filepath", label="Speak here...")
            gr.Markdown("### 🖼️ Upload an Image ")
            image_input = gr.Image(type="filepath", label="Upload Image")

        # Output column
        with gr.Column():
            gr.Markdown("### 📝 Speech to Text")
            speech_to_text_output = gr.Textbox(label="Transcribed Text", interactive=False)
            gr.Markdown("### 🧑‍⚕️ Doctor's Response")
            doctor_response_output = gr.Textbox(label="Doctor's Analysis", interactive=False)
            gr.Markdown("### 🔊 Listen to the Doctor")
            audio_output = gr.Audio(label="Doctor's Voice", interactive=False)

    # Process button
    gr.Button("🚀 Process").click(
        fn=process_inputs,
        inputs=[audio_input, image_input],
        outputs=[speech_to_text_output, doctor_response_output, audio_output]
    )

# Launch the app
demo.launch(pwa=True)
# demo.launch(debug=True)


#http://127.0.0.1:7860