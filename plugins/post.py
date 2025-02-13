import re
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode
from info import POST_CHANNEL, ADMINS

# Known languages for filtering
known_languages = {
    "arabic", "assamese", "bengali", "burmese", "chinese", "czech", "dutch", "english",
    "filipino", "french", "german", "gujarati", "hindi", "hungarian", "indonesian",
    "italian", "japanese", "kannada", "korean", "malay", "malayalam", "marathi",
    "nepali", "pashto", "persian", "polish", "portuguese", "punjabi", "russian",
    "sinhala", "spanish", "swedish", "tamil", "telugu", "thai", "turkish",
    "ukrainian", "urdu", "vietnamese"
}

@Client.on_message(filters.command("post"))
async def generate_post(client, message):
    if message.from_user.id not in ADMINS:
        await message.reply_text("You are not authorized to use this command.")
        return

    if len(message.command) < 2:
        await message.reply_text("Please provide a movie title and optional year/season (e.g., /post KGF 2018 S01 Tamil Telugu)")
        return

    user_input = message.command[1:]

    # Identify season identifier (e.g., S01, S02)
    season_identifier = None
    pattern = re.compile(r"\b[Ss](\d{2})\b")
    for item in user_input:
        if pattern.match(item):
            season_identifier = item.upper()
            user_input.remove(item)
            break

    # Extract languages
    languages = []
    while user_input and user_input[-1].lower() in KNOWN_LANGUAGES:
        languages.append(user_input.pop().capitalize())

    # Extract year
    year = None
    for item in user_input:
        if item.isdigit() and len(item) == 4:
            year = item
            user_input.remove(item)
            break

    title = " ".join(user_input)
    languages_text = ", ".join(f"#{lang}" for lang in languages) if languages else "Unknown"
    season_text = f" ({season_identifier})" if season_identifier else ""

    # Construct the button URL with spaces (%20) instead of underscores
    formatted_title = title.replace(" ", "%20").replace(".", "%20")
    if year:
        formatted_title += f"%20{year}"
    if season_identifier:
        formatted_title += f"%20{season_identifier}"
    
    button_url = f"tg://resolve?domain=ProSearchFatherBot&start&text={formatted_title}"

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔎 Click To Search 🔍", url=button_url)]
    ])

    message_text = f"""

<b>🎬 Title:</b> {title}{season_text} {year if year else ""}

<b>🔊 Audio:</b> {languages_text}
"""

    await client.send_message(
        chat_id=POST_CHANNEL,
        text=message_text,
        reply_markup=keyboard,
        parse_mode=ParseMode.HTML
    )

    await message.reply_text(f"Post for '{title} {season_text} {year if year else ''}' published successfully!")
