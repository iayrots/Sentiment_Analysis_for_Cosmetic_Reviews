import pickle
import re
from konlpy.tag import Twitter
twitter = Twitter()

def write_data(filename, s):
    with open(filename, 'w') as f:
        f.write(s)


def read_data_tab(filename):
    with open(filename, 'r') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:]
    return data


def read_data(filename):
    with open(filename, 'r') as f:
        data = [line.split(', ') for line in f.read().splitlines()]
        data = data[1:]
    return data


def save_pickle(file_name, obj):
    with open(file_name, 'wb') as f:
        pickle.dump(obj, f)


def load_pickle(file_name):
    with open(file_name, 'rb') as f:
        obj = pickle.load(f)
    return obj


def tokenize(doc):
    """
    Tokenize document with tokens/POS tags pairs.
    :param doc: Document to tokenize
    :return: token/POS tags paired document
    For iterable documents, they should be in iteration.
    """
    return ['/'.join(t) for t in twitter.pos(doc, norm=True, stem=True)]


def remove_pos(docs):
    """
    Remove POS tagging from token/POS.
    :param docs: Document to remove POS tags
    :return: Document with removed POS. Same result as tokenizing.
    """
    p = '/([a-zA-Z]+)[+]*([a-zA-Z]*)'
    pos_removed = []
    for s in docs:
        result = re.sub(p, '', s)
        pos_removed.append(result)
    return pos_removed
