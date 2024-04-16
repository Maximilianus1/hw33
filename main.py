import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="db_for_python"
)
def fetchOne(id):
  mycursor=mydb.cursor()
  mycursor.execute(f"SELECT * FROM `info` WHERE `id`={id}")
  myresult=mycursor.fetchone()
  if myresult!=None:
    print(myresult)
  else:
    print("В базе нет пользователя с таким id")
def fetchAll():
  mycursor=mydb.cursor()
  mycursor.execute(f"SELECT `id`, `name`, `surname`, `s_name` FROM info")
  myresult=mycursor.fetchall()
  for i in myresult:
    print(i)
fetchOne(int(input()))
fetchAll()
