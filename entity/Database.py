import json
from entity.User import User

class Database:
    def __init__(self):
        self.factoryUser = {}
        self.load()

    def user(self, telegram_id):
        return self.factoryUser[telegram_id]

    def exitsUser(self, telegram_id):
        return telegram_id in self.factoryUser

    def createUser(self, telegram_id):
        user = User(telegram_id, None, None)
        self.factoryUser[telegram_id] = user
        self.save()
        return user

    def load(self):
        with open('database.json') as json_file:
            database = json.load(json_file)
            for telegram_id in database:
                user_data = database[telegram_id]
                user = User(user_data["telegram_id"], user_data["name"], user_data["phone"])
                self.factoryUser[telegram_id] = user

    def save(self):
        dump = {}
        for telegram_id in self.factoryUser:
            user = self.factoryUser[telegram_id]

            dump[telegram_id] = {}
            dump[telegram_id]["telegram_id"] = user.telegram_id
            dump[telegram_id]["name"] = user.name
            dump[telegram_id]["phone"] = user.phone

        with open('database.json', 'w') as outfile:
            json.dump(dump, outfile)