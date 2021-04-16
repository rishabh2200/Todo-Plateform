# TODO-Plateform

## Local deployment

It is recommended you use a *virtual environment* required   
Required python version Python 3.6.9
**install all the dependencies**
$ pip install -r requirements.txt  

#### start redis server
$ services start redis  
or  
$ sudo systemctl start redis  
[redis-basic-command](https://www.tutorialspoint.com/redis/redis_commands.htm#:~:text=To%20start%20Redis%20client%2C%20open,you%20can%20run%20any%20command.&text=In%20the%20above%20example%2C%20we,server%20is%20running%20or%20not.)  

**Set Enviroment variable for redis **  
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
$ python manage.py migrate  

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('db_path'),
        'PORT': 5432,
    }
}
```
#### Run
$ python manage.py runserver    

## EC2 deployment 
**Run EC2 instance **  
[link](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html#:~:text=Open%20the%20Amazon%20EC2%20console,assign%20IPv6%20IP%2C%20choose%20Enable.)    
**install ansible and ansible-playbook**  
Follow this  [guide](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)  

**Run Ansible**
* ansible-playbook provision.yml --key-file "<ssh-EC2>"      
* ansible-playbook deploy.yml --key-file "<ssh-EC2>"      
* ansible-playbook todo-automation.yml --key-file "<ssh-EC2>"  

## HELM
**Create kubernetes cluster**
[cluster](https://humanitec.com/blog/how-to-set-up-a-kubernetes-cluster-on-gcp#:~:text=Create%20the%20cluster&text=This%20is%20where%20you%20create,cluster%20options%20to%20choose%20from.)  

On kubernetes terminal run coomand
$ helm install <project_name> todo_helm
