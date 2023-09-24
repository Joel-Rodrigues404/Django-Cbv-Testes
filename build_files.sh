echo "start"

python -m pip install -r requirements.txt
python manage.py collectstatic
# python3.9 manage.py migrate --noinput -- clear

echo "end"

