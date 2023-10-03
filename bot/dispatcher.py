import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from filters import IsOwnerFilter, IsAdminFilter, MemberCanRestrictFilter, IsUserFilter
import config


logging.basicConfig(level=logging.INFO)


if not config.BOT_TOKEN:
    exit("No token provided")


bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())


# activate filters
dp.filters_factory.bind(IsOwnerFilter)
dp.filters_factory.bind(IsAdminFilter)
dp.filters_factory.bind(IsUserFilter)
dp.filters_factory.bind(MemberCanRestrictFilter)
