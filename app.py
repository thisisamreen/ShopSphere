from flask import Flask, redirect, render_template, request, url_for

from models import User, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)



@app.route('/')
def home():
    render_template('index.html')
    return "Welcome to Grocery Shopping App"

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            if user.is_admin:
                return redirect('/admin_dashboard')
            else:
                return redirect('/user_dashboard')
        else:
            return "Invalid credentials"
    return render_template('login.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')

@app.route('/user_dashboard')
def user_dashboard():
    return render_template('user_dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)