import _mysql
import inspect
import logging

def lineno():
    return inspect.currentframe().f_back.f_lineno

def fetch_dict(db):
    sql = db.store_result()
    if sql is None:
        logging.exception('No valid result. Please check for query errors.')
    else:
        all = False
        while not all:
            row = sql.fetch_row(how=1)
            if row == tuple():
                all = True
            else:
                yield row[0]

def query(db, line, query):
    try:
        db.query(query)
    except _mysql.MySQLError, e:
        logging.exception('MySQL error at line '+str(line)+': "'+e[1]+'"')


db = _mysql.connect(host='localhost', user='test', passwd='testpw', db='test')

query(db, lineno(), "SELECT * FROM `test` ORDER BY `num` DESC")

for row in fetch_dict(db):
    print row