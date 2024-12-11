from flask import render_template
from flask import request
from . import events
from logger import logger

@events.route('/')
def events_view():
    logger.debug('events handler request')
    return 'events works'


@events.route('/add', methods= ['GET'])
def add_event_view():
    logger.debug('add_event handler request')
    return render_template('add_event.html')


@events.route('/add/submit', methods= ['POST'])
def add_event_submit_view():
    logger.debug('new event submited')
    logger.debug(request.form.to_dict())
    event_name = request.form.get('name')
    description = request.form.get('description')


    return 'submited'
