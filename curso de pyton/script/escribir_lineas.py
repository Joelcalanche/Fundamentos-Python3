

import sys
if len(sys.argv) == 3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])

    for r in range(repeticiones):
        print(texto)
else:
    print("error, introduce los argumentos correctamente")
    print("ejemplo: escribir_lineas.py 'texto' 5 ")