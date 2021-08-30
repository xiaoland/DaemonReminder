# author: Lan_zhijiang
# description: User Interface class
# date: 2021/08/26

import wx


class DaemonReminderUi(wx.Frame):

    def __init__(self, parent, base, main):

        self.base = base
        self.main = main
        self.log = base.log
        self.setting = base.setting

        self.log.add_log("DaemonReminderUi: start load ui", 1)
        self.width, self.height = self.setting["windows"]["width"], self.setting["windows"]["height"]
        size = wx.Size(width=self.width, height=self.height)
        wx.Frame.__init__(self, parent, -1, title="👿恶魔提醒器 | By Lan_zhijiang", size=size)
        # self.scroller = wx.ScrolledWindow(self, -1)
        # self.scroller.SetScrollbars(1, 1, self.width, self.height)

        self.editor_panel = wx.Panel(self)
        self.remind_list_panel = wx.Panel(self)

        self.load_main_page()

    def load_main_page(self):

        """
        加载主页
        :return:
        """
        self.log.add_log("DaemonReminderUi: start load main page-EditorPanel", 1)
        # load editor_panel
        # set basic
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        fgs1 = wx.FlexGridSizer(10, 2, 900, 300)
        fgs2 = wx.FlexGridSizer(1, 3, 50, 300)

        # set edit blanks
        name_t, tc_name = wx.StaticText(self.editor_panel, label="提醒名称"), wx.TextCtrl(self.editor_panel)
        desc_t, tc_desc = wx.StaticText(self.editor_panel, label="描述"), wx.TextCtrl(self.editor_panel)
        speech_t, tc_speech = wx.StaticText(self.editor_panel, label="自定义提醒句"), wx.TextCtrl(self.editor_panel)
        status_t, tc_status = wx.StaticText(self.editor_panel, label="开启/关闭(1/0)"), wx.TextCtrl(self.editor_panel)
        repeat_t, tc_repaet = wx.StaticText(self.editor_panel, label="重复(1,2,...)"), wx.TextCtrl(self.editor_panel)
        time_t, tc_time = wx.StaticText(self.editor_panel, label="提醒时间(hh-mm)"), wx.TextCtrl(self.editor_panel)
        date_t, tc_date = wx.StaticText(self.editor_panel, label="提醒日期(blank/yyyy-MM-DD)"), wx.TextCtrl(self.editor_panel)
        ringtone_t, tc_ringtone = wx.StaticText(self.editor_panel, label="提醒铃声(default/path)"), wx.TextCtrl(self.editor_panel)
        level_t, tc_level = wx.StaticText(self.editor_panel, label="提醒级别(0/1"), wx.TextCtrl(self.editor_panel)
        image_t, tc_image = wx.StaticText(self.editor_panel, label="恶魔图片列表(path,path)"), wx.TextCtrl(self.editor_panel)

        fgs1.AddMany([
            (name_t), (tc_name, 1, wx.EXPAND), (desc_t), (tc_desc, 1, wx.EXPAND), (speech_t), (tc_speech, 1, wx.EXPAND),
            (status_t), (tc_status, 1, wx.EXPAND), (repeat_t), (tc_repaet, 1, wx.EXPAND), (time_t), (tc_time, 1, wx.EXPAND),
            (date_t), (tc_date, 1, wx.EXPAND), (ringtone_t), (tc_ringtone, 1, wx.EXPAND), (level_t), (tc_level, 1, wx.EXPAND),
            (image_t), (tc_image, 1, wx.EXPAND),
        ])
        fgs1.AddGrowableRow(2, 1)
        fgs1.AddGrowableCol(1, 1)
        hbox.Add(fgs1, 2, flag= wx.ALL|wx.EXPAND)
        self.editor_panel.SetSizer(hbox)
        # set button
        set_remind_bitmap = wx.Image('./data/bitmap/set.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        update_remind_bitmap = wx.Image('./data/bitmap/update.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        remove_remind_bitmap = wx.Image('./data/bitmap/remove.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        set_remind_button = wx.BitmapButton(self.editor_panel, -1, set_remind_bitmap)
        update_remind_button = wx.BitmapButton(self.editor_panel, -1, update_remind_bitmap)
        remove_remind_button = wx.BitmapButton(self.editor_panel, -1, remove_remind_bitmap)
        self.Bind(wx.EVT_BUTTON, self.set_remind, set_remind_button)
        self.Bind(wx.EVT_BUTTON, self.update_remind, update_remind_button)
        self.Bind(wx.EVT_BUTTON, self.remove_remind, remove_remind_button)

        fgs2.AddMany([(set_remind_button), (update_remind_button), (remove_remind_button)])
        hbox.Add(fgs2, 2, flag= wx.ALL|wx.EXPAND)

    def set_remind(self):
        pass

    def update_remind(self):
        pass

    def remove_remind(self):
        pass


class DaemonReminderApp(wx.App):

    def __init__(self, base, main, redirect=False, filename=None, useBestVisual=False, clearSigInt=True):
        self.base = base
        self.main = main
        wx.App.__init__(self, redirect, filename, useBestVisual, clearSigInt)

    def OnInit(self):

        self.frame = DaemonReminderUi(None, self.base, self.main)
        self.frame.Show(True)
        self.SetTopWindow(self.frame)
        return True

