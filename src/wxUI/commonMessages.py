# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import wx
import application

def no_data_entered():
	return wx.MessageDialog(None, _("You must provide Both user and password."), _("Information needed"), wx.ICON_ERROR).ShowModal()

def no_update_available():
	return wx.MessageDialog(None, _("Your {0} version is up to date").format(application.name,), _("Update"), style=wx.OK).ShowModal()

def remove_buffer():
	return wx.MessageDialog(None, _("Do you really want to dismiss  this buffer?"), _("Attention"), style=wx.ICON_QUESTION|wx.YES_NO).ShowModal()

def no_user_exist():
	wx.MessageDialog(None, _("This user does not exist"), _("Error"), style=wx.ICON_ERROR).ShowModal()

def show_error_code(code):
	title = ""
	message = ""
	if code == 201:
		title = _("Restricted access")
		message = _("Access to user's audio is denied by the owner. Error code {0}").format(code,)
	return wx.MessageDialog(None, message, title, style=wx.ICON_ERROR).ShowModal()

def bad_authorisation():
	return wx.MessageDialog(None, _("authorisation failed. Your configuration will be deleted. If you recently changed your password in VK, you need to reauthorize Socializer. The application will be restarted and prompt you again for your user and password. Press OK to continue."), _("Error"), style=wx.ICON_ERROR).ShowModal()

def connection_error():
	return wx.MessageDialog(None, _("Socializer could not connect to VK due to a connection issue. Be sure you have a working internet connection. The application will be closed when you press the OK button. If your internet connection is working correctly, please try to open socializer in a few minutes. If this problem persists, contact the developers to receive further assistance."), _("Connection Error"), style=wx.ICON_ERROR).ShowModal()

def no_audio_albums():
	return wx.MessageDialog(None, _("You do not have audio albums."), _("Error"), style=wx.ICON_ERROR).ShowModal()

def no_video_albums():
	return wx.MessageDialog(None, _("You do not have video albums."), _("Error"), style=wx.ICON_ERROR).ShowModal()

def delete_audio_album():
	return wx.MessageDialog(None, _("Do you really want to delete   this Album? this will be deleted from VK too."), _("Attention"), style=wx.ICON_QUESTION|wx.YES_NO).ShowModal()

def updated_status():
	return wx.MessageDialog(None, _("Your status message has been successfully updated."), _("Success")).ShowModal()

def remove_post():
	return wx.MessageDialog(None, _("Do you really want to delete this post?"), _("Attention"), style=wx.ICON_QUESTION|wx.YES_NO).ShowModal()

def join_group():
	return wx.MessageDialog(None, _("If you like socializer, you can join or community from where you can ask for help, give us your feedback and help other users of the application. New releases are posted in the group too. Would you like to join the Socializer community?"), _("Attention"), style=wx.ICON_QUESTION|wx.YES_NO).ShowModal()

def group_joined():
	return wx.MessageDialog(None, _("You have joined the Socializer community."), _("Success")).ShowModal()

def proxy_question():
	return wx.MessageDialog(None, _("If you live in a country where VK is blocked, you can use a proxy to bypass such restrictions. Socializer includes a working proxy to ensure all users can connect to VK. Do you want to use Socializer through the proxy?"), _("Attention"), style=wx.ICON_QUESTION|wx.YES_NO).ShowModal()

def remove_friend(user):
	return wx.MessageDialog(None, _("Are you sure you want to remove {user1_nom} from your friends?").format(**user), _("Attention"), style=wx.ICON_QUESTION|wx.YES_NO).ShowModal()

def post_deleted():
	return wx.MessageDialog(None, _("This post has been removed."), _("Error"), wx.ICON_ERROR).ShowModal()

def restart_program():
	return wx.MessageDialog(None, _("In order to apply the changes you requested, you must restart the program. Do you want to restart Socializer now?"), _("Attention"), style=wx.ICON_QUESTION|wx.YES_NO).ShowModal()

def community_no_items():
	return wx.MessageDialog(None, _("There are 0 items for this community."), _("Error"), wx.ICON_ERROR).ShowModal()

def delete_conversation():
	return wx.MessageDialog(None, _("do you really want to delete all messages of this conversation in VK?"), _("Attention"), style=wx.ICON_QUESTION|wx.YES_NO).ShowModal()

def block_person(person):
	return wx.MessageDialog(None, _("Are you really sure you want to block {user1_nom} from your VK account?").format(**person,), _("Attention"), style=wx.ICON_QUESTION|wx.YES_NO).ShowModal()

def unblock_person():
	return wx.MessageDialog(None, _("Are you sure you want to unblock this user?"), _("Attention"), style=wx.ICON_QUESTION|wx.YES_NO).ShowModal()

def post_failed():
	return wx.MessageDialog(None, _("Unfortunately, we could not send your last post or message to VK. Would you like to try again?"), _("Post failed"), style=wx.ICON_QUESTION|wx.YES_NO).ShowModal()

def exit():
	dlg = wx.MessageDialog(None, _("Do you really want to close Socializer?"), _("Exit"), wx.YES_NO|wx.ICON_QUESTION)
	return dlg.ShowModal()

def vk_error(code):
	title = _("VK error")
	if code == 7:
		msg = _("You are not allowed to perform this action. Please be sure you are not attempting to post or send a message to a blocked or banned user. Error code 7.")
	elif code == 900:
		msg = _("You cannot send messages to users in your blacklist.")
	else:
		msg = str(code)
	return wx.MessageDialog(None, msg, title, wx.ICON_ERROR).ShowModal()