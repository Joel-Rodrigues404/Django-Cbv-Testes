echo "start"

pip install -r requirements.txt
python manage.py collectstatic --noinput --clear

echo "end"

