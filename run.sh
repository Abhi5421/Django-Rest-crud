echo ==== checking-for-migrations ====
python3 manage.py makemigrations
echo ================
python3 manage.py migrate
echo ======= completed-migrations ==============

python3 manage.py runserver 0.0.0.0:8001