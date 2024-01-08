

from bardapi import BardCookies

cookies = {
    "__Secure-1PSID": "***",
    "__Secure-1PSIDTS": "****",
    "__Secure-1PSIDCC": "****"
}


import os
import openai
import io
import pygame
def speak(content):
    bard = BardCookies(cookie_dict=cookies)
    # print(bard.get_answer("who is ceo of alphabet"))
    data = bard.speech(f"{content}")['audio']

    def play_audio_from_bytes(audio_bytes):
        audio_stream = io.BytesIO(audio_bytes)
        pygame.init()
        pygame.mixer.music.load(audio_stream)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        pygame.mixer.quit()
        pygame.quit()

    audio_bytes = data  
    play_audio_from_bytes(audio_bytes)




