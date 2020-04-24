from flask import Flask, render_template, request
import mysql_dao
import json

 
app = Flask(__name__)      
 
@app.route('/')
def index():
  return render_template('mainFrame.html')
 
@app.route('/search_page')
def search_page():
  return render_template('search.html')

@app.route('/intro_page')
def intro_page():
  return render_template('intro_page.html')

@app.route('/developer_page')
def developer_page():
  return render_template('developer_page.html')
 
@app.route('/contact_page')
def contact_page():
  return render_template('contact_page.html')

@app.route('/register_page')
def register_page():
  return render_template('register_page.html')

@app.route('/login_page')
def login_page():
  return render_template('login_page.html')

@app.route('/forgot_password_page')
def forgot_password_page():
  return render_template('forgot_password_page.html')

@app.route('/ecFunction_page')
def ecFunction_page():
  content = mysql_dao.get_tableSelect()
  return render_template('ec_function.html', content=content)

@app.route('/index')
def index_page():
  return render_template('index.html') 

@app.route("/searchEc", methods=['GET', 'POST'])
def loginProc():
    if request.method == "POST":
        #밑에 코드는 사용자가 입력한 시퀀스 값
        #resSeq = request.form["seq"]


        # ------ Model -----------
        ##############
        ############
        ##########
        #######
        # ------ Model -----------

      f = open("static/ecnumResult.txt", 'r')
      lines = f.readlines()
      for line in lines:
        resSeq=line
        f.close()
        content = mysql_dao.get_dbSelect(resSeq)
        #print(content[0].scnumber)
        #print(json_string,"server")
        return content
    #return render_template("index.html")
 
  

if __name__ == '__main__':
  app.debug = True
  app.use_reloader=True
  app.run(host='0.0.0.0', port=80) 
  #port : 5000