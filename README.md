# AFD_juanlozano

# Simulador de Autómata Finito Determinista (AFD)
### Proyecto: Validación de Cadenas Binarias con Inicio Específico

Este proyecto es una implementación robusta en Python de un **AFD** diseñado para filtrar cadenas basadas en su símbolo inicial y su composición.

---

## Lógica del Autómata
El programa evalúa cada línea de un archivo de texto y determina si pertenece al lenguaje definido.

### Reglas de Validación:
1. **Condición de Inicio:** La cadena debe empezar obligatoriamente con el carácter `0`.
2. **Alfabeto ($\Sigma$):** Solo se permiten los caracteres `{0, 1}`.
3. **Restricción de Punto:** El carácter `.` no es parte del alfabeto y causará el rechazo inmediato (Estado de Error).
4. **Estado de Aceptación:** Solo si el autómata termina en el estado $q1$ después de procesar toda la cadena, se marcará como **ACEPTA**.

### Diseño Formal
* **Estados:** $Q = \{q0, q1, q\_error\}$
* **Estado Inicial:** $q0$
* **Estado Final:** $F = \{q1\}$
* **Transiciones principales:**
    - $\delta(q0, 0) \rightarrow q1$
    - $\delta(q1, \{0, 1\}) \rightarrow q1$
    - $\delta(cualquiera, .) \rightarrow q\_error$

---

## Ejecución en Linux (Paso a Paso)

Para correr este programa en cualquier distribución de Linux (Ubuntu, Debian, Fedora, etc.), sigue estos pasos:

### 1. Preparar los archivos
Asegúrate de tener en la misma carpeta:
* `AFD.py` (El código fuente)
* `entrada.txt` (El archivo con las cadenas)

### 2. Abrir la Terminal
Haz clic derecho en la carpeta y selecciona **"Abrir en la terminal"**.

### 3. Ejecutar el comando
Escribe lo siguiente y presiona `Enter`:
```bash
python3 AFD.py entrada.txt
