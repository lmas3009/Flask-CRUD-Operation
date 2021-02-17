from flask import *
import json
import pymysql as Mysql

app = Flask(__name__)

mydb = Mysql.connect(host="localhost",user="root",password="",database="crudflask")
mycursor = mydb.cursor()

data_verify=[]
name_email=[]

@app.route("/")
def index():
    mycursor.execute("SELECT * FROM userinfo")
    data = mycursor.fetchall()
    # print(data)
    length = len(data)
    data_verify = []
    for i in range(len(data)):
        name_email.append(data[i][0])
        name_email.append(data[i][1])
    data_verify.append(name_email)
    # print(data_verify)
    return render_template("index.html",data=data,len = length)

@app.route("/userdetails",methods=['GET', 'POST', 'PUT'])
def userdetails():
    print(data_verify)
    if request.method == "POST":
        uname = request.form['uname']
        email = request.form['email']
        gender = (request.form.get('gender'))
        age = request.form['age']
        clgname = request.form['clgname']
        print(uname,email,gender,age,clgname)

        mycursor.execute("SELECT * FROM userinfo")
        data = mycursor.fetchall()
        length = len(data)
        if(length!=0):
            for i in range(len(data)):
                if((uname != data[i][0] or uname == "") and (email != data[i][1] or email == "")):
                    cmd = "INSERT INTO `userinfo`(`Name`, `EmailId`, `Gender`, `Age`, `ClgName`) VALUES(%s,%s,%s,%s,%s)"
                    val = (uname,email,str(gender),age,clgname)
                    res = mycursor.execute(cmd,val)
                    mydb.commit()
                    print(res)
                else:
                    return  "Name or Email is already Used"
        else:
            cmd = "INSERT INTO `userinfo`(`Name`, `EmailId`, `Gender`, `Age`, `ClgName`) VALUES(%s,%s,%s,%s,%s)"
            val = (uname,email,str(gender),age,clgname)
            res = mycursor.execute(cmd,val)
            mydb.commit()
            
    return redirect("/")

@app.route("/update/<string:id_data>")
def update(id_data):
    update_details=[]
    mycursor.execute("SELECT * FROM userinfo")
    data = mycursor.fetchall()
    for i in range(len(data)):
        if(data[i][0]==int(id_data)):
            update_details.append(data[i][0])
            update_details.append(data[i][1])
            update_details.append(data[i][2])
            update_details.append(data[i][3])
            update_details.append(data[i][4])
            update_details.append(data[i][5])
            return render_template("update.html",data = update_details)
    return redirect("/")

@app.route("/Update/<string:id_data>",methods=['POST'])
def Update(id_data):
    if request.method=="POST":
        uname = request.form['uname']
        email = request.form['email']
        age = request.form['age']
        clgname = request.form['clgname']
        print(uname,email,age,clgname)
        cmd = "UPDATE `userinfo` SET `Name`=%s,`EmailId`=%s,`Age`=%s,`ClgName`=%s WHERE `Id`=%s"
        val = (uname,email,age,clgname,id_data)
        res = mycursor.execute(cmd,val)
        mydb.commit()
        return redirect("/")


@app.route("/delete/<string:id_data>")
def delete(id_data):
    cmd = "DELETE FROM `userinfo` WHERE `Id`=%s"
    val = (int(id_data))
    mycursor.execute(cmd,val)
    mydb.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)