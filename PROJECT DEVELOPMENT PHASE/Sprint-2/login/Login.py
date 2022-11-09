#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,request,render_template
import pickle

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("login_page.html")

database={'lydia@gmail.com':'lydia','janaki@gmail.com':'janaki',
          'praveena@gmail.com':'praveena','muthulakshmi@gmail.com':'muthulakshmi'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['email']
    pwd=request.form['psw']
    if name1 not in database:
	    return render_template('login_page.html',info='Invalid E-mail')
    else:
        if database[name1]!=pwd:
            return render_template('login_page.html',info='Invalid Password')
        else:
	         return render_template('login_success.html',email=name1)

if __name__ == '__main__':
    app.run()


# In[ ]:





# In[ ]:




