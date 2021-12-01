from sample_config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command(["start"]))
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text="Hi",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support Group", url="https://t.me"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Owner", url="https://t.me"
                    )
                ],

            ]
        ),
        reply_to_message_id=update.message_id
        )