from flask import Flask,render_template,request,redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'testflask'

mysql = MySQL(app)

app.route('/',methods = ['GET',"POST"])

@app.route('/',methods = ['GET','POST'])
def register():  # put application's code here

    keys = ["nom","id"]
    data = [x for x in request.form.values()]
    d= {i: j for i, j in zip(keys, data)}
    nomclient=d["nom"]
    idclient=d["id"]

    print(nomclient,idclient)

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users(name, id) VALUES(%s, %s)", (nomclient, idclient))
    mysql.connection.commit()
    cur.close()
    return "success"

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True ,port=5000)
