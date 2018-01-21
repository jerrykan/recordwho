import logging
import os

### RecordWho Settings ###

IRC_HOST = 'irc.freenode.net'
IRC_NICK = 'lcawhobot'
IRC_CHANS = (
    '#linux.conf.au',
)
WHO_CHANS = (
    '#linux.conf.au',
)
IRC_ADMINS = ('jerrykan!~jerrykan@whatsit.theintraweb.net', )

### Errbot Configuration ###

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

BACKEND = 'IRC'

BOT_DATA_DIR = os.path.join(BASE_DIR, 'data')
BOT_EXTRA_PLUGIN_DIR = os.path.join(BASE_DIR, 'plugins')

BOT_LOG_FILE = os.path.join(BASE_DIR, 'errbot.log')
BOT_LOG_LEVEL = logging.WARNING

BOT_ADMINS = IRC_ADMINS

BOT_IDENTITY = {
    'server': IRC_HOST,
    'nickname': IRC_NICK,
}
CHATROOM_PRESENCE = IRC_CHANS
IRC_RECONNECT_ON_KICK = 180

RECORDWHO_CHANNELS = WHO_CHANS
RECORDWHO_INTERVAL = 300
RECORDWHO_DATA_DIR = os.path.join(BASE_DIR, 'who_data')
