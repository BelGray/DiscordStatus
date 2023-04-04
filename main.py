from pypresence import Presence
import time
from time import time

rpc = Presence("1072428976066269184")
rpc.connect()
while True:
  rpc.update(
    state="ReMolla - combining ideas & opportunities!",
    start=time(),
    buttons=[
        {
            "label":"Add ReMolla",
            "url":"https://discord.com/api/oauth2/authorize?client_id=1072428976066269184&permissions=140660567120&scope=bot%20applications.commands"
        },
        {
            "label":"Support Server",
            "url":"https://discord.gg/T9ruJk6QD2"
        },
    ],
    large_image="remolla",
    small_image="javalogo",
    large_text="Have you ever wondered why this particular avatar?",
    small_text="Our bot written in Java"
)
