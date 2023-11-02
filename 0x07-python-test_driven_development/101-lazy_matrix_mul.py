#!/usr/bin/python3
"""Creat lazy_matrix_mul function"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ multiply two matrix with numpy """
    return np.dot(m_a, m_b)
