# author: Lan_zhijiang
# description: Launch program
# date: 2021/08/26

from log import Log
from tts import BaiduTts
from encryption import Encryption
from main import DaemonReminderMain
from ui import DaemonReminderUi

import json


class Base:

    def __init__(self):

        self.log = Log()
        self.tts = BaiduTts(self.log, self.setting)
        self.encryption = Encryption()

        self.setting = json.load(open("./data/json/setting.json", "r", encoding="utf-8"))
        self.tasks = json.load(open("data/json/reminds.json"))


if __name__ == "__main__":
    base = Base()
    main = DaemonReminderMain(base)

    ui = DaemonReminderUi(base, main)
    ui.start()
