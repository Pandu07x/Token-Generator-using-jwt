from flask import *
from flask_session import Session
import jwt
import datetime

app=Flask(__name__,template_folder="template")
app.config["SECRET_KEY"]="ILOVEPRIYA"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['PERMANENT_SESSION_LIFETIME'] =  datetime.timedelta(minutes=1)
Session(app)


@app.route("/",methods=["GET","POST"])
def home():
    name = ""
    if request.method == "POST":
        name += request.form["name"]
    token = jwt.encode({"user": name, "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                       app.config["SECRET_KEY"])
    session["name"]=token


    print(token)



    data={
        "title":"Generated Token is:",
            "token":token
    }
    print(data)


    return render_template("index.html",data=data)

@app.route("/decode",methods=["GET","POST"])
def decode():
    name=""
    k={}
    if request.method=="POST":
        name+=request.form["name"]
        session["token"]=name
        data=jwt.decode(name, app.config["SECRET_KEY"], algorithms=["HS256"])
        k=data.copy()
    print(k)

    


    return render_template("decode.html",data=k)






if __name__=="__main__":
    app.run(debug=True)
