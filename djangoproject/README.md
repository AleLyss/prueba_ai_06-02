# TecnoScorpion
Aplicacion desarrollada en DJango
## Cómo iniciar el proyecto?
1. Instalar Postgresql en tu pc desde: 
    * Desde windows: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
    * Otros SO: https://www.postgresql.org/download/
2. Tener instalado Python o hacerlo desde: https://www.python.org/downloads/
3. Clonar este repositorio
4. Editar el archivo **mysite/settings.py** en la parte **DATABASES** con las credenciales de tu base de datos.
5. Ejecutar en tu linea de comnado: **python pip install virtualenv**
6. Acceder a la ruta del proyecto y en la terminal ejecutar **virtualenv env**
7. Luego en la terminal ejecutar **env/scripts/activate**
8. Ejecutar en la linea de comandos **python pip install -r requirements.txt**
9. Ejecutar en linea de comandos **python manage.py migrate**
10. Crear el superusuario con **python manage.py createsuperuser**
11. Iniciar el proyecto con **python manage.py runserver**
