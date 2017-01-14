#!/usr/bin/env python3

import json
import os
from glob import glob
from pprint import pprint

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
WHO_DATA_DIR = os.path.join(BASE_DIR, 'who_data')
HTML_DATA_DIR = os.path.join(BASE_DIR, 'html', 'data')

CHANNEL = '#linux.conf.au'
CHANNELS = (
    '#linux.conf.au',
    '#lca2017_plenary', '#lca2017_tasman_a', '#lca2017_tasman_bc',
    '#lca2017_boardwalk', '#lca2017_wellington_1', '#lca2017_wellington_2',
)
BOT_NICK = 'lcawhobot'

def parse_who_file(filename):
    matrix_users = set()
    slack_users = set()
    irc_users = set()

    with open(filename) as f:
        data = json.load(f)

    for entry in data:
        try:
            chan, user, host, server, nick, flags, hopcount_realname = entry
            hopcount, realname = hopcount_realname.split(' ', maxsplit=1)
        except ValueError:
            print('Error: Invalid entry')
            pprint(entry)
            continue

        if nick == BOT_NICK:
            continue

        if '/matrix.org/' in host:
            if '[m]' in nick:
                nick = nick.split('[m]')[0]

            if realname.startswith('@_slack_lca2017'):
                slack_users.add(nick.lower())
            else:
                matrix_users.add(nick.lower())
        else:
            irc_users.add(nick.lower())

    return {
        'irc': len(irc_users),
        'matrix': len(matrix_users),
        'slack': len(slack_users),
        'dups_irc_matrix': len(irc_users & matrix_users),
        'dups_irc_slack': len(irc_users & slack_users),
        'dups_matrix_slack': len(matrix_users & slack_users),
        'dups_irc_matrix_slack': len(irc_users & matrix_users & slack_users),
        'total_no_dups': len(irc_users | matrix_users | slack_users),
    }


who_data = {}

for channel in CHANNELS:
    who_data[channel] = {}
    filesglob = '{}_*.json'.format(channel)

    for filepath in glob(os.path.join(WHO_DATA_DIR, filesglob)):
        filename = os.path.basename(filepath)

        try:
            timestamp = int(filename.rsplit('_', maxsplit=1)[1].split('.')[0])
        except (IndexError, ValueError):
            print("Skipping file: '{}'".format(filename))
            continue

        who_data[channel][timestamp] = parse_who_file(filepath)

legend = (
    ('IRC', lambda x: x['irc'] - x['dups_irc_matrix']),
    ('IRC/Matrix', lambda x: x['dups_irc_matrix']),
    ('Matrix', lambda x:
        x['matrix'] - x['dups_irc_matrix'] - x['dups_matrix_slack']),
    ('Matrix/Slack', lambda x: x['dups_matrix_slack']),
    ('Slack', lambda x: x['slack']),
)

for channel in CHANNELS:
    d3_data = []
    d3_file = '{}.json'.format(channel.replace('#', '').replace('.', '-'))

    for name, func in legend:
        data_points = []
        for timestamp, values in sorted(who_data[channel].items()):
            data_points.append([timestamp, func(values)])

        d3_data.append({'key': name, 'values': data_points})

    with open(os.path.join(HTML_DATA_DIR, d3_file), 'w') as fh:
        json.dump(d3_data, fh)
