from flask import render_template, request
from logger import  logger
from . import auth


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
    logger.debug(f'data from registration request {request.form.to_dict()}')
    return 'submitted'


@auth.route('/login/submit', methods= ['POST'])
def login_submit_view():
    logger.debug('login submit view request')
    logger.debug(f'data from login request {request.form.to_dict()}')
    return 'logined'



