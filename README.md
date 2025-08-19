📚 Python Testing Demos
¡Bienvenido a python-testing-demos! Este repositorio es una colección de proyectos pequeños en Python, cada uno enfocado en demostrar y practicar diferentes aspectos del testing y el desarrollo de software con Python.

🚀 Cómo Empezar
Para clonar este repositorio, configurar los entornos y ejecutar las pruebas, sigue estos pasos:

1. Clonar el Repositorio

Abre tu terminal (en tu Mac o en Codespaces) y ejecuta el siguiente comando para clonar este repositorio en tu máquina local:

git clone https://github.com/tu_usuario/python-testing-demos.git

Nota: Reemplaza tu_usuario con tu nombre de usuario de GitHub.

Luego, navega a la carpeta del repositorio:

cd python-testing-demos

2. Estructura del Proyecto

Cada "demo" es una subcarpeta independiente dentro de este repositorio (por ejemplo, demo_calculadora_iva, demo_validador_email). Cada una de estas subcarpetas contiene su propio entorno virtual (venv/) y su propio archivo .gitignore para gestionar sus dependencias de forma aislada.

3. Configuración del Entorno Virtual y Dependencias (por Demo)

Para cada demo en el que desees trabajar, debes configurar su propio entorno virtual y sus dependencias.

Por ejemplo, para el demo del validador_email:

Navega a la carpeta del demo:

cd demo_validador_email

Crea el entorno virtual (si no existe):

python3 -m venv venv

Activa el entorno virtual:

source venv/bin/activate

(Deberías ver (venv) al inicio de tu línea de comando).

Instala las dependencias necesarias:
Si ya existe un archivo requirements.txt en la carpeta de este demo, instálalas así:

pip install -r requirements.txt

Si no existe (o si es la primera vez que añades dependencias), instálalas manualmente y luego genera el requirements.txt:

pip install pytest coverage pytest-mock pytest-json-report

Luego, genera el archivo requirements.txt para que otros (¡y tú mismo en el futuro!) puedan instalar las mismas versiones exactas de las librerías fácilmente. Asegúrate de que tu venv esté activo:

pip freeze > requirements.txt

Este comando creará el archivo requirements.txt en la carpeta actual (demo_validador_email/).

4. Ejecutar las Pruebas

Una vez que el entorno virtual esté activo y las dependencias instaladas, puedes ejecutar las pruebas para ese demo:

Asegúrate de estar en la carpeta del demo (ej., demo_validador_email/).

Asegúrate de que tu entorno virtual esté activo ((venv) en la terminal).

Ejecuta pytest:

pytest

🤝 Contribuciones
Si deseas contribuir o tienes sugerencias, no dudes en abrir un issue o pull request.