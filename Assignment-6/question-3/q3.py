from flask import Flask, render_template, request
import pymysql
app = Flask(__name__, template_folder='.', static_folder='.')

DB_CONFIG = {
    'host':'localhost',
    'user':'root',
    'password':'deeznuts',
    'db':'dbis_lab',
    'cursorclass': pymysql.cursors.DictCursor
}

def get_conn():
    return pymysql.connect(**DB_CONFIG)

@app.route('/', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        user_id = request.form.get('user_id','').strip()
        mobile = request.form.get('mobile','').strip()
        password = request.form.get('password','')
        if not (user_id and mobile and password):
            return render_template('q3_register.html', error='Fill all fields')
        conn = get_conn()
        try:
            with conn.cursor() as cur:
                sql = "INSERT INTO users (user_id,mobile,password) VALUES (%s,%s,%s)"
                cur.execute(sql,(user_id,mobile,password))
                conn.commit()
            return 'Registered successfully'
        except Exception as e:
            return f'Error: {e}'
        finally:
            conn.close()
    return render_template('q3.html')

if __name__=='__main__':
    app.run(debug=True)