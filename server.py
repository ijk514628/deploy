from flask import Flask, render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import connectToMySQL
import re

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "asdfl;kjasdf;lkj"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
SCHEMA_NAME = 'login_and_registration'

@app.route('/')
def signin():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    is_vaild = True
    if len(request.form['first_name'])<2:
        flash("First name must be longer than 2 characters.")
        is_vaild= False
    if len(request.form['last_name'])<2:
        flash("Last name must be longer than 2 characters.")
        is_vaild= False
    if not re.match(EMAIL_REGEX, request.form['reg_email']):
        flash("Please submit vaild email address.")
        is_vaild= False
    if len(request.form['reg_password'])< 8:
        flash("Password must be at least 8 characters long.")
        is_vaild= False
    if request.form['reg_password'] != request.form['confirm_password']:
        flash("Password do not match.")
        is_vaild= False
    
    if is_vaild == False:
        return redirect('/')
    else:
        pw_hash = bcrypt.generate_password_hash(request.form['reg_password'])  
        mysql = connectToMySQL('quote_dash')
        query = "INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) VALUES(%(fn)s, %(ln)s, %(em)s, %(pw)s, NOW(), NOW());"
        data = {
            "fn": request.form['first_name'],
            "ln": request.form['last_name'],
            "em": request.form['reg_email'],
            "pw": pw_hash
        }
    user = mysql.query_db(query, data)
    session['user_id'] = user
    session['greeting'] = request.form['first_name']
    return redirect('/quotes')

@app.route('/login', methods=['POST'])
def login():
    mysql = connectToMySQL('quote_dash')
    query = "SELECT * FROM users WHERE email = %(em)s;"
    data = {
        "em": request.form['log_email']
    }
    result = mysql.query_db(query, data)
    
    if result:
        if bcrypt.check_password_hash(result[0]['password'], request.form['log_password']):
            session['user_id'] = result[0]['id']
            session['greeting'] = result[0]['first_name']
            return redirect('/quotes')
        else:
            flash("Email OR password did not match.")
    else:
        flash('Email address has not be registered.')
    return redirect('/')

@app.route('/quotes')
def wall():
    if not 'user_id' in session:
        return redirect('/')
    else:
        mysqlcn = connectToMySQL('quote_dash')
        all_quotes = mysqlcn.query_db("SELECT * FROM quotes JOIN users ON users.id = quotes.creator ORDER BY quotes.updated_at DESC;")
    return render_template("show.html", quotes = all_quotes)


@app.route('/create', methods=['POST'])
def create():
    is_valid = True
    
    if len(request.form['author'])<3:
        flash("Author name must be longer than 3 characters.")
        is_valid = False
    
    if len(request.form['content'])< 10:
        flash("Quote must be at least 10 characters long.")
        is_valid = False
    
    if is_valid == True:
        mysql = connectToMySQL('quote_dash')
        query = "INSERT INTO quotes (author, content, created_at, updated_at, creator) VALUES(%(ah)s, %(ct)s, NOW(), NOW(), %(uid)s);"
        data = {
        "ah": request.form['author'], 
        "ct": request.form['content'],
        "uid": int(session['user_id'])
        }
        mysql.query_db(query, data)
    return redirect('/quotes')

@app.route("/users/<id1>")
def show(id1):
    mysql = connectToMySQL('quote_dash')
    query = "SELECT * FROM users JOIN quotes ON quotes.creator = users.id WHERE creator = %(id)s;"
    data = {
        'id': int(id1)
    }
    user1 =  mysql.query_db(query, data)
    return render_template('show_one.html', user123 = user1, user_name = user1[0])

@app.route("/myaccount/<id2>")
def edit(id2):
    mysql = connectToMySQL('quote_dash')
    query = "SELECT * FROM users WHERE id = %(id)s;"
    data = {
        'id': int(id2)
    }
    user2 =  mysql.query_db(query, data)
    return render_template('edit.html', user = user2)

@app.route("/myaccount/<id3>/update", methods = ['POST'])
def update(id3):
    is_vaild = True
    if len(request.form['first_nameE'])<2:
        flash("First name must be longer than 2 characters.")
        is_vaild= False
    if len(request.form['last_nameE'])<2:
        flash("Last name must be longer than 2 characters.")
        is_vaild= False
    if not re.match(EMAIL_REGEX, request.form['email_E']):
        flash("Please a valid email address.")
        is_vaild= False
    if is_vaild == True:
        mysql = connectToMySQL('quote_dash')
        query = "UPDATE users SET first_name=%(fn)s, last_name=%(ln)s, email=%(em)s, updated_at=NOW() WHERE id = %(id)s;"
        data = {
            "fn": request.form['first_nameE'],
            "ln": request.form['last_nameE'],
            "em": request.form['email_E'],
            'id': int(id3)
        }
        mysql.query_db(query, data)
        return redirect('/myaccount/success')
    else:
        return render_template('edit.html')
    
@app.route("/myaccount/success")
def success():
    return render_template('success.html')

@app.route("/delete/<id4>")
def delete(id4):
    mysql = connectToMySQL('quote_dash')
    query = "DELETE FROM quotes WHERE id = %(id)s;"
    data = {
        'id': int(id4)
    }
    mysql.query_db(query, data)
    return redirect("/quotes")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)