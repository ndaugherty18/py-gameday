from . import *
import psycopg2
import sys
from ConfigParser import ConfigParser

class Store:
    def __init__(self, **args):
        parser = ConfigParser()
        parser.read('%s/db.ini' % sys.path[0])
        user = parser.get('db', 'user')
        password = parser.get('db', 'password')
        db = parser.get('db', 'db')

        args = {'user': user, 'password': password, 'database': db}

        if parser.has_option('db', 'host'):
            args['host'] = parser.get('db', 'host')

        self.db = psycopg2.connect(**args)
        self.cursor = self.db.cursor()

    def save(self):
        self.db.commit()

    def finish(self):
        self.db.commit()
        self.db.close()

    def query(self, query, values = None):
        #simplefilter("error", MySQLdb.Warning)
        res = self.cursor.execute(query, values)

    def fetchall(self, query, values = None):
        res = self.cursor.execute(query, values)
        return self.cursor.fetchall()
