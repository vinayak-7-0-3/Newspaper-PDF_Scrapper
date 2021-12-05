import sys
from helpers.sorted_news import *
from pyrogram import Client, filters
from helpers.check_list import check_list
from helpers.get_link import get_news_direct_link
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

news_lang_regex = "^(english|hindi|telugu|marathi|bengali|gujarati|punjabi|tamil|malayalam|kannada|urdu|odiya|assamese)$"

@Client.on_message(filters.command(["news", "shell@indian_newspapers_bot"]))
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
                ],
                [
                    InlineKeyboardButton(
                        "Close",
                        callback_data="close"
                    )
                ]
            ]
        ),
        reply_to_message_id=message.message_id
    )

@Client.on_callback_query(filters.regex(news_lang_regex))
async def choose_news(c: Client, cb: CallbackQuery):

    news_name = getattr(sys.modules[__name__], cb.data + "_name")
    news_list = getattr(sys.modules[__name__], cb.data + "_list")

    inline_keyboard = []
    i = 0
    while i < len(news_name):
        if news_name[i] and news_name[i+1] is not None:
            inline_keyboard.append([
                InlineKeyboardButton(
                    news_name[i],
                    callback_data=news_list[i]
                ),
                InlineKeyboardButton(
                    news_name[i+1],
                    callback_data=news_list[i+1]
                )
            ])
        elif news_name[i+1] is None and news_name[i] is not None:
            inline_keyboard.append([
                InlineKeyboardButton(
                    news_name[i],
                    callback_data=news_list[i]
                )
            ])
        i += 2
    inline_keyboard.append([
        InlineKeyboardButton(
            "Close",
            callback_data="close"
        )
    ])
    await c.edit_message_text(
        chat_id=cb.message.chat.id,
        text=f"<b>Choose Your News Paper</b>",
        message_id=cb.message.message_id,
        reply_markup=InlineKeyboardMarkup(inline_keyboard)
    )

@Client.on_callback_query(~filters.regex(news_lang_regex) & ~filters.regex("close"))
async def get_news(c: Client, cb: CallbackQuery):
    news_link = "https://www.fresherwave.com/" + cb.data + "/"

    name, url = await get_news_direct_link(news_link)
    inline_keyboard = []
    for i in range(len(name)):
        inline_keyboard.append([
            InlineKeyboardButton(
                name[i],
                url=url[i]
            )
        ])
    inline_keyboard.append([
        InlineKeyboardButton(
            "Close",
            callback_data="close"
        )
    ])
    await c.edit_message_text(
        chat_id=cb.message.chat.id,
        text=f"<b>Choose The Date</b>",
        message_id=cb.message.message_id,
        reply_markup=InlineKeyboardMarkup(inline_keyboard)
    )
    
@Client.on_callback_query(filters.regex("close"))
async def cancel(c: Client, cb: CallbackQuery):
    await c.delete_messages(
        chat_id=cb.message.chat.id,
        message_ids=cb.message.message_id
    )
    try:
        await c.delete_messages(
            chat_id=cb.message.chat.id,
            message_ids=cb.message.reply_to_message.message_id
        )
    except:
        pass









