#! /usr/bin/python


from collections import namedtuple

Instance = namedtuple('Instance', ['obj', 'constr_mat', 'constr_vec'])

def get_extension(file_name: str):
    index = file_name.find('.')
    if index != -1:
        return file_name[index + 1:]
    else:
        return None

def load_instance(file_name):
    pass
