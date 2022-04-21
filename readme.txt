python
Django

-base de datos:
Install XAMPP.
Run APACHE and MySQL.
Run on the terminal: pip3 install PyMySQL
Run on the terminal: pip3 install pillow

Una vez la estructura de models.py de la base de datos esté hecha, se corre: python manage.py makemigrations
luego se hace la migración a la base con: python manage.py migrate
Si se quiere hacer un cambio en la estructura de la base de datos, se puede hacer por medio del archivo models.py
corriendo los dos comandos anteriores

crear un super usuario: python mange.py createsuperuser
con esos datos ingresados podemos ingresar al "#de host"/admin para poder ingresar