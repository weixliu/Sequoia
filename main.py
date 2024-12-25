# -*- encoding: UTF-8 -*-

import utils
import logging
import work_flow
import settings
import schedule
import time
import datetime
import os
from pathlib import Path


def job():
    if utils.is_weekday():
        work_flow.prepare()

if not os.path.exists('logs'):
    os.mkdir('logs')
if not os.path.exists(f"data/{datetime.datetime.now().strftime('%Y-%m-%d')}"):
    os.mkdir(f"data/{datetime.datetime.now().strftime('%Y-%m-%d')}")

logger = logging.getLogger()
# set log level
logger.setLevel(logging.INFO)

# file handler
handler = logging.FileHandler(f"logs/sequoia-{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log", mode='w', encoding='utf-8')
handler.setFormatter(logging.Formatter("%(asctime)s-%(name)s-%(levelname)s: %(message)s"))

logger.addHandler(handler)

settings.init()

if settings.config['cron']:
    EXEC_TIME = "15:15"
    schedule.every().day.at(EXEC_TIME).do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
else:
    work_flow.prepare()
