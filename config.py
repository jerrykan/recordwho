import logging
import os

IRC_HOST = 'irc.freenode.net'
IRC_NICK = 'lcawhobot'
IRC_CHANS = (
    '#taslugdev',
    '#linux.conf.au',
    '#lca2017_plenary', '#lca2017_tasman_a', '#lca2017_tasman_bc',
    '#lca2017_boardwalk', '#lca2017_wellington_1', '#lca2017_wellington_2',
)
WHO_CHANS = (
    '#linux.conf.au',
    '#lca2017_plenary', '#lca2017_tasman_a', '#lca2017_tasman_bc',
    '#lca2017_boardwalk', '#lca2017_wellington_1', '#lca2017_wellington_2',
)

# This is a minimal configuration to get you started with the Text mode.
# If you want to connect Errbot to chat services, checkout
# the options in the more complete config-template.py from here:
# https://raw.githubusercontent.com/errbotio/errbot/master/errbot/config-template.py

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

BACKEND = 'IRC'  # Errbot will start in text mode (console only mode) and will answer commands from there.

BOT_DATA_DIR = os.path.join(BASE_DIR, 'data')
BOT_EXTRA_PLUGIN_DIR = os.path.join(BASE_DIR, 'plugins')

BOT_LOG_FILE = os.path.join(BASE_DIR, 'errbot.log')
BOT_LOG_LEVEL = logging.WARNING

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
