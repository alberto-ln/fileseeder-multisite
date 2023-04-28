import sys
from functions.fileseeder import fileseeder

if __name__ == "__main__":

    # Establecer valores por defecto
    tipo = None
    name = None
    traduccion = None
    delete = False
    
    # Obtener los valores de tipo y name desde los argumentos de línea de comandos
    if len(sys.argv) > 2:
        tipo = sys.argv[1]
        name = sys.argv[2]

        # Si existe una traducción se pasará por el fileseeder
        if len(sys.argv) > 3 and sys.argv[3] != "--d":
            traduccion = sys.argv[3]
        
    # Si el último parámetro es --d el componente se eliminará
    if sys.argv[-1] == "--d":
        delete = True
        
    # Llamar a la función fileseeder con los valores de tipo, name y delete
    fileseeder(tipo, name, traduccion, delete)
