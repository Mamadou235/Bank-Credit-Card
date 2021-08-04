import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle

from mysql.connector import errorcode
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root'
app.config['MYSQL_DB']='database'

mysql= MySQL(app)


@app.route('/')
def Home():
	cur = mysql.connection.cursor()
	cur.execute("SELECT * FROM dataset")
	fetchdata = cur.fetchall()
	#mysql.connection.commit()
	cur.close()

	return render_template('home.html', data = fetchdata)



if __name__== "__main__":
	app.run(debug=True)
