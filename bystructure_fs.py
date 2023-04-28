import os
import re
import argparse
import sys
from functions.build_temp_files import build_temp_files
from functions.fileseeder import fileseeder
import subprocess

root_path = os.getcwd()
fs_path = os.path.dirname(os.path.abspath(__file__))
md_path = os.path.join(root_path, 'structure.md')
his_path = os.path.join(root_path, 'historial_fs.txt')
rs_path = os.path.join(fs_path, 'functions/read_history.py')

parser = argparse.ArgumentParser()
parser.add_argument('--force', help='Ejecutar una operación forzada', action='store_true')
parser.add_argument('--show', help='Muestra toda la salida', action='store_true')
parser.add_argument('--web', help='Crea solo los archivos que se crean en web', action='store_true')
parser.add_argument('--backoffice', help='Crea solo los archivos que se crean en backoffice', action='store_true')
args = parser.parse_args()

if args.web and args.backoffice:
    args.web = False
    args.backoffice = False

sys.stdout = open(his_path, 'w')

with open(md_path, 'r') as structure:
    for linea in structure:
        page_match = re.search(r'^# \*\*(\w+)\*\*', linea)
        page_match_default = re.search(r'^# \*\*(\w+)\*\*$', linea)
        page_match_traduccion = re.search(r'^# \*\*(\w+)\*\* - ', linea)
        if page_match:
            camelName = page_match.group(1)
            ndir = 0
            if page_match_traduccion:
                kebabTraduccion = linea.split(' - ')[1]
                for char in kebabTraduccion:
                    if char == "/":
                        ndir += 1
            if args.backoffice == False:
                build_temp_files(camelName, ndir)
                if args.force:
                    if page_match_traduccion:
                        fileseeder("gpag", camelName, kebabTraduccion, True, True)
                    if page_match_default:
                        fileseeder("gpag", camelName, None, True)
                    fileseeder("land", camelName, None, True)
                if page_match_traduccion:
                    fileseeder("gpag", camelName, kebabTraduccion, False, True)
                if page_match_default:
                    fileseeder("gpag", camelName)
                fileseeder("land", camelName)
            if args.web == False:
                if args.force:
                    fileseeder("sdoc", camelName, None, True)
                fileseeder("sdoc", camelName)
        template_match = re.search(r'^# (\w+)', linea)
        template_match_default = re.search(r'^# (\w+)$', linea)
        template_match_traduccion = re.search(r'^# (\w+) - ', linea)
        if template_match:
            camelName = template_match.group(1)
            if template_match_traduccion:
                kebabTraduccion = linea.split(' - ')[1]
            if args.backoffice == False:
                build_temp_files(camelName)
                if args.force:
                    if page_match_traduccion:
                        fileseeder("gtemp", camelName, kebabTraduccion, True, True)
                    if page_match_default:
                        fileseeder("gtemp", camelName, None, True)
                    fileseeder("land", camelName, None, True)
                if template_match_traduccion:
                    fileseeder("gtemp", camelName, kebabTraduccion, False, True)
                if template_match_default:
                    fileseeder("gtemp", camelName)
                fileseeder("land", camelName)
            if args.web == False:
                if args.force:
                    fileseeder("sdoc", camelName, None, True)
                fileseeder("sdoc", camelName)
        organism_match = re.search(r'^## (\w+)$', linea)
        if organism_match:
            camelName = organism_match.group(1)
            if args.backoffice == False:
                if args.force:
                    fileseeder("org", camelName, None, True)
                fileseeder("org", camelName)
            if args.web == False:
                if args.force:
                    fileseeder("sobj", camelName, None, True)
                fileseeder("sobj", camelName)
        molecule_match = re.search(r'^### (\w+)$', linea)
        if molecule_match:
            camelName = molecule_match.group(1)
            if args.backoffice == False:
                if args.force:
                    fileseeder("mol", camelName, None, True)
                fileseeder("mol", camelName)
                
sys.stdout.close()

if args.show:
    subprocess.call(["python3", rs_path , "--show" ])
else:
    subprocess.call(["python3", rs_path ])