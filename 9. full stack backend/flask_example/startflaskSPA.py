# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 16:29:59 2023

@author:https://python-adv-web-apps.readthedocs.io/en/latest/flask3.html
A proper Flask app is going to use multiple files — some of which will be template files. 
The organization of these files has to follow rules so the app will work. 
Here is a diagram of the typical structure:
    
    my-flask-app
   ├── static/
   │   └── css/
   │       └── main.css
   ├── templates/
   │   ├── index.html
   │   └── student.html
   ├── data.py
   └── students.py
Everything the app needs is in one folder, here named my-flask-app.

That folder contains two folders, specifically named static and templates.

The static folder contains assets used by the templates, including CSS files, JavaScript files, and images. In the example, we have only one asset file, main.css. Note that it’s inside a css folder that’s inside the static folder.

The templates folder contains only templates. These have an .html extension. As we will see, they contain more than just regular HTML.

In addition to the static and templates folders, this app also contains .py files. Note that these must be outside the two folders named static and templates.
"""


from flask import Flask, render_template, render_template_string, jsonify, request
import util
import pax


app = Flask(__name__)

# create a list of dicts from a CSV
presidents_list = util.convert_to_dict("US_presidents.csv")


@app.route('/', methods=['GET'])
def index():
    return render_template ("index.html")

@app.route('/user/<name>')
def user(name):
    return render_template('hello.html', name=name)

@app.route('/president/<num>')
def detail(num):
    try:
        pres_dict = presidents_list[int(num) - 1]
    except:
        return f"<h1>Invalid value for Presidency: {num}</h1>"
    # a little bonus function, imported on line 2 above
    ord = util.make_ordinal( int(num) )
    return render_template('president.html', pres=pres_dict, ord=ord, the_title=pres_dict['President'])

#%%
@app.route('/pax', methods=['GET'])
def indexPax():
    return render_template ("indexPax.html")

@app.route('/pax/me', methods=['GET'])
def aboutMe():
    return render_template ("aboutMe.html")

@app.route('/pax/all', methods=['GET'])
def getAllPax():
    return jsonify(pax.load())

@app.route('/pax/add', methods=['GET'])
def addPax():
    return render_template ("addPax.html")

@app.route('/pax/new2', methods=['POST'])
def addNewPax():
    pname=request.form.get('name')
    page = request.form.get('age')
    newData = {"name" :pname,
               "age":page}
    pax.addNewPax(newData)
    print(newData)
    return render_template ("addPax.html")
    
#%%
@app.route('/flask', methods=['GET'])
def test():
    return render_template ("test.html")

@app.route('/hello', methods=['GET'])
def hello():
    return render_template_string('''<!doctype html>
        <html>
            <head>
                <link rel="stylesheet" href="css url"/>
            </head>
            <body>
                <p>Hello, World!</p>
            </body>
        </html>
        ''')

        
if __name__ == "__main__":
    app.run(port=5000, debug=False)
    
 
    
