import pymysql
import connection
import json

def get_dbSelect(seqNumber):
    conn = connection.connection()

    try:
        sql = "SELECT ec_num, accepted_name, reaction FROM test.entry where ec_num =" + "'" + seqNumber + "'"
        cursor = conn.cursor()
        cursor.execute(sql)
        row_num = cursor.rowcount
        
    finally:
        cursor.close()

    if row_num > 0:
        row = cursor.fetchall()
        for row_data in row :
            print(row_data[0], "db야")
            print(row_data[1], "db야")
            print(row_data[2], "db야")
            json_object = {
                "ec_num": row_data[0],
                "accepted_name": row_data[1],
                "reaction": row_data[2]
            }
            print(json_object)
        return json_object

    return "fail"
    
    
    """
    conn = connection.connection()
    
    sql = "SELECT ec_num, accepted_name, reaction FROM test.entry where ec_num =" + "'" + seqNumber + "'"


    if(seqNumber == undefined)

    cursor = conn.cursor()
    cursor.execute(sql)
    row = cursor.fetchall()
    
    

    #data_list = []

    for row_data in row :
        print(row_data[0], "db야")
        print(row_data[1], "db야")
        print(row_data[2], "db야")
        json_object = {
            "ec_num": row_data[0],
            "accepted_name": row_data[1],
            "reaction": row_data[2]
        }
    conn.close
    return json_object
    """
def get_dbInsert():
    return 0


def get_tableSelect():
    conn = connection.connection()

    try:
        sql = "SELECT ec_num, accepted_name, reaction FROM test.entry"
        cursor = conn.cursor()
        cursor.execute(sql)
        row_num = cursor.rowcount
        
    finally:
        cursor.close()

    if row_num > 0:
        object_list = []
        row = cursor.fetchall()
        for row_data in row:
            json_object = {"ec_num": row_data[0], "accepted_name": row_data[1], "reaction": row_data[2]}
            object_list.append(json_object)
        return object_list

    return "fail"
