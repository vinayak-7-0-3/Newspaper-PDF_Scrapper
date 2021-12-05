from helpers.sorted_news import *
from pyrogram import Client, filters
from helpers.check_list import check_list
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


@Client.on_message(filters.command("news"))
async def news(client, message):
    await client.send_message(
        message.chat.id,
        "Choose Your Language",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "English",
                        callback_data="english"
                    ),
                    InlineKeyboardButton(
                        "Hindi",
                        callback_data="hindi"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Telugu",
                        callback_data="telugu"
                    ),
                    InlineKeyboardButton(
                        "Marathi",
                        callback_data="marathi"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Bengali",
                        callback_data="bengali"
                    ),
                    InlineKeyboardButton(
                        "Gujarati",
                        callback_data="gujarati"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Punjabi",
                        callback_data="punjabi"
                    ),
                    InlineKeyboardButton(
                        "Tamil",
                        callback_data="tamil"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Malayalam",
                        callback_data="malayalam"
                    ),
                    InlineKeyboardButton(
                        "Kannada",
                        callback_data="kannada"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Urdu",
                        callback_data="urdu"
                    ),
                    InlineKeyboardButton(
                        "Odiya",
                        callback_data="odiya"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Assamese",
                        callback_data="assamese"
                    )
                ]
            ]
        ),
        reply_to_message_id=message.message_id
    )

@Client.on_callback_query(filters.regex("^(english|hindi|telugu|marathi|bengali|gujarati|punjabi|tamil|malayalam|kannada|urdu|odiya|assamese)$"))
async def english(c: Client, cb: CallbackQuery):
    inline_keyboard = []
    cb_news_lang = f"{cb.data}_list"
    cb_news_name = f"{cb.data}_name"
    i = 0
    while i < len(cb_news_lang):
        if cb_news_lang[i] and cb_news_lang[i+1] is not None:
            inline_keyboard.append([
                InlineKeyboardButton(
                    cb_news_lang[i],
                    callback_data=cb_news_name[i]
                ),
                InlineKeyboardButton(
                    cb_news_lang[i+1],
                    callback_data=cb_news_name[i+1]
                )
            ])
        elif cb_news_lang[i+1] is None and cb_news_lang[i] is not None:
            inline_keyboard.append([
                InlineKeyboardButton(
                    cb_news_lang[i],
                    callback_data=cb_news_name[i]
                )
            ])
        i += 2

        await c.edit_message_text(
            chat_id=cb.message.chat.id,
            text=f"<b>Choose Your News Paper</b>",
            message_id=cb.message.message_id,
            reply_markup=InlineKeyboardMarkup(inline_keyboard)
        )





