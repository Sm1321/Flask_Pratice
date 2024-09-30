#S1 - import Flask
from flask import Flask,render_template,request

'''
It creates an instance of the Flask class,
which will be your WSGI(Web Server Gateway Interface)application

'''


#S2 - Create a Flask Object and Pass __name__
app = Flask(__name__)

##S3 - Create a route and bound it to a function
#Route1
@app.route('/')
def welcome():
    return render_template("welcome.html")

@app.route("/index",methods = ['GET'])
def index():
    return render_template("index.html")



@app.route("/form", methods=['GET', 'POST'])
def personal():
    if request.method == 'POST':
        name = request.form['name'] #name is variable in the html
        return f'Hello {name}!' 
    return render_template("form.html")



#S4 - Run the Application
if __name__=='__main__':
    app.run(debug = True) 