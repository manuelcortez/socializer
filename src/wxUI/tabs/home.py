# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import wx
import widgetUtils
from pubsub import pub

class homeTab(wx.Panel):

	def create_list(self):
		self.lbl = wx.StaticText(self, wx.NewId(), _("Po&sts"))
		self.list = widgetUtils.list(self, *[_("User"), _("Text"), _("Date")], style=wx.LC_REPORT, name=_("Posts"))
		self.list.set_windows_size(0, 200)
		self.list.set_windows_size(1, 300)
		self.list.set_windows_size(2, 250)
		self.list.set_size()
		self.list.list.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnKeyDown)

	def create_post_buttons(self):
		self.postBox = wx.StaticBoxSizer(parent=self, orient=wx.HORIZONTAL, label=_("Actions"))
		self.post = wx.Button(self.postBox.GetStaticBox(), wx.NewId(), _("&Post"))
		self.postBox.Add(self.post, 0, wx.ALL, 5)

	def __init__(self, parent):
		super(homeTab, self).__init__(parent=parent)
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.create_list()
		self.create_post_buttons()
		sizer.Add(self.postBox, 0, wx.ALL, 5)
		sizer.Add(self.lbl, 0, wx.ALL, 5)
		sizer.Add(self.list.list, 1, wx.EXPAND, 5)
		self.SetSizer(sizer)
		self.SetClientSize(sizer.CalcMin())

	def OnKeyDown(self, ev=None):
		pub.sendMessage("show-current-status", buffer=self.name)
		ev.Skip()

	def showMenu(self, ev):
		if self.list.get_count() == 0: return
		pub.sendMessage("show-menu", position=ev.GetPosition())

	def showMenuByKey(self, ev):
		if self.list.get_count() == 0: return
		if ev.GetKeyCode() == wx.WXK_WINDOWS_MENU:
			pub.sendMessage("show-menu", position=self.results.list.GetPosition())

	def set_focus_function(self, focus_function):
		self.list.list.Bind(wx.EVT_LIST_ITEM_FOCUSED, focus_function)

class feedTab(homeTab):
	def __init__(self, parent):
		super(feedTab, self).__init__(parent=parent)
		self.name = "me_feed"

class communityTab(feedTab):

	def create_post_buttons(self):
		self.postBox = wx.StaticBoxSizer(parent=self, orient=wx.HORIZONTAL, label=_("Actions"))
		self.load = wx.Button(self.postBox.GetStaticBox(), wx.NewId(), _("Load buffer"))
		self.post = wx.Button(self.postBox.GetStaticBox(), -1, _("&Post in group"))
		self.postBox.Add(self.load, 0, wx.ALL, 5)
		self.postBox.Add(self.post, 0, wx.ALL, 5)

class audioTab(homeTab):
	def create_list(self):
		self.lbl = wx.StaticText(self, wx.NewId(), _("Mu&sic"))
		self.list = widgetUtils.multiselectionList(self, *[_("Title"), _("Artist"), _("Duration")], style=wx.LC_REPORT, name=_("Music"))
		self.list.set_windows_size(0, 160)
		self.list.set_windows_size(1, 380)
		self.list.set_windows_size(2, 80)
		self.list.set_size()
		self.list.list.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnKeyDown)

	def create_post_buttons(self):
		self.postBox = wx.StaticBoxSizer(parent=self, orient=wx.HORIZONTAL, label=_("Actions"))
		self.post = wx.Button(self.postBox.GetStaticBox(), -1, _("&Upload audio"))
		self.post.Enable(False)
		self.play = wx.Button(self.postBox.GetStaticBox(), -1, _("P&lay"))
		self.play_all = wx.Button(self.postBox.GetStaticBox(), -1, _("Play &All"))
		self.postBox.Add(self.post, 0, wx.ALL, 5)
		self.postBox.Add(self.play, 0, wx.ALL, 5)
		self.postBox.Add(self.play_all, 0, wx.ALL, 5)

	def get_file_to_upload(self):
		openFileDialog = wx.FileDialog(self, _("Select the audio file to be uploaded"), "", "", _("Audio files (*.mp3)|*.mp3"), wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
		if openFileDialog.ShowModal() == wx.ID_CANCEL:
			return None
		return openFileDialog.GetPath()

	def get_download_path(self, filename="", multiple=False):
		if multiple == False:
			d = wx.FileDialog(self, _("Save this file"), "", filename, _("Audio Files(*.mp3)|*.mp3"), wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
		else:
			d = wx.DirDialog(None, _("Select a folder to save all files"))
		if d.ShowModal() == wx.ID_OK:
			return d.GetPath()
		d.Destroy()

class audioAlbumTab(audioTab):

	def create_post_buttons(self):
		self.postBox = wx.StaticBoxSizer(parent=self, orient=wx.HORIZONTAL, label=_("Actions"))
		self.load = wx.Button(self.postBox.GetStaticBox(), wx.NewId(), _("Load buffer"))
		self.post = wx.Button(self.postBox.GetStaticBox(), -1, _("&Post"))
		self.play = wx.Button(self.postBox.GetStaticBox(), -1, _("P&lay"))
		self.play_all = wx.Button(self.postBox.GetStaticBox(), -1, _("Play &All"))
		self.postBox.Add(self.load, 0, wx.ALL, 5)
		self.postBox.Add(self.post, 0, wx.ALL, 5)
		self.postBox.Add(self.play, 0, wx.ALL, 5)
		self.postBox.Add(self.play_all, 0, wx.ALL, 5)

class notificationTab(homeTab):
	def __init__(self, parent):
		super(notificationTab, self).__init__(parent=parent)
		self.name = "notifications"

	def OnKeyDown(self, ev=None):
		pub.sendMessage("show-notification", buffer=self.name)
		ev.Skip()

	def create_list(self):
		self.lbl = wx.StaticText(self, wx.NewId(), _("Po&sts"))
		self.list = widgetUtils.list(self, *[_("Notification"), _("Date")], style=wx.LC_REPORT)
		self.list.set_windows_size(0, 190)
		self.list.list.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnKeyDown)

class albumTab(homeTab):
	def __init__(self, parent):
		super(albumTab, self).__init__(parent=parent)
		self.name = "albums"

	def OnKeyDown(self, ev=None):
		pub.sendMessage("show-album", buffer=self.name)
		ev.Skip()

	def create_list(self):
		self.list = widgetUtils.list(self, *[_("User"), _("Name"), _("Description"), _("Photos"), _("Created at")], style=wx.LC_REPORT)
		self.list.set_windows_size(0, 190)
		self.list.set_windows_size(1, 320)
		self.list.set_windows_size(2, 513)
		self.list.set_windows_size(3, 390)
		self.list.set_windows_size(4, 180)
		self.list.list.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnKeyDown)

