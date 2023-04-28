import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--show', help='Muestra toda la salida', action='store_true')
args = parser.parse_args()


root_path = os.getcwd()
his_path = os.path.join(root_path, 'historial_fs.txt')
with open(his_path, "r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        if args.show:
            print(linea.strip())
        else:
            if linea.find("ya existe") != -1:
                print(linea.strip())

os.remove(his_path)