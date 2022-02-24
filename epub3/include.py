#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
include.py - The core part of epub3.

Author: Matt Belfast Brown
E-mail: thedayofthedo@gmail.com
Create Date: 2022-02-23
Version Date: 2022-02-28
Version: 0.0.1

Copyright (C) 2022 Matt Belfast Brown
LICENSE　MIT LICENSE
"""

import os


# define variable list

def fun_make_ndir(file_path: str):
    """
    Function to create non-existent file path.
    :param file_path: The path of the file detected and created.
    Check and create path what you want.
    """
    if not os.path.exists(file_path):
        os.mkdir(file_path)


def fun_mkob_path(vari_fipt):
    fun_make_ndir(vari_fipt + path_meta)
    fun_make_ndir(vari_fipt + path_oebp)
    fun_make_ndir(vari_fipt + path_oebp)


path_meta = r"\META-INF"
path_oebp = r"\OEBPA"
path_chap = r"\OEBPA\Chapter"
