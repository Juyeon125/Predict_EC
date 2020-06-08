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

def get_saveInfo_Select(mail):

    conn = connection.connection()
    try:
        sql = "SELECT seq, ec_num, accepted_name, reaction, acc FROM test.search where mail =" + "'" + mail + "'"
        cursor = conn.cursor()
        cursor.execute(sql)
        row_num = cursor.rowcount
    finally:
        cursor.close()
    if row_num > 0:
        object_list = []
        row = cursor.fetchall()
        object_list.append(row_num)
        for row_data in row:
            json_object = {"seq":row_data[0],"ec_num": row_data[1], "accepted_name": row_data[2], "reaction": row_data[3], "acc": row_data[4]}
            object_list.append(json_object)
        return object_list
    
            
def get_dbInsert_history_1(mail, seq, ec_num, acc):
    conn = connection.connection()
    try:
        sql = "SELECT ec_num, accepted_name, reaction FROM test.entry where ec_num =" + "'" + ec_num + "'"
        cursor = conn.cursor()
        cursor.execute(sql)
        row_num = cursor.rowcount
        if row_num > 0:
            object_list = []
            row = cursor.fetchall()
            for row_data in row:
                accepted_name = row_data[1]
                reaction = row_data[2]
    finally:
        cursor = conn.cursor()
        sql = "INSERT INTO search (mail, seq, ec_num, accepted_name, reaction, acc) VALUES (%s, %s, %s, %s, %s, %s);"
        val = (mail, seq, ec_num, accepted_name, reaction, acc)
        cursor.execute(sql,val)
        conn.commit()
        cursor.close()
        return "true"

    if row_num > 0:
        object_list = []
        row = cursor.fetchall()
        for row_data in row:
            ec_num = row_data[0]
            accepted_name = row_data[1]
            reaction = row_data[2]
        return object_list