import logging
import os

IRC_HOST = 'irc.freenode.net'
IRC_NICK = 'lcawhobot'
IRC_CHANS = ('#linux.conf.au', '#taslugdev')
WHO_CHANS = ('#linux.conf.au', )

# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

BACKEND = 'IRC'  # Errbot will start in text mode (console only mode) and will answer commands from there.

BOT_DATA_DIR = os.path.join(BASE_DIR, 'data')
BOT_EXTRA_PLUGIN_DIR = os.path.join(BASE_DIR, 'plugins')

BOT_LOG_FILE = os.path.join(BASE_DIR, 'errbot.log')
BOT_LOG_LEVEL = logging.DEBUG

BOT_ADMINS = ('jerrykan!~jerrykan@whatsit.theintraweb.net', )

BOT_IDENTITY = {
    'server': IRC_HOST,
    'nickname': IRC_NICK,
}
CHATROOM_PRESENCE = IRC_CHANS
IRC_RECONNECT_ON_KICK = 180

RECORDWHO_CHANNELS = WHO_CHANS
RECORDWHO_INTERVAL = 300
RECORDWHO_DATA_DIR = os.path.join(BASE_DIR, 'who_data')
