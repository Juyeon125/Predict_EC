import pymysql
import connection
import json

def get_dbSelect_login(email, pw):
    conn = connection.connection()

    try:
        sql = "SELECT email FROM test.member where email =" + "'" + email + "'" + "AND pw = '" + pw + "'"
        cursor = conn.cursor()
        cursor.execute(sql)
        row_num = cursor.rowcount
        
    finally:
        cursor.close()

    if row_num > 0:
        row = cursor.fetchall()
        for row_data in row :
            json_object = {
                "email": row_data[0]
            }
        print(json_object)
        return json_object

    return "fail"

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
            json_object = {
                "ec_num": row_data[0],
                "accepted_name": row_data[1],
                "reaction": row_data[2]
            }
        return json_object

    return "fail"

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

def get_dbInsert_register(email, pw, first, last):
    conn = connection.connection()

    try:
        sql = "SELECT email FROM test.member where email =" + "'" + email + "'"
        cursor = conn.cursor()
        cursor.execute(sql)
        row_num = cursor.rowcount
        
    finally:
        cursor.close()

    if row_num > 0:
        return "fail"
    
    else:
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO member (email, pw, first, last) VALUES (%s, %s, %s, %s);"
            val = (email, pw, first, last)
            cursor.execute(sql,val)

            conn.commit()
        
        finally:
            cursor.close()
            return "true"