from flask import Flask, render_template, request, redirect, url_for, session
import pymysql
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, template_folder='.', static_folder='.')
app.secret_key = 'change_this_secret'

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'deeznuts',
    'db': 'dbis_lab',
    'cursorclass': pymysql.cursors.DictCursor
}

def get_conn():
    return pymysql.connect(**DB_CONFIG)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_id = request.form.get('user_id', '').strip()
        mobile = request.form.get('mobile', '').strip()
        password = request.form.get('password', '')
        if not (user_id and password and mobile):
            return render_template('register.html', error='Fill all fields')
        hashed = generate_password_hash(password)
        conn = get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO users (user_id,mobile,password) VALUES (%s,%s,%s)",
                            (user_id, mobile, hashed))
                conn.commit()
            return redirect(url_for('login'))
        except Exception as e:
            return render_template('register.html', error=str(e))
        finally:
            conn.close()
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('user_id', '').strip()
        password = request.form.get('password', '')
        conn = get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM users WHERE user_id=%s', (user_id,))
                row = cur.fetchone()
            if row and check_password_hash(row['password'], password):
                session['user_id'] = user_id
                return redirect(url_for('welcome'))
            else:
                return render_template('login.html', error='Invalid credentials')
        finally:
            conn.close()
    return render_template('login.html')

@app.route('/welcome')
def welcome():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('welcome.html', user_id=session['user_id'])

@app.route('/courses')
def courses():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    courses = [
        {'code': 'CS 203/MA 213', 'name': 'Data Structures and Algorithms', 'credits': 3},
        {'code': 'CS 207N', 'name': 'Data Base & Information Systems', 'credits': 3},
        {'code': 'CS 209', 'name': 'Logic Design', 'credits': 3},
        {'code': 'CS 215', 'name': 'Mathematics for AI and ML', 'credits': 3},
        {'code': 'CS 253/MA 253', 'name': 'Data Structures and Algorithms Lab', 'credits': 1.5},
        {'code': 'CS 257', 'name': 'Data Base & Information Systems Lab', 'credits': 1.5},
        {'code': 'MA 205', 'name': 'Complex Analysis', 'credits': 2},
        {'code': 'MA 207', 'name': 'Differential Equations II', 'credits': 2},
        {'code': 'MA 211/CS 201', 'name': 'Discrete Mathematical Structures', 'credits': 3}
    ]
    return render_template('courses.html', courses=courses)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)