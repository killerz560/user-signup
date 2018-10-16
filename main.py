from flask import Flask, request, redirect, render_template
import os
import cgi


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def user_signup():
    return render_template('home_page.html')



# FUNCTIONS FOR VALIDATION

def empty_val(x):
    if x:
        return True
    else:
        return False
    
def char_length(x):
    if len(x) > 2 and len(x) < 21:
        return True
    else:
        return False

def email_at_symbol(x):
    if x.count('@') >= 1:
        return True
    else:
        return False

def multiple_email_at_symbols(x):
    if x.count('@') <= 1:
        return True
    else:
        return False

def email_period(x):
    if x.count('.') >= 1:
        return True
    else:
        return False

def multiple_email_periods(x):
    if x.count('.') <= 1:
        return True
    else:
        return False



# TAKE USER-SIGNUP INFO AND VALIDATE

@app.route("/", methods=['POST'])
def user_signup_validation():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    err_required = "Required field"
    err_reenter_pw = "Please re-enter password"
    err_char_count = "must be between 3 and 20 characters"
    err_no_spaces = "may not contain spaces"

    if not empty_val(password):
        password_error = err_required
        password = ''
        verify = ''
    
    elif not char_length(password):
        password_error = "Password" + err_char_count
        password = ''
        verify = ''
        verify_error = err_reenter_pw

    else:
        if " " in password:
            password_error = "Password"  + err_no_spaces
            password = ''
            verify = ''
            verify_error = err_reenter_pw

   
    if verify != password:
        verify_error = "Passwords must match"
        password = ''
        verify = ''
        password_error = 'Passwords must match'


    if not empty_val(username):
        username_error = err_required
        password = ''
        verify = ''
        password_error = err_reenter_pw
        verify_error = err_reenter_pw

    elif not char_length(username):
        username_error = "Username" + err_char_count
        password = ''
        verify = ''
        password_error = err_reenter_pw

    else:
        if " " in username:
            username_error = "Username" + err_no_spaces
            password = ''
            verify = ''
            password_error = err_reenter_pw
            verify_error = err_reenter_pw

    if empty_val(email):
        if not char_length(email):
            email_error = "Email " + err_char_count
            password = ''
            verify = ''
            password_error = err_reenter_pw
            verify_error = err_reenter_pw
        
        elif not email_at_symbol(email):
            email_error = "Email must contain the @ symbol"
            password = ''
            verify = ''
            password_error = err_reenter_pw
            verify_error = err_reenter_pw
        
        elif not multiple_email_at_symbols(email):
            email_error = "Email must contain only one @ symbol"
            password = ''
            verify = ''
            password_error = err_reenter_pw
            verify_error = err_reenter_pw
        
        elif not email_period(email):
            email_error = "Email must contain ."
            password = ''
            verify = ''
            password_error = err_reenter_pw
            verify_error = err_reenter_pw
        
        elif not multiple_email_periods(email):
            email_error = "Email must contain only one ."
            password = ''
            verify = ''
            password_error = err_reenter_pw
            verify_error = err_reenter_pw
        
        else:
            if " " in email:
                email_error = "Email " + err_no_spaces
                password = ''
                verify = ''
                password_error = err_reenter_pw
                verify_error = err_reenter_pw

    

    if not username_error and not password_error and not verify_error and not email_error:
        username = username
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('home_page.html', username_error=username_error, username=username, password_error=password_error, password=password, verify_error=verify_error, verify=verify, email_error=email_error, email=email)

@app.route('/')
def keep():
    username = request.args.get('username')
    email = request.args.get('email')
    return render_template('home_page.html', username = username, email = email)

@app.route('/welcome')
def valid_signup():
    username = request.args.get('username')
    return render_template('welcome_page.html', username=username)

app.run()
