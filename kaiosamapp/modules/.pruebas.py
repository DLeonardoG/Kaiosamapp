import shutil

def imprimir_texto_centralizado(texto):
    # Obtener el ancho de la consola
    ancho_consola = shutil.get_terminal_size().columns

    # Calcular el espacio en blanco necesario para centrar el texto
    espacio_blancos = (ancho_consola - len(texto)) // 2

    # Imprimir el texto centrado
    print(' ' * espacio_blancos + texto)

# Ejemplo de uso
texto = "Texto centrado"
imprimir_texto_centralizado(texto)




