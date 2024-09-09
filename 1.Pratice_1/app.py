###S1- Import Flask

from flask import Flask




##S2 -  init a Flask object with __name_ Parameter
app = Flask(__name__)



##S3 - Create an endpoint /route and
#Bind each route some functionality
@app.route('/')
def home():
    return "Welcome to My Billion Dollor Application $$$$"




#S4 - Run the app

if __name__ == '__main__':
    app.run(debug = True)
