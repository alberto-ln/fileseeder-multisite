def camel_to_kebab(string):
    # Buscamos todas las letras mayúsculas en la cadena y las reemplazamos por "-letra"
    kebab = ''.join(['-' + i.lower() if i.isupper() else i for i in string])
    # Si la cadena empieza por mayúscula, eliminamos el primer "-"
    if kebab[0] == '-':
        kebab = kebab[1:]
    return kebab