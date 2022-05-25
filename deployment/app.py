from flask import Flask, render_template, request, send_file
#from reg import register_yourself
from flask import flash
app = Flask(__name__)

app.secret_key = 'sri'
@app.route('/')
def indexpage():
    return render_template('home.html')
#
@app.route("/sub",methods = ['GET' , 'POST'])
def submit1():
    #if request.form.get("submit1"):
    import attendanceproject
    attendanceproject.att()
    return "ATTENDANCE MARKED"
@app.route("/reg",methods=['GET','POST'])
def reg():
    import reg
    reg.regi()
    #print("Registration Successful")
    return render_template("home.html")

@app.route("/sub1",methods = ['GET' , 'POST'])
def submit2():
    #if request.form.get("submit1"):
    import attendanceproject1
    attendanceproject1.att()
    return "ATTENDANCE MARKED"


    
if __name__ == '__main__':
    app.run(debug = True)