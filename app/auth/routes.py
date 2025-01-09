from app.security.hashing import hash_password
from sqlalchemy import select
from flask import render_template, request, redirect
from flask import session as flask_session
from logger import  logger
from . import auth
from app.models import User, session
from sqlalchemy.exc import IntegrityError



@auth.route('/registration')
def registration_view():
    logger.debug('Registration handler request')
    return render_template('registration.html')



@auth.route('/login')
def login_view():
    logger.debug('Login handler request')
    return render_template('login.html')



@auth.route('/registration/submit', methods= ['POST'])
def registration_submit_view():
    logger.debug('registration submit view request')
    data = request.form.to_dict()
    logger.debug(f'data from registration request {data}')
    for i in data.values():
        if i == '':
            return 'error, fill up required fields'
    user = User(username= request.form.get('username'),
                email= request.form.get('email'),
                password= hash_password(request.form.get('password')))
    try:
        session.add(user)
        session.commit()
    except IntegrityError as e:
        logger.debug(f'error not uniq data entered:{e}')
        return 'error not uniq data entered'
    return 'submitted'


@auth.route('/login/submit', methods= ['POST'])
def login_submit_view():
    logger.debug('login submit view request')
    logger.debug(f'data from login request {request.form.to_dict()}')
    username = request.form.get('username')
    password = request.form.get('password')
    hashed_password = hash_password(password)
    logger.debug(f'hashed password {hashed_password}')
    query = select(User).where(User.username == username, User.password == hashed_password)
    result = session.execute(query).scalar_one_or_none()
    if result:
        flask_session['user_id'] = result.id
        logger.debug(f'User {username} authenticated successfully')
        return redirect('/events')
    else:
        logger.debug('authentication failed')
        return 'Auth failed'




