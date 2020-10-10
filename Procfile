web: python manage.py runserver 0.0.0.0:$PORT
web: gunicorn artist_albums.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate

