from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message
from JioSavaan import app
from JioSavaan.core.call import Anony
from JioSavaan.utils.decorators.language import language
from JioSavaan.utils.inline import supp_markup
from pytgcalls import PyTgCalls, idle
from pytgcalls.types import GroupCallParticipant
from config import BANNED_USERS

# Initialize PyTgCalls with User Client
pytgcalls = Anony

# Handler for when a user joins the voice chat
@pytgcalls.on_participant_joined()
async def on_user_joined(client, update: GroupCallParticipant):
    chat_id = update.chat_id
    user_id = update.user_id
    user_info = await client.get_users(user_id)
    message = f"🎤 **{user_info.first_name}** joined the voice chat!"
    await app.send_message(chat_id, message)

# Handler for when a user leaves the voice chat
@pytgcalls.on_participant_left()
async def on_user_left(client, update: GroupCallParticipant):
    chat_id = update.chat_id
    user_id = update.user_id
    user_info = await client.get_users(user_id)
    message = f"🚫 **{user_info.first_name}** left the voice chat."
    await app.send_message(chat_id, message)

