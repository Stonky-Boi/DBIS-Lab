from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__, template_folder='.', static_folder='.')
app.secret_key = 'change_this_secret'

registered_users = {}

@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        user_id = request.form.get('user_id','').strip()
        password = request.form.get('password','')
        if user_id and password:
            registered_users[user_id] = password
            return f"Registered (demo) user: {user_id}"
        return render_template('q2.html', error='Fill both fields')
    return render_template('q2.html')

if __name__ == '__main__':
    app.run(debug=True)