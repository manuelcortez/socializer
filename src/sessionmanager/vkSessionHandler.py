#!/usr/bin/python
import keys
from vk import API, AuthSession, Session

class vkObject(object):

	def __init__(self):
		self.api_key = keys.keyring.get_api_key()
		self.api_version = 5.45

	def login(self, user, password):
		s = AuthSession(app_id=self.api_key, user_login=user, user_password=password, scope="wall, notify, friends, photos, audio, video, docs, notes, pages, status, groups, messages, notifications, stats")
		self.client = API(s, v=self.api_version)
		self.client.account.getProfileInfo()

	def login_access_token(self, token):
		s = Session(access_token=token)
		self.client = API(s, v=self.api_version)
		return self.client.account.getProfileInfo()