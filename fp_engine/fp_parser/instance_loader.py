#! /usr/bin/python


from collections import namedtuple

Instance = namedtuple('Instance', ['obj', 'constr_mat', 'constr_vec'])

def get_extension(file_name: str):
    index = file_name.find('.')
    return file_name[index:]

def load_instance(file_name):
    pass
