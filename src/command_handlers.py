import textwrap
import sqlite3

from src.database import disable_posts

async def start_command(update, context):
    """Send a message when the command /start is issued."""
    reply = """
    
    Hi, this is the meeple matchmaker bot.
    
    I'm here to help match buyers and sellers in the Meeple Market Telegram Channel
        
    ## How do I work?
    
    I use two things from a posted message in the group
    
    - a message tag, supported tags are: #lookingfor, #sale, #selling, #seekinginterest, #sell
    - a game name, the more accurately your name matches the BGG name, the better your chances of success
        
    Example:
    
    Deepak posts a message
    ```
    #lookingfor Ark Nova
    ```
    
    Chaitanya posts a message
    ```
    #lookingfor Ark Nova
    ```
    
    Tanuj posts a message a few days later
    ```
    #seekinginterest Ark Nova
    ```
    
    The bot will reply to Tanuj's message and tag Deepak and Chaitanya
    ```
    @Deepak @Chaitanya
    ```
    
    ## How do I stop the notifications?
    Go to the bot chat and type /disable
    This will stop all tags for you for all games
    
    We currently do not support disabling notifications for specific games but watch this space for an update
    on that
    
    """
    await update.message.reply_text(textwrap.dedent(reply), parse_mode="Markdown")

async def disable_notifications(update, context):
    conn = sqlite3.connect("meeple-matchmaker")
    user_id = update.message.from_user.id
    with conn:
        cur = conn.cursor()
        disable_posts(cur, user_id)
        conn.commit()

    conn.close()
