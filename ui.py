# author: Lan_zhijiang
# description: User Interface class
# date: 2021/08/26

import wx


class DaemonReminderUi(wx.Frame):

    def __init__(self, base, main):

        self.base = base
        self.main = main
        self.log = base.log
        self.setting = base.setting

        self.log.add_log("DaemonReminderUi: start load ui", 1)
        self.width, self.height = self.setting["windows"]["width"], self.setting["windows"]["height"]
        size = wx.Size(width=self.width, height=self.height)
        wx.Frame.__init__(self, None, -1, title="👿恶魔提醒器 | By Lan_zhijiang", size=size)
        # self.scroller = wx.ScrolledWindow(self, -1)
        # self.scroller.SetScrollbars(1, 1, self.width, self.height)

        self.panel = self

        # set ui
        set_remind = wx.Image('./bitmap/reload.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        update_remind = wx.Image('./bitmap/TV-icon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        remove_remind = wx.Image('./bitmap/home-icon.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.set_remind_button = wx.BitmapButton(self.panel, -1, reload_bitmap, pos=(0, 536))
        self.update_remind_button = wx.BitmapButton(self.panel, -1, janpanese_anime_bitmap, pos=(0, 128))
        self.remove_remind_button = wx.BitmapButton(self.panel, -1, main_page_bitmap, pos=(0, 0))

        self.Bind(wx.EVT_BUTTON, self.set_remind, self.set_remind_button)
        self.Bind(wx.EVT_BUTTON, self.update_remind, self.update_remind_button)
        self.Bind(wx.EVT_BUTTON, self.remove_remind, self.remove_remind_button)

        self.load_main_page()

    def load_main_page(self):

        """
        加载主页
        :return:
        """


