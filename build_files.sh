echo "BUILD START"
pip install -r requirements.txt
python manage.py makemigrations --noinput
python manage.py migrate --noinput
python seed_data.py
python manage.py collectstatic --noinput --clear
echo "BUILD END"
