from flask import Flask, url_for, session, redirect, escape, render_template, request, session
import mysql_dao
import json
 
app = Flask(__name__)      

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
  if 'username' in session:

    result = '%s' % escape(session['username'])
    print(result,'main')
    return render_template('mainFrame.html', loginId = result)
  else:
    print('없어서 추가함')
    session['username'] = ''
    result = '%s' % escape(session['username'])

    print(result)
    return redirect('/')
 
@app.route('/search_page')
def search_page():
  if 'username' in session:

    result = '%s' % escape(session['username'])
    print(result,'main')
    return render_template('search.html', loginId = result)
  else:
    print('없어서 추가함')
    session['username'] = ''
    result = '%s' % escape(session['username'])

    print(result)
    return redirect('/search_page')

@app.route('/intro_page')
def intro_page():
  if 'username' in session:

    result = '%s' % escape(session['username'])
    print(result,'main')
    return render_template('intro_page.html', loginId = result)
  else:
    print('없어서 추가함')
    session['username'] = ''
    result = '%s' % escape(session['username'])

    print(result)
    return redirect('/intro_page')

@app.route('/developer_page')
def developer_page():
    if 'username' in session:

      result = '%s' % escape(session['username'])
      print(result,'main')
      return render_template('developer_page.html', loginId = result)
    else:
      print('없어서 추가함')
      session['username'] = ''
      result = '%s' % escape(session['username'])

    print(result)
    return redirect('/developer_page')
 
@app.route('/contact_page')
def contact_page():
    if 'username' in session:

      result = '%s' % escape(session['username'])
      print(result,'main')
      return render_template('contact_page.html', loginId = result)
    else:
      print('없어서 추가함')
      session['username'] = ''
      result = '%s' % escape(session['username'])

    print(result)
    return redirect('/contact_page')

@app.route('/register_page')
def register_page():
  return render_template('register_page.html')

@app.route('/login_page')
def login_page():
  return render_template('login_page.html')

@app.route('/mypage')
def mypage():
  
    if 'username' in session:

      result = '%s' % escape(session['username'])
      print(result,'main')
      return render_template('mypage.html', loginId = result)
    else:
      print('없어서 추가함')
      session['username'] = ''
      result = '%s' % escape(session['username'])

    print(result)
    return redirect('/mypage')

@app.route('/forgot_password_page')
def forgot_password_page():
  return render_template('forgot_password_page.html')

@app.route('/ecFunction_page')
def ecFunction_page():
  content = mysql_dao.get_tableSelect()

  if 'username' in session:

    result = '%s' % escape(session['username'])
    print(result,'main')
    return render_template('ec_function.html', loginId = result, content=content)
  else:
    print('없어서 추가함')
    session['username'] = ''
    result = '%s' % escape(session['username'])

    print(result)
    return redirect('/ecFunction_page', content=content)

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

@app.route("/login_route", methods=['GET', 'POST'])
def login_route():
  if request.method == "POST":
    reqid = request.form["id"]
    reqpw = request.form["pw"]

    content = mysql_dao.get_dbSelect_login(reqid,reqpw)
    if(content != 'fail'):
      print(content["email"])
      result = content["email"]
      session['username'] = result
      #session.pop('username', None)
    else:
      result = "fail"
  return result

@app.route("/logout")
def logout_route():

  session.pop('username', None)
  
  return redirect(request.args.get('url'))
  

if __name__ == '__main__':
  app.debug = True
  app.use_reloader=True
  app.run(host='0.0.0.0', port=80) 
  #port : 5000


@app.route('/register_route', methods=['GET', 'POST'])
def register_route(): 
  #html에서 입력받은 값 전송 받음(post)

  if request.method == "POST":
    reqid = request.form["id"]
    reqpw = request.form["pw"]
    reqfi = request.form["first"]
    reqla = request.form["last"]
    print(reqid,reqpw,reqfi,reqla)
    
    content = mysql_dao.get_dbInsert_register(reqid,reqpw,reqfi,reqla)
    #content값은 T/F

  return content
