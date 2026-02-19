Descripción

Esta aplicación en Python permite gestionar tareas desde consola.
El usuario puede agregar nuevas tareas, listarlas y marcarlas como completadas.
Además, implementa el patrón de diseño Singleton para la configuración global
y guarda las tareas en un archivo JSON, de modo que se conservan entre ejecuciones.

Características

Agregar, listar y completar tareas.
Guardado automático de tareas en formato JSON.
Carga automática de las tareas al iniciar.
Uso del patrón Singleton para controlar la configuración global (modo debug).
Pruebas unitarias con unittest para validar el funcionamiento.

Ejecución

Abrir una terminal en la carpeta del proyecto.
Ejecutar el programa con:
python tarea2.py
Usar las opciones del menú para administrar las tareas.
El programa guarda automáticamente los cambios antes de salir.

Pruebas

Para ejecutar las pruebas unitarias:
python -m unittest test_tareas2.py
Las pruebas verifican:
El funcionamiento del patrón Singleton.
La creación, listado y completado de tareas.
La correcta lectura y escritura del archivo JSON.


# Desarrollo-y-gesti-n-de-una-aplicaci-n-de-tareas
