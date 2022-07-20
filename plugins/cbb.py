from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b> • OWNER : <code>@ninja_00p</code>\n○ • Channel : @DarkRubix \n○ • Group : @DarkRubix_org </b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(

         [[ InlineKeyboardButton("Movies Channel" ,url="https://t.me/MoviesSearchBox") ]  ]))

                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "clos
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Doc
