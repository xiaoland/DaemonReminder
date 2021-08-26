# author: Lan_zhijiang
# description: The program core functions
# date: 2021/08/26


class DaemonReminderMain:

    def __init__(self, base):

        self.base = base
        self.log = base.log
        self.tts = base.tts
        self.encryption = base.encryption

        self.setting = base.setting
        self.tasks = base.tasks

    def set_remind(self, name, desc, when_t, when_d, repeat=None, ringtone="default", remind_level=1, image_list=None, remind_speech=""):

        """
        设置新的提醒
        :param name: 提醒名称
        :param desc: 提醒描述
        :param when_t: 提醒时间（hh:mm）
        :param when_d: 提醒日期（YYYY-MM-DD）
        :param repeat: 是否重复，是则应为列表形式
        :param ringtone: 设置铃声
        :param remind_level: 设置提醒级别 0-3
        :param image_list: 刺激你的图片的列表 >=2才需要
        :return: bool, str
        """

    def update_remind(self, remind_id, info):

        """
        更新提醒信息
        :param remind_id: 提醒id
        :param info: 要更新的信息的字典
        :type info: dict
        :return: bool, str
        """

    def remove_remind(self, remind_id):

        """
        删除这个提醒
        :param remind_id: 提醒id
        :return: bool, str
        """

    def start_remind(self, remind_id):

        """
        时间到了，开始提醒
        :param remind_id: 提醒id
        :return:
        """
