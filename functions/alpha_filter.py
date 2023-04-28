def alpha_filter(cadena):
    letras = ""
    for caracter in cadena:
        if caracter.isalpha():
            letras += caracter
    return letras