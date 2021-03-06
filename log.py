# coding=utf-8
# author: Lan_zhijiang
# description: Log class
# date: 2020/10/2

import json
import time
import datetime
import os
import sys


class Log:

    def __init__(self):

        self.logLevelList = [
            "DEBUG", "INFO", "WARNING", "ERROR", "FATAL"
        ]
        self.log_setting = json.load(open("./data/json/log_setting.json", "r", encoding="utf-8"))

    def get_log_file_path(self):

        """
        获取log文件路径
        :return:
        """
        basic_path = self.log_setting["logPath"]
        log_file_name = self.get_date() + ".log"
        if os.path.exists(basic_path + log_file_name) is False:
            create_log_file = open(basic_path + log_file_name, "w")
            create_log_file.close()
        else:
            pass
        return basic_path + log_file_name

    def get_time_stamp(self):

        """
        获取当前时间戳，整数化字符化
        :return:
        """
        return str(int(time.time()))

    def get_date(self):

        """
        获取当前日期
        :return:
        """
        return str(datetime.date.today())

    def get_formatted_time(self):

        """
        获取格式化的时间
        :return:
        """
        return time.strftime("%H:%M:%S")

    def add_log(self, content, level, is_print=True, is_period=True):

        """
        添加log
        :param level: log级别  0: DEBUG 1: INFO 2: WARNING 3: ERROR(当前任务可能停止) 4: FATAL: 主线程退出
        :param content: log内容
        :param is_print: 是否打印
        :param is_period: 是否添加句号
        :return:
        """
        log = "[" + self.logLevelList[level] + "] " + self.get_formatted_time() + " " + content

        if is_period:
            log = log + " ."
        if is_print:
            if level >= self.log_setting["displayLevel"]:
                print(log)

        try:
            log_file = open(self.get_log_file_path(), "a")
            log_file.write(log + '\r\n')
            log_file.close()
        except IOError:
            print(
                "[WARNING] %s Can't write into the log file, please check the permission or is the path correct!" % self.get_formatted_time())
        else:
            if level > 3:
                sys.exit()
            return 0
