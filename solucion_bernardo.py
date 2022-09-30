# convertirEspaciado
# Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada letra. 
# Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función.

#separa la cadena por espacios y la vuelve a unir con un espacio entre cada letra y luego reemplaza los espacios por dos espacios 
# para que quede un espacio entre cada letra

#programa principal
#cadena = input("ingrese una cadena: ")
#print(ConvertirEspaciado(cadena))
#assert ConvertirEspaciado("Hola, tú") == "H o l a , t ú "


def ConvertirEspaciado(cadena):
    #join une los elementos de una lista con un separador y replace reemplaza un caracter por otro
    return " ".join(cadena).replace(" ", " ") # reemplaza los espacios por dos espacios para que quede un espacio entre cada letra

print(ConvertirEspaciado("Hola, tú"))

