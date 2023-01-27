
class Msg:
    def __init__(self, user_id, text, direction, message_id):
        self.user_id = user_id
        self.text = text
        self.direction = direction
        self.message_id = message_id


class User:
    def __init__(self, tg_id, is_bot, username, first_name, last_name):
        self.tg_id = tg_id
        self.is_bot = is_bot
        self.username = username
        self.first_name = first_name
        self.last_name = last_name


