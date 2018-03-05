import uuid
from logging import getLogger

import psycopg2
import ujson
from psycopg2.extras import RealDictCursor


log = getLogger(__name__)


class Contacts:
    def __init__(self):
        host = 'localhost'
        user = 'Brien'
        password = ''
        dbname = 'Miami'
        self._connection = psycopg2.connect(host=host, user=user, password=password, dbname=dbname)
        self._cursor = self._connection.cursor(cursor_factory=RealDictCursor)

    def __del__(self):
        if self._connection:
            self._connection.close()

    def get_all(self):
        self._cursor.execute('SELECT * FROM "Contacts"')
        return [{'id': row['id'], **row['data']} for row in self._cursor.fetchall()]

    def create(self, data):
        id = uuid.uuid4()
        data.pop('id', None)
        self._cursor.execute("INSERT INTO \"Contacts\" (id, data) VALUES ('{}', '{}')".format(id, ujson.dumps(data)))
        self._connection.commit()
        return 'Contact created'

    def update(self, id, data):
        data.pop('id', None)
        self._cursor.execute("UPDATE \"Contacts\" SET data = '{}' where id = '{}'".format(ujson.dumps(data), id))
        self._connection.commit()
        return 'Contact updated'

    def delete(self, id):
        self._cursor.execute("DELETE FROM \"Contacts\" WHERE id = '{}'".format(id))
        self._connection.commit()
        return 'Contact deleted'
