import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ninja",
    database="akmal"
)

mycursor = mydb.cursor()
mycursor.execute("select * from vagon where id_poezd = 1;")

myresult = mycursor.fetchall()

with open("RedHat.txt", "r") as file:
    content = file.read()

print(content)

print("справка 118 (наличие в поезде вагонов, подлежащих ремонту(:213 0:7200001 7236 118:)")

print("1 -s ИНДЕКС_ПОЕЗДА: 72000017236 ")
malimot = ['1']

for i in range(10000):
    kirish = input("Kiritish------>: ")
    if kirish in malimot:
        for x in myresult:
            print(x)
    else:
        print("bunday malumot bazada yo`q iltmos tekshrib qatatan urinib ko`ring")