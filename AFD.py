import sys # Importamos la libreria sys, para que pueda interactuar directamente con el interprete de python.

def simular_afd(archivo):
    # Definición formal del AFD
    # Q = {'q0', 'q1', 'q_error'}
    # Sigma = {'0', '1'}
    # F = {'q1'}
    
    try:
        # Abrimos el archivo de texto en modo lectura.
        with open(archivo, 'r') as f:
            for linea in f:
                # Limpiamos saltos de linea, al ser un listado.
                cadena = linea.strip()
                if not cadena:
                    continue
                
                estado_actual = 'q0'
                alfabeto = {'0', '1'}
                
                for simbolo in cadena:
                    # Lógica de transiciones d(q, s) desde el estado inicial.
                    if estado_actual == 'q0':
                        if simbolo == '0':
                            estado_actual = 'q1'
                        else:
                            estado_actual = 'q_error'
                            break # Si llega a leer un caracter como el ".", en vez de tener un valor entero como el "1000" dara error.
                            
                    elif estado_actual == 'q1':
                        if simbolo in alfabeto:
                            estado_actual = 'q1'
                        else:
                            estado_actual = 'q_error'
                            break
                    
                    elif estado_actual == 'q_error':
                        break

                # Verificación de estado final.
                if estado_actual == 'q1':
                    print(f"{cadena} ACEPTA")
                else:
                    print(f"{cadena} NO ACEPTA")
                    
    except FileNotFoundError:
        pass # Por si da error, al no existir el archivo de texto.

if __name__ == "__main__":
    # Con esto podemos abrir nuestro entrada.txt
    if len(sys.argv) > 1:
        simular_afd(sys.argv[1])

# Juan Camilo Lozano Cortes