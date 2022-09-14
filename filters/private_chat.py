from aiogram.dispatcher.filters import BoundFilter
from aiogram.types import Message, ChatType


class IsPrivate(BoundFilter):
    async def check(self, message: Message):
        return message.chat.type == ChatType.PRIVATE



