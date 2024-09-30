#S1 - import Flask
from flask import Flask

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
    return "Welcome to this Flask Course."

@app.route('/test')
def test():
    return "This is a test page."

@app.route('/index')
def W_index():
    return "This is a Index page."

#S4 - Run the Application
if __name__=='__main__':
    app.run(debug = True) 