#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
part_CRE_Cnr.py - The core part of epub3.

Author: Matt Belfast Brown
E-mail: thedayofthedo@gmail.com
Create Date: 2022-02-23
Version Date: 2022-02-28
Version: 0.0.1

Copyright (C) 2022 Matt Belfast Brown
LICENSE　MIT LICENSE
"""

import epub3.include as include


def fun_mkco_fxml(vari_fipt):
    include.fun_make_ndir(vari_fipt + include.path_meta)
    vari_pcon = vari_fipt + include.path_meta + "\\container.xml"
    head_xmlf = '<?xml version="1.0" encoding="utf-8"?>\n'
    xmlf_cont = '<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">\n	<rootfiles> \n		<rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>\n   </rootfiles>\n</container> '
    with open(vari_pcon, 'w+', encoding='utf-8') as cont_fxml:
        cont_fxml.write(head_xmlf)
        cont_fxml.write(xmlf_cont)
