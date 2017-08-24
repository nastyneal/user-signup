from flask import Flask, request, redirect, render_template
import cgi

app= Flask(__name__)
app.config['DEBUG'] = True

def check_valid( item ):
    message = ''
    if len(item)<3 or len(item)>20 or ' ' in item:
        message="This must be between 3-20 characters and have no spaces"
        #print message
    return message
def email_check(email):
    message = check_valid (email)
    if '@' not in email or '.' not in email: message = "Must contain @ and ."
    if email.count('@')==1 or email.count ('.')==1: message == "Not a valid email"
        #print message
    return message

@app.route("/", methods=["Post", "GET"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        verify_password = request.form["verify_password"]
        email = re4quest_form['email']

        username_error=check_valid(username)
        password_error=check_valid(password)
        verify_password_error=""
        email_error=""

        if password!=verify_password:
            verify_password_error="Password and verify password do not match"
        if len(email)>0: email_check(email)
        if not username_error and not password_error and not verify_password_error:
            return render_template('welcome.html', user=username)



    return render_template("index.html", user_name = username,password = password,
    verify_password = verify_password, email = email, username_error = username_error, password_error = password_error, email_error =email_error)
    return render_template('index.html')

app.run()
