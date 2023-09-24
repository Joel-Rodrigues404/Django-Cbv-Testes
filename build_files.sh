echo "start"

pip install -r requirements.txt
python3.10.4 -m manage.py collectstatic --noinput --clear

echo "end"

