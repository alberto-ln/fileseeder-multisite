import os

def delete_dir(dir_path):
    
    # Elimina todos los archivos dentro del directorio
    for root, dirs, files in os.walk(dir_path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))

        # Elimina todos los subdirectorios
        for name in dirs:
            os.rmdir(os.path.join(root, name))

    # Elimina el directorio principal
    os.rmdir(dir_path)