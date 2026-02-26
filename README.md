# Calculadora de Promedios

Este proyecto contiene una calculadora de promedios sencilla escrita en Python.
Se ejecuta desde la línea de comandos y permite ingresar el nombre de un estudiante,
la cantidad de materias y las notas correspondientes. Luego calcula y muestra el
promedio final.

## Ejecución

Asegúrese de tener Python 3 instalado y, en una terminal, navegue al directorio del proyecto:

```bash
cd "c:\Users\juanh\OneDrive\Escritorio\DOCUMENTOS\UNIR PRIMER SEMESTRE\Logica computacional\calculadora_prom"
```

### Versión de línea de comandos

```bash
python calculadora.py
```

Siga las instrucciones en pantalla para ingresar los datos. El programa pide nombre, cantidad de materias y luego cada materia con su nota.

### Interfaz gráfica

Si prefiere una ventana con campos de formulario, puede usar el archivo `calculadora_gui.py`:

```bash
python calculadora_gui.py
```

Aparecerá una pequeña ventana donde podrá introducir el nombre del estudiante, la cantidad de materias y luego rellenar las notas. Se mostrará una ventana emergente con el promedio y si el alumno aprobó (mínimo 6.0).

### Versión web local

También existe una página HTML (`index.html`) que puede abrirse directamente en el navegador sin necesidad de servidor. Simplemente haga doble clic en el archivo o arrástrelo a una ventana del navegador. La página ofrece un formulario dinámico y calcula el promedio con la misma lógica (nota mínima 6.0).

> Si necesita un servidor HTTP local, puede usar Python para servir el directorio:
>
> ```bash
> python -m http.server 8000
> ```
>
> y luego abrir `http://localhost:8000/index.html` en el navegador.

## Consideraciones

- Las notas se consideran en una escala de 0 a 10.
- No se usan dependencias externas.
