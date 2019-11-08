import os
#
# import yaml
from ruamel import yaml


def get_yaml():
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data',
                        'yamls', 'page_data.yaml')
    test_data_file = os.path.abspath(path)
    file = open(test_data_file, 'r', encoding='utf-8')
    data_yaml = yaml.load(file, Loader=yaml.RoundTripLoader)
    return data_yaml
