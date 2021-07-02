from random import choice, randint, uniform
from time import time, sleep

from pypresence import Presence
from requests import get

RPC = Presence(860442029669875742)

emoji_heart = ('❤️', '🧡', '💛', '💚', '💙', '🖤', '🤍')
sakura = '🌸'
emoji_other = ('💔', '💖', '💘', '💕', '💗', '💝', '💞')

def rpc_connect():
    RPC.connect()

def random_choices(list_to_random):
    return choice(list_to_random)

def string_generator():
        
    other_gen1 = random_choices(emoji_other)
    other_gen2 = random_choices(emoji_other)
    heart_gen1 = random_choices(emoji_heart)
    heart_gen2 = random_choices(emoji_heart)
    
    if randint(0, 1) == 1:
        lineString = f'{sakura} {heart_gen2} {sakura} {heart_gen1} {other_gen1} {heart_gen1} {sakura} {heart_gen2} {sakura}'
        return lineString
    
    else:
        lineString = f'{heart_gen1} {sakura} {heart_gen2} {sakura} {other_gen2} {sakura} {heart_gen2} {sakura} {heart_gen1}'
        return lineString

def anime_url_get():
    response = get('https://animego.org/anime/random')
    return response.url

def start_time_generator():
    start_time = uniform((time() - 604525), (time()))
    return start_time

def rpc_update():
    
    btn = [
    {
        "label": "Случайное аниме",
        "url": f"{anime_url_get()}"
    },
    {
        "label": "GitHub",
        "url": "https://github.com/"
    }
        ]
    
    RPC.update(
        state=f"{string_generator()}",
        details=f"{string_generator()}",
        buttons=btn,
        large_image=str(randint(1, 104)),
        #small_image=str(randint(1, 104)),
        start=start_time_generator()
        )

rpc_connect()
while True:
    rpc_update()
    sleep(5)