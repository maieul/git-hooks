#!/usr/bin/python
# -*- coding: utf-8 -*-
"Pour exporter vers le CTAN"""

import os 

folder      ="hook-pre-commit-pkg"
original    ="pre-commit-latex"
readme      = "README"
#créer le dossier si pas encore créé
try:
    for the_file in os.listdir(folder):
        path = os.path.join(folder, the_file)
        os.remove(path)
    os.rmdir(folder)
except:
    pass

try:
    os.mkdir(folder)
except:
    pass


content = open(original,"r")
readme  = open(folder+"/"+readme,"w")
for line in content:
    if line[0] == "#":
        pass
    
    elif line[:3] == '"""':
        if line  == '"""\n':
            break
        else:
            readme.write(line[3:])
    else:
        readme.write(line)

readme.close()
content.close()