class friendsTab(homeTab):
	def OnKeyDown(self, ev=None):
		pub.sendMessage("show-album", buffer=self.name)
		ev.Skip()

	def create_list(self):
		self.list = widgetUtils.list(self, *[_("Name")], style=wx.LC_REPORT)
		self.list.set_windows_size(0, 400)
		self.list.list.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnKeyDown)

class topicTab(homeTab):
	def create_list(self):
		self.lbl = wx.StaticText(self, wx.NewId(), _("Topics"))
		self.list = widgetUtils.list(self, *[_("User"), _("Title"), _("Posts"), _("Last")], style=wx.LC_REPORT)
		self.list.set_windows_size(0, 200)
		self.list.set_windows_size(1, 64)
		self.list.set_windows_size(2, 15)
		self.list.set_windows_size(2, 250)
		self.list.set_size()
		self.list.list.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnKeyDown)

class documentCommunityTab(homeTab):
	def create_list(self):
		self.lbl = wx.StaticText(self, wx.NewId(), _("Documents"))
		self.list = widgetUtils.list(self, *[_("User"), _("Title"), _("Type"), _("Size"), _("Date")], style=wx.LC_REPORT)
		self.list.set_windows_size(0, 200)
		self.list.set_windows_size(1, 128)
		self.list.set_windows_size(2, 35)
		self.list.set_windows_size(3, 15)
		self.list.set_windows_size(4, 25)
		self.list.set_size()
		self.list.list.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnKeyDown)

	def get_download_path(self, filename):
		saveFileDialog = wx.FileDialog(self, _("Save document as"), "", filename, _("All files (*.*)|*.*"), wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
		if saveFileDialog.ShowModal() == widgetUtils.OK:
			return saveFileDialog.GetPath()

class documentTab(documentCommunityTab):
	def create_post_buttons(self):
		self.postBox = wx.StaticBoxSizer(parent=self, orient=wx.HORIZONTAL, label=_("Actions"))
		self.load = wx.Button(self.postBox.GetStaticBox(), wx.NewId(), _("Load buffer"))
		self.post = wx.Button(self.postBox.GetStaticBox(), -1, _("&Post"))
		self.postBox.Add(self.load, 0, wx.ALL, 5)
		self.postBox.Add(self.post, 0, wx.ALL, 5)

class empty(wx.Panel):
	def __init__(self, parent, name):
		super(empty, self).__init__(parent=parent, name=name)
		self.name = name
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(sizer)

class chatTab(wx.Panel):

	def insert_attachments(self, attachments):
		for i in attachments:
			self.attachments.insert_item(False, *i)

	def __init__(self, parent):
		super(chatTab, self).__init__(parent=parent)
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(self.create_controls())
		sizer.Add(self.create_attachments(), 0, wx.ALL, 5)
		sizer.Add(self.create_chat(), 0, wx.ALL, 5)
		self.attachment = wx.Button(self, wx.NewId(), _("Add"))
		sizer.Add(self.attachment, 0, wx.ALL, 5)
		self.send = wx.Button(self, -1, _("Send"))
		sizer.Add(self.send, 0, wx.ALL, 5)
		self.SetSizer(sizer)

	def create_controls(self):
		lbl1 = wx.StaticText(self, wx.NewId(), _("History"))
		self.history = wx.TextCtrl(self, wx.NewId(), style=wx.TE_READONLY|wx.TE_MULTILINE, size=(500, 300))
		selectId = wx.NewId()
		self.Bind(wx.EVT_MENU, self.onSelect, id=selectId)
		self.accel_tbl = wx.AcceleratorTable([(wx.ACCEL_CTRL, ord('A'), selectId)])
		self.SetAcceleratorTable(self.accel_tbl)
		box = wx.BoxSizer(wx.HORIZONTAL)
		box.Add(lbl1, 0, wx.ALL, 5)
		box.Add(self.history, 0, wx.ALL, 5)
		return box

	def onSelect(self, event, *args, **kwargs):
		if self.history.HasFocus():
			self.history.SelectAll()
		else:
			self.text.SelectAll()
		event.Skip()

	def create_attachments(self):
		lbl = wx.StaticText(self, -1, _("Attachments"))
		self.attachments = widgetUtils.list(self, _("Type"), _("Title"), style=wx.LC_REPORT)
		box = wx.BoxSizer(wx.HORIZONTAL)
		box.Add(lbl, 0, wx.ALL, 5)
		box.Add(self.attachments.list, 0, wx.ALL, 5)
		self.attachments.list.Enable(False)
		return box

	def create_chat(self):
		lbl2 = wx.StaticText(self, -1, _("Write a message"))
		self.text = wx.TextCtrl(self, -1, size=(400, -1), style=wx.TE_MULTILINE)
		box = wx.BoxSizer(wx.HORIZONTAL)
		box.Add(lbl2, 0, wx.ALL, 20)
		box.Add(self.text, 0, wx.ALL, 5)
		return box

	def set_focus_function(self, focus_function):
		self.history.Bind(wx.EVT_KEY_UP , focus_function)

	def add_message(self, message, reverse=False):
		old_line = self.history.GetNumberOfLines()#.count("\n")
		point = self.history.GetInsertionPoint()
		if reverse:
			wx.CallAfter(self.history.SetValue, message+"\n"+self.history.GetValue())
		else:
			wx.CallAfter(self.history.AppendText, message+"\n")
		wx.CallAfter(self.history.SetInsertionPoint, point)
		new_line = self.history.GetNumberOfLines()#.count("\n")
		return (old_line, new_line)

class peopleTab(homeTab):

	def create_list(self):
		self.lbl = wx.StaticText(self, wx.NewId(), _("Friends"))
		self.list = widgetUtils.list(self, *[_("Name"), _("Last seen")], style=wx.LC_REPORT)
		self.list.set_windows_size(0, 190)
		self.list.set_windows_size(1, 100)
		self.list.set_size()
		self.list.list.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnKeyDown)

	def create_post_buttons(self):
		self.postBox = wx.StaticBoxSizer(parent=self, orient=wx.HORIZONTAL, label=_("Actions"))
		self.post = wx.Button(self.postBox.GetStaticBox(), -1, _("&Post on user's wall"))
		self.new_chat = wx.Button(self.postBox.GetStaticBox(), wx.NewId(), _("Send message"))
		self.postBox.Add(self.post, 0, wx.ALL, 5)
		self.postBox.Add(self.new_chat, 0, wx.ALL, 5)

