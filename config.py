# Copyright (c) 2023 EDM115
import os


class Config:
    APP_ID = int(os.environ.get("1083385"))
    API_HASH = os.environ.get("65f961d8cd5ec69af786fdb7bd42cc5c")
    BOT_TOKEN = os.environ.get("6356020724:AAHYXKJwVTkJbpy0hEVjN_1QRtphkQXleTk")
    LOGS_CHANNEL = int(os.environ.get("-1001908283263"))
    MONGODB_URL = os.environ.get("mongodb+srv://lucifer:@Mantap22@cluster0.qsev9ei.mongodb.net/?retryWrites=true&w=majority")
    BOT_OWNER = int(os.environ.get("1007538121"))
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/Downloaded"
    THUMB_LOCATION = f"{os.path.dirname(__file__)}/Thumbnails"
    TG_MAX_SIZE = 2097152000
    # Default chunk size (0.005 MB → 1024*6) Increase if you need faster downloads
    CHUNK_SIZE = 1024 * 1024 * 5  # 5 MB
    BOT_THUMB = f"{os.path.dirname(__file__)}/bot_thumb.jpg"
    MAX_CONCURRENT_TASKS = 50
    MAX_TASK_DURATION_EXTRACT = 45 * 60  # 45 minutes (in seconds)
    MAX_TASK_DURATION_MERGE = 90 * 60  # 1 hour 30 minutes (in seconds)
