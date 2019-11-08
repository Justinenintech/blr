# -*- coding: utf-8 -*-
import os

# import yaml
from ruamel import yaml


def update_newest_username(username):
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data',
                        'yamls', 'page_data.yaml')
    test_data_file = os.path.abspath(path)
    with open(test_data_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = yaml.load(f, Loader=yaml.RoundTripLoader)
        content['datas']['data_newest_username'] = "{}".format(username)
    with open(test_data_file, 'w', encoding='utf-8', errors='ignore') as nf:
        yaml.dump(content, nf, Dumper=yaml.RoundTripDumper, default_flow_style=False, allow_unicode=True)


def update_last_username(username):
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data',
                        'yamls', 'page_data.yaml')
    test_data_file = os.path.abspath(path)
    with open(test_data_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = yaml.load(f, Loader=yaml.RoundTripLoader)
        content['datas']['data_last_username'] = "{}".format(username)
    with open(test_data_file, 'w', encoding='utf-8', errors='ignore') as nf:
        yaml.dump(content, nf, Dumper=yaml.RoundTripDumper, default_flow_style=False, allow_unicode=True)


def update_deposit_channel_1(channel):
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data',
                        'yamls', 'page_data.yaml')
    test_data_file = os.path.abspath(path)
    with open(test_data_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = yaml.load(f, Loader=yaml.RoundTripLoader)
        content['datas']['data_zfb_channel_1'] = "{}".format(channel)
    with open(test_data_file, 'w', encoding='utf-8', errors='ignore') as nf:
        yaml.dump(content, nf, Dumper=yaml.RoundTripDumper, default_flow_style=False, allow_unicode=True)


def update_deposit_channel_2(channel):
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data',
                        'yamls', 'page_data.yaml')
    test_data_file = os.path.abspath(path)
    with open(test_data_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = yaml.load(f, Loader=yaml.RoundTripLoader)
        content['datas']['data_zfb_channel_2'] = "{}".format(channel)
    with open(test_data_file, 'w', encoding='utf-8', errors='ignore') as nf:
        yaml.dump(content, nf, Dumper=yaml.RoundTripDumper, default_flow_style=False, allow_unicode=True)


def update_zfbh5_amount(min_amount, max_amount):
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data',
                        'yamls', 'page_data.yaml')
    test_data_file = os.path.abspath(path)
    with open(test_data_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = yaml.load(f, Loader=yaml.RoundTripLoader)
        content['datas']['data_zfbh5_min_amount'] = "{}".format(min_amount)
        content['datas']['data_zfbh5_max_amount'] = "{}".format(max_amount)
    with open(test_data_file, 'w', encoding='utf-8', errors='ignore') as nf:
        yaml.dump(content, nf, Dumper=yaml.RoundTripDumper, default_flow_style=False, allow_unicode=True)

def update_bind_card(card):
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data',
                        'yamls', 'page_data.yaml')
    test_data_file = os.path.abspath(path)
    with open(test_data_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = yaml.load(f, Loader=yaml.RoundTripLoader)
        content['datas']['data_bind_card'] = "{}".format(card)
    with open(test_data_file, 'w', encoding='utf-8', errors='ignore') as nf:
        yaml.dump(content, nf, Dumper=yaml.RoundTripDumper, default_flow_style=False, allow_unicode=True)