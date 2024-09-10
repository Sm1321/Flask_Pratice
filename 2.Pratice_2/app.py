from flask import Flask,request,render_template



####
#-- Create a Flask Object and Pass __name__
app = Flask(__name__)




#-------------------------------------------------------------
@app.route('/')
def index():
    return render_template("first.html")

@app.route('/add')
def add_func():
    # Get query parameters
    var_1 = int(request.args.get('a'))
    var_2 = int(request.args.get('b'))
    # Calculate the total
    total = var_1 + var_2
    return str(total)



#---------------------------------------------------------------------------







###
if __name__=="__main__":
    app.run(debug = True)