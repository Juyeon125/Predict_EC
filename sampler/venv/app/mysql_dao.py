import pymysql
import connection

def get_dbSelect(seqNumber):
    conn = connection.connection()
    
    sql = "SELECT * FROM test.example where seq =" + "'" + seqNumber + "'"

    cursor = conn.cursor()
    cursor.execute(sql)
    row = cursor.fetchall()

    #data_list = []

    for row_data in row :
        print(row_data[0])
        print(row_data[1])
    conn.close
    return row_data[1]

def get_dbInsert():
    return 0

