
# A continuación el código que conecta sqlite con python
import sqlite3
from sqlite3 import Error
from flask import current_app, g

def get_db():
    try:
        if 'db' not in g:
            print('conectada')
            # A continuación va el nombre de la base de datos
            g.db = sqlite3.connect('/home/alinero09/mysite/database/DB_CUDAC.db')
            return g.db
    except Error:
        print(Error)

def close_db():
    db = g.pop( 'db', None)

    if db is not None:
        db.close()
