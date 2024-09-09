#Crear un ambiernte de desarrollo -- python enviroment

1: python -m venv envAplicativo
2: instalamos los requerimientos : pip install requirements.txt
3: Carpeta VaterinariaBack/setting/local.py Modificar ALLOWED_HOSTS a nuestra ip local
4: Dentro del mismo archivo local.py corregir la conexion con nuestra base de datos SQL server
5: correr el comando : python manage.py runserver 192.168.tu.ip:4000

