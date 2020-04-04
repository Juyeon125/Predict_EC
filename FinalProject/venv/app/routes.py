from flask import Flask, render_template, request


 
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


if __name__ == '__main__':
  app.debug = True
  app.use_reloader=True
  app.run(host='0.0.0.0', port=80) 
  #port : 5000