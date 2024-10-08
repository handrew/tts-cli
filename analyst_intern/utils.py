"""Intern utils."""

import os
from openai import OpenAI
from langchain_text_splitters import TokenTextSplitter
from wordcel.llms import openai_call, anthropic_call, gemini_call


def llm_call(prompt, model="openai"):
    """LLM call router."""
    if model == "openai":
        return openai_call(prompt)
    elif model == "anthropic":
        return anthropic_call(prompt)
    elif model == "gemini":
        return gemini_call(prompt)
    else:
        raise ValueError(f"Unsupported LLM provider: {model}")


"""TTS utils."""


def openai_tts(text, voice="nova", model="tts-1"):
    """Uses openai to generate speech."""
    client = OpenAI()
    response = client.audio.speech.create(model=model, voice=voice, input=text)
    return response


def split_text(text, chunk_size=500, chunk_overlap=0):
    """Split text using TokenTextSplitter."""
    text_splitter = TokenTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    texts = text_splitter.split_text(text)
    return texts


def stitch_mp3s_together(fpaths, outpath):
    """Stitch mp3s together."""
    cmd = f"""ffmpeg -i 'concat:{
        '|'.join(fpaths)
    }' -c copy {outpath}"""
    os.system(cmd)
