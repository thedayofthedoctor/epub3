#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
part_CON_Opf.py - The core part of epub3.

Author: Matt Belfast Brown
E-mail: thedayofthedo@gmail.com
Create Date: 2022-02-23
Version Date: 2022-02-28
Version: 0.0.1

Copyright (C) 2022 Matt Belfast Brown
LICENSE　MIT LICENSE
"""

import time
import uuid


def fun_mkco_topf(vari_titl: str, vari_lang: str, vari_ctor: str) -> list:
	vari_pubd = uuid.uuid1()
	vari_rlti = time.localtime(time.time())
	vari_modi = time.strftime('%y-%M-%DT%H:%m:%s', vari_rlti)
	cons_titl = '<dc:title>' + vari_titl + '</dc:title>\n'
	cons_lang = '<dc:language>' + vari_lang + '</dc:language>\n'
	cons_ctor = '<dc:creator>' + vari_ctor + '</dc:creator>\n'
	'''
	<dc:publisher>PUBLISHER</dc:publisher>
	<dc:description></dc:description>
	<dc:coverage></dc:coverage>
	<dc:source></dc:source>
	<dc:date></dc:date>
	<dc:rights></dc:rights>
	<dc:subject></dc:subject>
	<dc:contributor></dc:contributor>
	<dc:type></dc:type>
	<dc:format></dc:format>
	<dc:relation></dc:relation>
	<dc:builder></dc:builder>
	'''


cons_blan = "    "
