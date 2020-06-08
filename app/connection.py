import pymysql

def connection():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='7777', db='test', charset='utf8')
    return conn