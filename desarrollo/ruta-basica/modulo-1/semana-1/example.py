def acortar_texto(texto,max_logitud):
    
    if len(texto) >= max_logitud:
        return texto
    elif max_logitud <=5:
        return '.' * max_logitud
    else:
        return texto [:max_logitud -5] + '...'
    
print(acortar_texto(input("ejemplo"),2))