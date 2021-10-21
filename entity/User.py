class User:
    def __init__(self, telegram_id, name, phone):
        self._telegram_id = telegram_id or "не указан"
        self._name = name or "не указан"
        self._phone = phone or "не указан"

    def get_telegram_id(self):
        return self._telegram_id

    def set_telegram_id(self, value):
        self._telegram_id = value

    def del_telegram_id(self):
        del self._telegram_id

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def del_name(self):
        del self._name

    def get_phone(self):
        return self._phone

    def set_phone(self, value):
        self._phone = value

    def del_phone(self):
        del self._phone

    telegram_id = property(get_telegram_id, set_telegram_id, del_telegram_id)
    name = property(get_name, set_name, del_name)
    phone = property(get_phone, set_phone, del_phone)
