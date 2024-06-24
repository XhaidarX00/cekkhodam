import os
from app.src.helpers.msg_types import Types
from app import Bot, bot, OWNER_ID


async def send_cmd(client: Bot, msgtype: int):
    GET_FORMAT = {
        Types.TEXT.value: client.send_message,
        Types.DOCUMENT.value: client.send_document,
        Types.PHOTO.value: client.send_photo,
        Types.VIDEO.value: client.send_video,
        Types.STICKER.value: client.send_sticker,
        Types.AUDIO.value: client.send_audio,
        Types.VOICE.value: client.send_voice,
        Types.VIDEO_NOTE.value: client.send_video_note,
        Types.ANIMATION.value: client.send_animation,
        Types.ANIMATED_STICKER.value: client.send_sticker,
        Types.CONTACT: client.send_contact,
    }
    return GET_FORMAT[msgtype]


async def write_to_file(data, filename):
    with open(filename, 'w') as file:
        file.write(data)
        
async def send_document(data, filename):
    await write_to_file(str(data), filename)
    await bot.send_document(OWNER_ID, filename, caption=str(filename))
    
    if os.path.exists(filename):
        os.remove(filename)
    