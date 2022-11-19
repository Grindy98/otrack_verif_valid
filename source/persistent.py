import pickle
import os

_state_dict = None

def load_from_save(filename):
    # TODO: check if filename exists, else empty state dict
    if not os.path.exists(filename):
        return None
    else:
        with open(filename, 'r') as infile:
            _state_dict = pickle.load(infile)

def dump_to_save(filename):
    with open(filename, 'w') as outfile:
        pickle.dump(_state_dict, outfile)

def get_class_list(cls : type):
    # TODO: state dict structure is a dict of lists of classes having the same type
    if cls not in _state_dict:
        _state_dict[cls] = []
    return _state_dict[cls]