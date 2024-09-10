from flask import Flask,request,render_template






###
app = Flask(__name__)


###########################################
#by default the route is GET MEthod
@app.route('/')
def func():
    return render_template("first.html")
    

@app.route('/start')
def start_func():
    return render_template("temp.html")


###createing the route form and post the username on the screen .
@app.route('/form',methods = ['POST'])
def form_fun():
    u_name = request.form.get("user_name")
    u_age = int(request.form.get("user_age"))#Type cast the age
    return render_template("tq.html",u_name = u_name,u_age = u_age)#f"Thanks For the Registering {u_name}!"

###Dynamic Routing
@app.route('/in/<user_name>')
def user_profile(user_name):
    return render_template("user_profile.html",u_name = user_name)






################################################
if __name__ == "__main__":
    app.run(debug = True)