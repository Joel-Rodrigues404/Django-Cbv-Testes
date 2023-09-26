 echo "BUILD START"
 echo "INSTALL REQUIREMENTS"
 python3.9 -m pip install -r requirements.txt
 echo "MAKEMIGRATIONS"
 python3.9 manage.py makemigrations --noinput
 python3.9 manage.py migrate --noinput
 echo "COLLECTSTATIC"
 python3.9 manage.py collectstatic --noinput
 echo "BUILD END"