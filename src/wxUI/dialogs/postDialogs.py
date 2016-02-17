# -*- coding: utf-8 -*-
import wx
import widgetUtils

class basicPost(widgetUtils.BaseDialog):
	def __init__(self, *args, **kwargs):
		super(basicPost, self).__init__(parent=None, *args, **kwargs)
		self.panel = wx.Panel(self, -1)
		self.sizer = wx.BoxSizer(wx.VERTICAL)

	def done(self):
		self.panel.SetSizer(self.sizer)
		self.SetClientSize(self.sizer.CalcMin())

	def create_post_view(self, label=_(u"Message")):
		lbl = wx.StaticText(self.panel, -1, label)
		self.post_view = wx.TextCtrl(self.panel, -1, size=(730, -1), style=wx.TE_READONLY|wx.TE_MULTILINE)
		box = wx.BoxSizer(wx.HORIZONTAL)
		box.Add(lbl, 0, wx.ALL, 5)
		box.Add(self.post_view, 0, wx.ALL, 5)
		return box

	def create_comments_list(self):
		self.comments = widgetUtils.list(self.panel, _(u"User"), _(u"Comment"), _(u"Date"), _(u"Likes"), style=wx.LC_REPORT)
		box = wx.BoxSizer(wx.HORIZONTAL)
		box.Add(self.comments.list, 0, wx.ALL, 5)
		return box

	def create_likes_box(self):
		self.likes = wx.Button(self.panel, -1, _(u"Loading data..."))
		return self.likes

	def create_shares_box(self):
		self.shares = wx.Button(self.panel, -1, _(u"Loading data..."))
		return self.shares

	def create_action_buttons(self, comment=True):
		self.like = wx.Button(self.panel, -1, _(u"Like"))
		if comment: self.comment = wx.Button(self.panel, -1, _(u"Add comment"))
		box = wx.BoxSizer(wx.HORIZONTAL)
		box.Add(self.like, 0, wx.ALL, 5)
		if comment: box.Add(self.comment, 0, wx.ALL, 5)
		return box

	def create_tools_button(self):
		self.tools = wx.Button(self.panel, -1, _(u"Actions"))

	def create_dialog_buttons(self):
		self.close = wx.Button(self.panel, wx.ID_CANCEL, _(u"Close"))
		return self.close

	def set_post(self, text):
		if hasattr(self, "post_view"):
			self.post_view.ChangeValue(text)
		else:
			return False

	def insert_comments(self, comments):
		for i in comments:
			self.comments.insert_item(False, *i)

	def set_likes(self, likes):
		if hasattr(self, "likes"):
			self.likes.SetLabel(_(u"{0} people like this").format(likes,))
		else:
			return False

	def set_shares(self, shares):
		if hasattr(self, "shares"):
			self.shares.SetLabel(_(u"Shared {0} times").format(shares,))
		else:
			return False

class post(basicPost):
	def __init__(self, *args, **kwargs):
		super(post, self).__init__(*args, **kwargs)
		post_view_box = self.create_post_view()
		self.sizer.Add(post_view_box, 0, wx.ALL, 5)
		self.create_tools_button()
		self.sizer.Add(self.tools, 0, wx.ALL, 5)
		likes_box = self.create_likes_box()
		self.sizer.Add(likes_box, 0, wx.ALL, 5)
		shares_box = self.create_shares_box()
		self.sizer.Add(shares_box, 0, wx.ALL, 5)
		actions_box = self.create_action_buttons()
		self.sizer.Add(actions_box, 0, wx.ALL, 5)
		comments_box = self.create_comments_list()
		self.sizer.Add(comments_box, 0, wx.ALL, 5)
		self.sizer.Add(self.create_dialog_buttons())
		self.done()

class comment(basicPost):
	def __init__(self, *args, **kwargs):
		super(comment, self).__init__(*args, **kwargs)
		post_view_box = self.create_post_view()
		self.sizer.Add(post_view_box, 0, wx.ALL, 5)
		self.create_tools_button()
		self.sizer.Add(self.tools, 0, wx.ALL, 5)
		likes_box = self.create_likes_box()
		self.sizer.Add(likes_box, 0, wx.ALL, 5)
		actions_box = self.create_action_buttons(comment=False)
		self.sizer.Add(actions_box, 0, wx.ALL, 5)
		self.sizer.Add(self.create_dialog_buttons())
		self.done()

class audio(widgetUtils.BaseDialog):
	def __init__(self, *args, **kwargs):
		super(audio, self).__init__(parent=None, *args, **kwargs)
		panel = wx.Panel(self)
		sizer = wx.BoxSizer(wx.VERTICAL)
		lbl_title = wx.StaticText(panel, wx.NewId(), _(u"Title"))
		self.title = wx.TextCtrl(panel, wx.NewId(), size=(413, -1), style=wx.TE_READONLY|wx.TE_MULTILINE)
		titleBox = wx.BoxSizer(wx.HORIZONTAL)
		titleBox.Add(lbl_title, 0, wx.ALL, 5)
		titleBox.Add(self.title, 0, wx.ALL, 5)
		sizer.Add(titleBox, 0, wx.ALL, 5)
		lbl_artist = wx.StaticText(panel, wx.NewId(), _(u"Artist"))
		self.artist = wx.TextCtrl(panel, wx.NewId(), size=(413, -1), style=wx.TE_READONLY|wx.TE_MULTILINE)
		artistBox = wx.BoxSizer(wx.HORIZONTAL)
		artistBox.Add(lbl_artist, 0, wx.ALL, 5)
		artistBox.Add(self.artist, 0, wx.ALL, 5)
		sizer.Add(artistBox, 0, wx.ALL, 5)
		lbl_duration = wx.StaticText(panel, wx.NewId(), _(u"Duration"))
		self.duration = wx.TextCtrl(panel, wx.NewId(), size=(413, -1), style=wx.TE_READONLY|wx.TE_MULTILINE)
		durationBox = wx.BoxSizer(wx.HORIZONTAL)
		durationBox.Add(lbl_duration, 0, wx.ALL, 5)
		durationBox.Add(self.duration, 0, wx.ALL, 5)
		sizer.Add(durationBox, 0, wx.ALL, 5)
		lbl_lyrics = wx.StaticText(panel, wx.NewId(), _(u"Lyric"))
		self.lyric = wx.TextCtrl(panel, wx.NewId(), size=(500, 500), style=wx.TE_READONLY|wx.TE_MULTILINE)
		lbox = wx.BoxSizer(wx.HORIZONTAL)
		lbox.Add(lbl_lyrics, 0, wx.ALL, 5)
		lbox.Add(self.lyric, 0, wx.ALL, 5)
		sizer.Add(lbox, 0, wx.ALL, 5)
		self.play = wx.Button(panel, wx.NewId(), _(u"Play"))
		self.download = wx.Button(panel, wx.NewId(), _(u"Download"))
		close = wx.Button(panel, wx.ID_CANCEL)
		bbox = wx.BoxSizer(wx.HORIZONTAL)
		bbox.Add(self.play, 0, wx.ALL, 5)
		bbox.Add(self.download, 0, wx.ALL, 5)
		bbox.Add(close, 0, wx.ALL, 5)

	def get_destination_path(self, filename):
		saveFileDialog = wx.FileDialog(self, _(u"Save this file"), "", filename, _(u"Audio Files(*.mp3)|*.mp3"), wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
		if saveFileDialog.ShowModal() == wx.ID_OK:
			return saveFileDialog.GetPath()
		saveFileDialog.Destroy()

class friendship(widgetUtils.BaseDialog):
	def __init__(self):
		super(friendship, self).__init__(parent=None)
		panel = wx.Panel(self)
		sizer = wx.BoxSizer(wx.VERTICAL)
		self.friends = widgetUtils.list(panel, [_(u"Friend")], style=wx.LC_REPORT)
		sizer.Add(self.friends.list, 0, wx.ALL, 5)
		close = wx.Button(panel, wx.ID_CANCEL)
		btnbox = wx.BoxSizer(wx.HORIZONTAL)
		btnbox.Add(close, 0, wx.ALL, 5)
		sizer.Add(btnbox, 0, wx.ALL, 5)
		panel.SetSizer(sizer)
		self.SetClientSize(sizer.CalcMin())