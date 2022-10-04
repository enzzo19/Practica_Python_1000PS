# convertirEspaciado
# Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada letra. 
# Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función.

#separa la cadena por espacios y la vuelve a unir con un espacio entre cada letra y luego reemplaza los espacios por dos espacios 
# para que quede un espacio entre cada letra

def convertirEspaciado(cadena):
    cadena = cadena.replace(", ", ",") # reemplaza el espacio despues de la coma por nada
    return " ".join(cadena).replace(" ", " ")

convertirEspaciado("Hola, tú") #  Output:  'H o l a , t ú'

