from flask import Flask, render_template, redirect,request
import mysql.connector
from config import db_config

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(**db_config)
    # return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/feedback',methods=['GET',"POST"])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        comment = request.form['comment']

        conn = get_db_connection()
        print(conn)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO feedback (student_name , email, comments) VALUES (%s, %s, %s)", (name, email, comment))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/')
    return render_template('feedback.html')
    
@app.route('/admin')
def admin():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM feedback order by submitted_at desc")
    feedbacks = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('admin.html',feedbacks=feedbacks)

if __name__ == '__main__'
'':
    app.run(debug=True)