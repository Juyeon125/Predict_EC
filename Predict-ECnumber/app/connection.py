import pymysql
import json

input_path = "./config.json"

with open(input_path, "r") as json_file:
  data = json.load(json_file)

def connection():
    conn = pymysql.connect(host=data['dbHost'], user=data['dbUser'], password=data['dbPassword'], db=data['db'], charset='utf8')
    return conn