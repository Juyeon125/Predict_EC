from flask import Flask, url_for, session, redirect, escape, render_template, request, session
import mysql_dao
import json
from io import StringIO
import numpy as np
import torch
import pandas as pd
from ml.cnn1_test_pyfile import CNN1
from ml.cnn2_test_pyfile import CNN2
from ml.cnn3_test_pyfile import CNN3

import flask
from flask_mail import Mail, Message
import smtplib

app = Flask(__name__)      

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "minsu960908@gmail.com" 
app.config['MAIL_PASSWORD'] = 'qwer4231' 
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
mail = Mail(app)   

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

thrid_data = pd.read_csv('./model/thrid_second_test.csv')
fourth_data = pd.read_csv('./model/Fourth_EC_total.csv')
thrid_list = thrid_data.loc[:,'EC']
fourth_list = fourth_data.loc[:,'LABEL']
def predict_ec(want_predict):
    a = split_data(want_predict)
    data = torch.FloatTensor(a)
    data = data.view(1,1,1000,21)
    classfier = cnn1(data)
    fourth_predict_list = []
    third_predict_list = []
    percentage_list = []
    
    _, binary = torch.max(classfier.data, 1)
    if binary == 1:
        thrid_predict = cnn2(data)
        thrid_predict = 100 * torch.FloatTensor(thrid_predict)

        thrid_sort, thrid_sort_index = torch.sort(thrid_predict, dim=1, descending=True)
        thrid_predict_sort = thrid_sort[0][:5].detach()
        thrid_predict_sort = np.array(thrid_predict_sort)
        
        thrid_sort_index = np.array(thrid_sort_index[0][:5])
        
        fourth_predict = cnn3(data)
        
        fourth_predict = 100 * torch.FloatTensor(fourth_predict)
        
        fourth_sort, fourth_index = torch.sort(fourth_predict, dim=1, descending=True)
        fourth_sort = fourth_sort[0][:5].detach()
        fourth_sort = np.array(fourth_sort)
        
        fourth_index = np.array(fourth_index[0][:5])

        for i in range(5):
            third_data = thrid_list[thrid_sort_index[i]]
            third_predict_list.append(third_data)
            
            fourth_data = fourth_list[fourth_index[i]]
            fourth_predict_list.append(fourth_data)
     
    return fourth_predict_list, fourth_sort

def split_data(train): # dataset ->a (X_train)
    list_test = []
    train = train.upper()
    train = list(train)
    embedding_matrix = np.zeros((1000, 21))
    aa_list = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y', 'X']
    
    for i in range(len(aa_list)): # 21번 반복
        if len(train) > 1000:
            length_test = 1000
        else:
            length_test = len(train)
        for j in range(length_test):
            if aa_list[i] == train[j]: 
                embedding_matrix[j,i] = 1
                    
    return embedding_matrix
    
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

@app.route('/test')
def test():
  return render_template('test.html')

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
  content = mysql_dao.get_saveInfo_Select()
  print(content)

  if 'username' in session:
    result = '%s' % escape(session['username'])
    print(result,'main')
    return render_template('mypage.html', loginId = result, content=content)

  else:
    print('없어서 추가함')
    session['username'] = ''
    result = '%s' % escape(session['username'])

  print(result)
  return redirect('/mypage', content=content)


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

      result1 = {'ec':'1.1.1.1', 'accuracy':'90.0'}
      result2 = {'ec':'2.1.1.1', 'accuracy':'80.0'}
      result3 = {'ec':'3.1.1.1', 'accuracy':'70.0'}
      result4 = {'ec':'4.1.1.1', 'accuracy':'60.0'}
      result5 = {'ec':'5.1.1.1', 'accuracy':'50.0'}

      return result1

@app.route("/save_Result", methods=['GET', 'POST'])
def save_Result():
  if request.method == "POST":
    reqid = request.form["seq"]
    inputreqid = request.form["input"]

    json_data = json.loads(reqid)

    print(inputreqid,'너누구냐')
    print(json_data['accepted_name'])
    print(json_data['ec_num'])
    print(json_data['reaction'])


    save_ecnum = json_data['ec_num']
    save_accep = json_data['accepted_name']
    save_reaction = json_data['reaction']

    content = mysql_dao.get_dbInsert_saveInfo(inputreqid,save_ecnum, save_accep, save_reaction)

  return reqid

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
    else:
      result = "fail"
  return result

@app.route("/logout")
def logout_route():
  session.pop('username', None)
  return redirect(request.args.get('url'))
  

@app.route('/register_route', methods=['GET', 'POST'])
def register_route(): 
  if request.method == "POST":
    reqid = request.form["id"]
    reqpw = request.form["pw"]
    reqfi = request.form["first"]
    reqla = request.form["last"]
    print(reqid,reqpw,reqfi,reqla)
    
    content = mysql_dao.get_dbInsert_register(reqid,reqpw,reqfi,reqla)

  return content

cnn1 = CNN1()
cnn2 = CNN2()
cnn3 = CNN3()

@app.route('/predict_ec', methods=['GET', 'POST'])
def make_prediction1():
    if request.method == 'POST':
        input_value = request.form["seq"]
        test_data = input_value

        fourth_one, fouth_two =  predict_ec(test_data)
        result_ec = {'ec1':fourth_one[0],'ec2':fourth_one[1],'ec3':fourth_one[2],'ec4':fourth_one[3],'ec5':fourth_one[4],'acc1':str(fouth_two[0]),'acc2':str(fouth_two[1]),'acc3':str(fouth_two[2]),'acc4':str(fouth_two[3]),'acc5':str(fouth_two[4])}
        
        return result_ec

@app.route("/contact_page", methods=['post', 'get'])
def email_test():
    if request.method == 'POST':
        senders = request.form['email_sender']
        
        receiver = request.form['email_receiver']
        content = senders + request.form['email_content']
        receiver = receiver.split(',')
       
        for i in range(len(receiver)):
            receiver[i] = receiver[i].strip()
           
        print(receiver)
       
        result = send_email(senders, receiver, content)
       
        if not result:
            return render_template('contact_page.html', content="Email is sent")
        else:
            return render_template('contact_page.html', content="Email is not sent")
    else:
        return render_template('contact_page.html')
   
def send_email(senders, receiver, content):
    msg = Message('SAMPLE 문의 메일', sender = senders, recipients = receiver)
    msg.body = content
    mail.send(msg)

if __name__ == '__main__':
  device = torch.device('cpu')
  cnn1.load_state_dict(torch.load('./model/cnn1.pth', map_location=device))
  cnn1.eval()

  cnn2.load_state_dict(torch.load('./model/cnn2.pth', map_location=device))
  cnn2.eval()

  cnn3.load_state_dict(torch.load('./model/cnn3.pth', map_location=device))
  cnn3.eval()
  
  app.debug = True
  app.use_reloader=True
  app.secret_key = "123123123"
  app.run(host='0.0.0.0', port=80) 