from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


BATCH_MESSAGE = BATCH = """
Need to shorten or convert links from all of your channel's posts? I've got you covered! Just make me an admin in your channel and use the following command:

<code>/batch [channel id or username]</code>

For example: <code>/batch -100xxx</code>

I'll handle the rest and get those links shortened or converted in a short time! 💪
"""

START_MESSAGE = """
**Hi {} 

I am BDSHORTNER Bulk Link Converter Bot. I Can Convert Links Directly From Your BDSHORTNER Account,
    
1. Go To https://bdshortner.com/member/tools/api
2. Then Copy API Key
3. Then Type /api than give a single space and than paste your API Key (see example to understand more...)

To learn more about what I can do, just 
type /help.**

"""

HELP_MESSAGE = """**Hey there! My name is {firstname} and I'm a link convertor and shortener bot here to make your work easier and help you earn more 💰.

I have a ton of handy features to help you out, such as:

- https://t.me/naimur_0 (support) 🔗
- Button conversion support 
- Header and footer text support 📝
- Replace username function 📎
- Banner image support 🖼️

Useful commands:

- /help: Send this message; I'll tell you more about myself!**
"""

ABOUT_TEXT = """
**My Details:

`🤖 Name:` ** {} **
    
`📝 Language:` [Python 3](https://www.python.org/)
`🧰 Framework:` [Pyrogram](https://github.com/pyrogram/pyrogram)**
"""


METHOD_MESSAGE = """
"""

CUSTOM_ALIAS_MESSAGE = """For custom alias, `[link] | [custom_alias]`, Send in this format

This feature works only in private mode only

Ex: https://t.me/example | Example"""


ADMINS_MESSAGE = """
List of Admins who has access to this Bot

{admin_list}
"""


CHANNELS_LIST_MESSAGE = """
Here is a list of the channels:

{channels}"""

HELP_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("", callback_data=""),
            InlineKeyboardButton("", callback_data=""),
        ],
        [
            InlineKeyboardButton("", callback_data=""),
            InlineKeyboardButton("", callback_data=""),
        ],
        [
            InlineKeyboardButton("", callback_data=""),
            InlineKeyboardButton("", callback_data=""),
        ],
    ]
)


ABOUT_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Home", callback_data="start_command"),
            InlineKeyboardButton("Help", callback_data="help_command"),
        ],
        [InlineKeyboardButton("Close", callback_data="delete")],
    ]
)

START_MESSAGE_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("", callback_data=""),
            InlineKeyboardButton("", callback_data=""),
        ],
        [
            InlineKeyboardButton("", callback_data=""),
            InlineKeyboardButton("", callback_data=("")),
        ],
    ]
)

METHOD_REPLY_MARKUP = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                "", callback_data=""
            ),
            InlineKeyboardButton(
                "", callback_data=""
            ),
            InlineKeyboardButton("", callback_data=""),
        ],
        [
            InlineKeyboardButton("", callback_data=""),
            InlineKeyboardButton("", callback_data=""),
        ],
    ]
)

BACK_REPLY_MARKUP = InlineKeyboardMarkup(
    [[InlineKeyboardButton("", callback_data="")]]
)

USER_ABOUT_MESSAGE = """**
🔧 Here are the current settings for this bot:

- 🌐 Shortner website: bdshortner.com

- ✅ API: {shortener_api}

- 📎 Username: @{username}

- 📝 Header text:
{header_text}

- 📝 Footer text:
{footer_text}

🖼️ Banner image: {banner_image}**
"""



SHORTENER_API_MESSAGE = """**🔰Go To BDSHORTNER website. 
🔰Then Copy API Key. 
🔰Then Type /shortener_api then give a single space and then paste your API Key & press Enter
            
Example: `/shortener_api 6LZq851sXofffPHugiKQq`

Go to 'https://bdshortner.com/member/tools/api'


Current Shortener API: `{shortener_api}`**"""

HEADER_MESSAGE = """**📝 To set the header text for every message caption or text, just reply with the text you want to use. You can use \\n to add a line break.

🗑 To remove the header text, use the following command:

`/header remove`

This is a helpful way to add a consistent header to all of your messages. Enjoy! **🎉"""

FOOTER_MESSAGE = """**📝 To set the footer text for every message caption or text, just reply with the text you want to use. You can use \\n to add a line break.

🗑 To remove the footer text, use the following command:

`/footer remove`

This is a helpful way to add a consistent footer to all of your messages. Enjoy! **🎉"""

USERNAME_TEXT = """**Current username: {username}

To set the username that will be automatically replaced with other usernames in the post, use the following command:

`/username your_username`

__(Note: Do not include the @ symbol in your username.)__

To remove the current username, use the following command:

`/username remove`

This is a helpful way to make sure that all of your posts have a consistent username. Enjoy! 📎**"""

BANNER_IMAGE = """**
Usage: `/banner_image image_url` or reply to any Image with this command

This image will be automatically replaced with other images in the post

To remove custom image, `/banner_image remove`

Eg: `/banner_image https://www.nicepng.com/png/detail/436-4369539_movie-logo-film.png`**"""

INCLUDE_DOMAIN_TEXT = """
Use this option if you want to short only links from the following domains list.

Current Include Domain:
{}
Usage: /include_domain domain
Ex: `/include_domain t.me, stack.com`

To remove a domain,
Ex: `/include_domain remove t.me`

To remove all domains,
Ex: `/include_domain remove_all`
"""

EXCLUDE_DOMAIN_TEXT = """
Use this option if you wish to short every link on your channel but exclude only the links from the following domains list

Current Exclude Domains:
{}
Usage: /exclude_domain domain
Ex: `/exclude_domain t.me, google.com`

To remove a domain, 
Ex: `/exclude_domain remove t.me`

To remove all domains,
Ex: `/exclude_domain remove_all`
"""

BANNED_USER_TXT = """
Usage: `/ban [User ID]`
Usage: `/unban [User ID]`

List of users that are banned:

{users}
"""
