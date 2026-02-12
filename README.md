# Simulador de Autómata Finito Determinista (AFD)
# Autor: Juan Camilo Lozano Cortes
### Validación de Cadenas con Prefijo Cero

Este programa implementa un modelo computacional de un Autómata Finito Determinista (AFD) en Python. El objetivo principal es procesar un archivo de texto con múltiples cadenas y determinar si pertenecen al lenguaje regular definido.

## 1. Definición de la Lógica del Autómata

El autómata está diseñado bajo la restricción de que toda cadena válida debe iniciar obligatoriamente con el símbolo '0' y estar compuesta exclusivamente por el alfabeto binario.

### Especificaciones Formales:
* **Alfabeto (Σ):** {0, 1}
* **Conjunto de Estados (Q):** {q0, q1, q_error}
* **Estado Inicial:** q0
* **Estado de Aceptación (F):** {q1}

### Comportamiento de las Transiciones:
1.  **Estado q0 (Inicial):** Si el primer carácter es '0', transita a q1. Si es '1' o cualquier otro carácter (como '.'), transita a q_error.
2.  **Estado q1 (Aceptación):** Permanece en q1 si recibe '0' o '1'. Si recibe cualquier carácter fuera del alfabeto, transita a q_error.
3.  **Estado q_error (Muerte):** Una vez que el autómata entra en este estado, la cadena se marca como NO ACEPTA y se detiene el procesamiento de esa línea.



## 2. Instrucciones de Ejecución en Linux

Para ejecutar el programa correctamente en un entorno basado en Unix/Linux, siga estos pasos detallados:

### Paso 1: Localización de los archivos
Es indispensable que el archivo del programa `AFD.py` y el archivo de datos `entrada.txt` se encuentren en el mismo directorio.

### Paso 2: Acceso a la ruta desde la terminal
Debe abrir una terminal y navegar hasta la carpeta específica donde guardó los archivos. Utilice el comando `cd` (change directory):

```bash
cd /ruta/hacia/tu/carpeta/donde/esta/el/codigo
