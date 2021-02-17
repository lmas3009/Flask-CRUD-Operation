import pymysql as Mysql

mydb = Mysql.connect(host="localhost",user="root",password="",database="crudflask")
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE userinfo(Id INT NOT NULL AUTO_INCREMENT,Name CHAR(20),EmailId Char(30),Gender Char(7),Age CHAR(10), ClgName CHAR(40),PRIMARY KEY (Id))")
