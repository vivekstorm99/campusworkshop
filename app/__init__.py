"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgpr61orddl9mmoi2qjg-a.singapore-postgres.render.com",
        database="todo_t6zf",
        user="root",
        password="5y7iR6utxtRn2uXEaiQQ92igPIWxmyRP")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
