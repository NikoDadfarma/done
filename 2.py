# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 11:44:29 2023

@author: Lenovo
"""
import re
print(re.sub(r"(\w)([A-Z])", r"\1 \2", "WordWordWord"))