class videoTab(homeTab):
	def create_list(self):
		self.lbl = wx.StaticText(self, wx.NewId(), _("Video&s"))
		self.list = widgetUtils.list(self, *[_("Title"), _("Description"), _("Duration")], style=wx.LC_REPORT)
		self.list.set_windows_size(0, 160)
		self.list.set_windows_size(1, 380)
		self.list.set_windows_size(2, 80)
		self.list.set_size()
		self.list.list.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnKeyDown)

	def create_post_buttons(self):
		self.postBox = wx.StaticBoxSizer(parent=self, orient=wx.HORIZONTAL, label=_("Actions"))
		self.post = wx.Button(self.postBox.GetStaticBox(), -1, _("&Post"))
		self.play = wx.Button(self.postBox.GetStaticBox(), -1, _("P&lay"))
		self.postBox.Add(self.post, 0, wx.ALL, 5)
		self.postBox.Add(self.play, 0, wx.ALL, 5)

class videoAlbumTab(videoTab):

	def create_post_buttons(self):
		self.postBox = wx.BoxSizer(parent=self, orient=wx.HORIZONTAL, label=_("Actions"))
		self.load = wx.Button(self.postBox.GetStaticBox(), wx.NewId(), _("Load buffer"))
		self.post = wx.Button(self.postBox.GetStaticBox(), -1, _("&Post"))
		self.play = wx.Button(self.postBox.GetStaticBox(), -1, _("P&lay"))
		self.postBox.Add(self.post, 0, wx.ALL, 5)
		self.postBox.Add(self.play, 0, wx.ALL, 5)
