#! /usr/bin/python

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

from collections import namedtuple
from .json_parser import load_json_instance

Instance = namedtuple('Instance', ['obj', 'constr_mat', 'constr_vec'])

def get_extension(file_name: str):
    index = file_name.find('.')
    if index != -1:
        return file_name[index + 1:]
    else:
        return None


def get_loader(ext):
    loaders = {'json': load_json_instance}
    return loaders[ext]

def load_instance(file_name):
    ext = get_extension(file_name)
    load = get_loader(ext)
    return load(file_name)
