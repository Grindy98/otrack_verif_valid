import pickle
import os

_state_dict = None

def load_from_save(filename):
    global _state_dict
    try:
        with open(filename, 'rb') as infile:
            _state_dict = pickle.load(infile)
    except EOFError as eof:
        _state_dict = {}
    except FileNotFoundError as fnf:
        _state_dict = {}

def dump_to_save(filename):
    global _state_dict
    with open(filename, 'wb') as outfile:
        pickle.dump(_state_dict, outfile)

def get_class_list(cls : type):
    global _state_dict
    # TODO: state dict structure is a dict of lists of classes having the same type
    if cls not in _state_dict:
        _state_dict[cls] = []
    return _state_dict[cls]