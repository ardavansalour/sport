on previous server:
scp -r familytree/ root@142.93.40.157:/root
scp -r /var/www/html/ root@142.93.40.157:/var/www/
scp -r /etc/nginx/sites-available/default root@142.93.40.157:/etc/nginx/sites-available



new:
apt update
apt install nginx

on new server: edit server ip in default file:
vim /etc/nginx/sites-available/default

apt install -y python3-venv
python3 -m venv django_env
source django_env/bin/activate


pip install django
pip install gunicorn
mkdir conf
vim conf/gunicorn_config.py
command = '/root/django_env/bin/gunicorn'
pythonpath = '/root/familytree'
bind = '142.93.40.157:8000'
workers = 3

mkdir familytree

from windows:
scp -r * root@64.23.160.242:/root/familytree

pip install -r familytree/requirements.txt
--------------------------------------------------------
screen -S ft
source django_env/bin/activate
gunicorn -c conf/gunicorn_config.py familytree.wsgi
ctrl a + d

screen -ls
--------------------------------------------------------
edit dns record
turn off proxy

systemctl stop nginx
apt-get install certbot -y
certbot certonly --standalone --preferred-challenges http --agree-tos --email ardavansalour@gmail.com -d ezzedoleh.com
certbot renew --force-renewal
systemctl start nginx

turn on proxy

check:
https://ezzedoleh.com/ezzadmin
--------------------------------------------------------
--------------------------------------------------------
--------------------------------------------------------
--------------------------------------------------------
OLD:

# edit ip
vim /etc/nginx/sites-available/default
vim conf/gunicorn_config.py

apt install python pip nginx python3-pip
    apt install python
    apt install pip
    apt install nginx
    apt install python3-pip
pip4 install virtualenv
apt install python3.8-venv gunicorn
    apt install gunicorn
pip install requests
pip install djangorestframework
pip install django-cors-headers
pip install django_login_history

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser