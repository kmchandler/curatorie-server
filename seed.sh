#!/bin/bash
rm -rf curatorieapi/migrations
rm db.sqlite3
python3 manage.py migrate
python3 manage.py makemigrations curatorieapi
python3 manage.py migrate curatorieapi
python3 manage.py loaddata users
python3 manage.py loaddata boards
python3 manage.py loaddata board_types
python3 manage.py loaddata gift_cards
python3 manage.py loaddata inspo_cards
python3 manage.py loaddata list_cards
python3 manage.py loaddata purchase_cards
python3 manage.py loaddata share_requests
python3 manage.py loaddata shared_boards
python3 manage.py loaddata icons
