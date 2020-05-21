from flask import Flask, url_for, session, redirect, escape, render_template, request, session
import mysql_dao
import json
from ml.model import *
import flask

app = Flask(__name__)      

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

def split_data(train): # dataset ->a (X_train)
    list_test = []
    train = train.upper()
    train = list(train)
    embedding_matrix = np.zeros((1000, 21))
    aa_list = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y', 'X']
    
    for i in range(len(aa_list)): # 21번만큼 반복
        if len(train) > 1000: # 현재 스플릿된 SEQ의 값이 1000보다 크면  lengh_test에 1000을 넣어줌
            length_test = 1000
        else:
            length_test = len(train) # 1000보다 아래면 그냥 그 길이를 넣어줌
        for j in range(length_test): # lengh_test의 길이만큼 반복 (1000또는 그보다 아래)
            if aa_list[i] == train[j]: # aa_list의 값(0번쨰부터 ~21번쨰)과  SEQ split해서 하나씩 검사
                     #A ==    #ASDADSASADASGSADASGDSFSDDFDSFSDFSDFSDF
                embedding_matrix[j,i] = 1
                    
    return embedding_matrix #모든 SEQ를 한글자씩 잘라놓은것을 리턴
    
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

@app.route("/index")
def index2():
    return flask.render_template('index.html')

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


#out = [1.0, 0.0], [0.0, 1.0] <- 0, 1 
# , pred = torch.max(out.data, 1)
# pred = 큰 값의 index를 반환해주는데
# 
# 데이터 예측 처리
cnn = CNN1()

@app.route('/predict', methods=['POST'])
def make_prediction():
    if request.method == 'POST':

        #predict_value = cnn(data)
        #, pred = torch.max(predict_value.data, 1)
        # pred = 0, 1 0은 비효소 1은 효소
        # cnn2, cnn3 연계할라면
        
        #if pred == 1:
            #cnn2(data)
            #cnn3(data)
        test_data = "MQYLHCCLQIAPNQEGMVQAGGQGHGLARVVLRAVLSPPCWAPHSPCGSPAATEAGRLMRRLPSVGGRMTAPKTPRFLTRRPPASSPEDPPLPHPKTPRFLTQRPPASLPRRPRFLTLGPVSSHSSGDLRLWTAHQLPQQGGCPG"
        
        test_data = split_data(test_data)
        test_data = torch.FloatTensor(test_data)
        test_data = test_data.view(1,1,1000,21)
        
        predict_value = cnn(test_data)
        _, pred = torch.max(predict_value.data, 1)
        
        if pred == 1:
            a = "효소"
            b = "효소"
        else:
            a = "비효소"
            b = "비효소"
        # 텍스트 파일 오픈
        # f = open('static/test.txt', 'r')
        
        #a= str("비효소")
        #b= str("효소")
        
        # 결과 리턴
        return render_template('index.html', a = a, b = b)

        # 텍스트 결과 리턴
        # return "</br>".join(f.readlines())


if __name__ == '__main__':
  cnn = torch.load('./model/cnn1_training-Copy3.pth')
  cnn.eval()
  app.debug = True
  app.use_reloader=True
  app.run(host='0.0.0.0', port=80) 
  #port : 5000

