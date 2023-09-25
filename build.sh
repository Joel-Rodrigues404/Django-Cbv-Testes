 echo "BUILD START"
 echo "INSTALL REQUIREMENTS"
 python3 -m pip install -r requirements.txt
 echo "MAKEMIGRATIONS"
 python3 manage.py makemigrations --noinput
 python3 manage.py migrate --noinput
 echo "COLLECTSTATIC"
 python3 manage.py collectstatic --noinput --clear
 echo "BUILD END"