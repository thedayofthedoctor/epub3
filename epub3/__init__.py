#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__init__.py - The core part of epub3.

Author: Matt Belfast Brown
E-mail: thedayofthedo@gmail.com
Create Date: 2022-02-23
Version Date: 2022-02-24
Version: 0.0.1

Copyright (C) 2022 Matt Belfast Brown
LICENSE　MIT LICENSE
"""

# import list
import epub3.include as include
import epub3.content.part_CRE_Cnr as part_CRE_Cnr

__title__ = 'epub3'
__version__ = '0.0.1'
__author__ = 'Matt Belfast Brown'
__license__ = 'MIT LIENSE'
__copyright__ = 'Copyright (C) 2022 Matt Belfast Brown'
__all__ = ['content', 'media', 'OCF', 'packages', 'include', 'part_CRE_Cnr']

# define function list
fun_make_ndir = include.fun_make_ndir
fun_mkob_path = include.fun_mkob_path
fun_obta_path = include.fun_obta_path
fun_pppa_rati = include.fun_pppa_rati

fun_mkco_fxml = part_CRE_Cnr.fun_mkco_fxml
