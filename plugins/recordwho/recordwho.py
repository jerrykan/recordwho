import json
import os
from time import time

from errbot import BotPlugin, botcmd, arg_botcmd, webhook


class Recordwho(BotPlugin):
    """
    Regularly record the WHO details of users in a channel
    """
    def __init__(self, bot):
        super().__init__(bot)
        self._who_list = {}
        self._bot.conn.reactor.add_global_handler('whoreply', self.do_whoreply)
        self._bot.conn.reactor.add_global_handler('endofwho', self.do_endofwho)

    def do_whoreply(self, connection, event):
        self._who_list[event.arguments[0]].append(event.arguments)

    def do_endofwho(self, connection, event):
        try:
            os.mkdir(self._bot.bot_config.RECORDWHO_DATA_DIR)
        except FileExistsError:
            pass

        chan = event.arguments[0]
        fname = os.path.join(self._bot.bot_config.RECORDWHO_DATA_DIR,
                             '{}_{}.json'.format(chan, int(time())))

        with open(fname, 'w') as fh:
            json.dump(self._who_list[chan], fh)

    def activate(self):
        super().activate()
        self.start_poller(self._bot.bot_config.RECORDWHO_INTERVAL,
                          self.send_msg)

    def send_msg(self):
        for chan in self._bot.bot_config.RECORDWHO_CHANNELS:
            self._who_list[chan] = []
            self._bot.conn.connection.who(chan)
