# Copyright (c) 2023 EDM115
import logging
import time

from pyrogram import Client
from pyromod import listen  # skipcq: PY-W2000

from config import Config

boottime = time.time()

plugins = dict(root="unzipper/modules")
unzipperbot = Client(
    "UnzipperBot",
    bot_token=Config.BOT_TOKEN,
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    plugins=plugins,
    sleep_threshold=10,
    max_concurrent_transmissions=3,
)

logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.FileHandler("unzip-log.txt"), logging.StreamHandler()],
    format="%(asctime)s - %(levelname)s - %(name)s - %(threadName)s - %(message)s",
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARN)
logging.getLogger("motor").setLevel(logging.INFO)
logging.getLogger("aiohttp").setLevel(logging.INFO)
