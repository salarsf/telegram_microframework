from bot import TelegramBot


bot = TelegramBot("config.cfg")

"""
    You can configure create_response_text function to generate your own logic for replys
"""

def create_response_text(user_message):
    message_received = user_message["message"]["text"]
    return f"You said '{message_received}'"

offset = None
while True:
    updates = bot.get_updates(offset)
    updates = updates["result"]
    if updates:
        for item in updates:
            offset = item["update_id"]
            user_id = item["message"]["from"]["id"]
            response = create_response_text(item)
            bot.send_message(response,user_id)