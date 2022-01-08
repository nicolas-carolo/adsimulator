import os
import pickle
import json
from adsimulator.templates.default_values import DEFAULT_VALUES


def get_data_path():
    return os.path.expanduser("~") + "/.adsimulator/data/"


def get_names_pool():
    with open(get_data_path() + 'first.pkl', 'rb') as f:
        return pickle.load(f)
        


def get_surnames_pool():
    with open(get_data_path() + 'last.pkl', 'rb') as f:
        return pickle.load(f)


def get_domains_pool():
    with open(get_data_path() + 'domain.pkl', 'rb') as f:
        return pickle.load(f)


def get_parameters_from_json(json_path):
    try:
        with open(json_path, 'rb') as f:
            return json.load(f)
    except FileNotFoundError:
        return DEFAULT_VALUES