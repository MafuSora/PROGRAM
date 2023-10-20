# build_files.sh
pip install -r requirements.txt
python3.2 manage.py collectstatic
