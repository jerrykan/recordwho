import json
import os
from time import time

from errbot import BotPlugin

class RecordWho(BotPlugin):
    """
    Regularly record the WHO details of users in a channel
    """
    def __init__(self, bot, *args, **kwargs):
        self._who_list = {}
        bot.conn.reactor.add_global_handler('whoreply', self.do_whoreply)
        bot.conn.reactor.add_global_handler('endofwho', self.do_endofwho)
        super().__init__(bot, *args, **kwargs)

        try:
            os.mkdir(self._bot.bot_config.RECORDWHO_DATA_DIR)
        except FileExistsError:
            pass

    def do_whoreply(self, connection, event):
        self._who_list[event.arguments[0]].append(event.arguments)

    def do_endofwho(self, connection, event):
        # round to nearest interval
        t = int(time()) + (self.bot_config.RECORDWHO_INTERVAL // 2)
        timestamp = t - (t % self.bot_config.RECORDWHO_INTERVAL)

        chan = event.arguments[0]
        fname = os.path.join(self.bot_config.RECORDWHO_DATA_DIR,
                             '{}_{}.json'.format(chan, timestamp))

        with open(fname, 'w') as fh:
            json.dump(self._who_list[chan], fh)

    def activate(self):
        super().activate()
        self.start_poller(self.bot_config.RECORDWHO_INTERVAL, self.send_msg)

    def send_msg(self):
        for chan in self.bot_config.RECORDWHO_CHANNELS:
            self._who_list[chan] = []
            self._bot.conn.connection.who(chan)
