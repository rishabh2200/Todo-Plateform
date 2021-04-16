# TODO-Plateform

## Local deployment

It is recommended you use a *virtual environment* required   
Required python version Python 3.6.9
*install all the dependencies*  
$ pip install -r requirements.txt  

#### start redis server
$ services start redis  
or  
$ sudo systemctl start redis  
[redis-basic-command](https://www.tutorialspoint.com/redis/redis_commands.htm#:~:text=To%20start%20Redis%20client%2C%20open,you%20can%20run%20any%20command.&text=In%20the%20above%20example%2C%20we,server%20is%20running%20or%20not.)  

*Set Enviroment variable for redis *  
$ export redis_path='redis://redis:6379/0'  

#### Create database in postgres
* [Postgres-WithDjango](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-django-with-postgres-nginx-and-gunicorn)  
* sudo su - postgres  
* createdb mydb  
* createuser -P  
* psql  
* GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;  
*Set Enviroment variable*
$ export db_path='127.0.0.1'  
$ export POSTGRES_DB='mydb'  
$ export POSTGRES_USER='postgres'  
$ export POSTGRES_PASSWORD='postgres'  




$ python manage.py runserver  





## Local deployment using docker
Required docker version Docker version 20.10.3 



