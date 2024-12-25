# -*- encoding: UTF-8 -*-

import utils
import logging
import work_flow
import settings
import schedule
import time
import datetime
from pathlib import Path


def job():
    if utils.is_weekday():
        work_flow.prepare()


logger = logging.getLogger()
# set log level
logger.setLevel(logging.INFO)

# file handler
handler = logging.FileHandler('sequoia.log', mode='w', encoding='utf-8')
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
