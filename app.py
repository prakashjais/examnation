from flask import Flask, render_template
import mysql.connector
import random

app = Flask(__name__)

# MySQL configuration
db_config = {
    'user': 'root',
    'password': 'Prakash1234',
    'host': 'localhost',
    'database': 'new'
}

def get_random_data():
    # Establish connection to MySQL
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    
    # Fetch all data from a specific column
    cursor.execute("SELECT * FROM courses")
    rows = cursor.fetchall()
    
    # data = [item[0] for item in rows]
    
    cursor.close()
    conn.close()
    # random.shuffle(rows)

    return rows

@app.route('/')
def index():
    random_data = get_random_data()
    return render_template('login.html', random_data=random_data)

if __name__ == '__main__':
    app.run(debug=True)
