#!/usr/bin/env python
from jabberbot.mucbot import MUCBot
import settings

jid = settings.JID
pwd = settings.PWD
muc_room = settings.MUC_ROOM
muc_nick = settings.MUC_NICK

bot = MUCBot(jid, pwd, muc_room, muc_nick)
bot.connect()
bot.process(block=True)
