#! /usr/bin/python

# Copyright (c) 2019 Filippo Ranza <filipporanza@gmail.com>

import json
import numpy as np


def objective_function(data):
    try:
        array = np.array(data["min"])
    except KeyError:
        array = np.array(data["max"])
        array *= -1
    return array


def parse_constr(constr):
    eq = constr["eq"]
    try:
        val = constr["ge"] * -1
        ceq = np.array(eq) * -1
    except KeyError:
        val = constr["le"]
        ceq = np.array(eq)
    return ceq, val


def constraints(data):

    constr_mat = []
    constr_val = []

    for constr in data["constrs"]:
        eq, val = parse_constr(constr)
        constr_mat.append(eq)
        constr_val.append(val)
    return np.array(constr_mat), np.array(constr_val)


def parse_data(data):
    obj = objective_function(data)
    mat, val = constraints(data)
    return obj, mat, val


def load_json_instance(file_name):
    with open(file_name) as file:
        data = json.load(file)

    return parse_data(data)
