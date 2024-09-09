###----- Import Flask

from flask import Flask




##----  init a Flask object with __name_ Parameter
app = Flask(__name__)



##--- Create an endpoint /route and
#Bind each route some functionality
@app.route('/')
def home():
    return "Welcome to My First Flask APP $"




#---- Run the app

if __name__ == '__main__':
    app.run(debug = True)
