def convertirEspaciado(frase):
  frase=" ".join(frase)
  frase=frase.replace("  ","") # correccion* utlice el metodo replace para eliminar donde habia dos espacios
  return frase

convertirEspaciado("hola, tu")
