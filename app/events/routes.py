from flask import render_template
from flask import request
from . import events
from logger import logger
from app.models.event import Event, UserEventAssociation
from app.models import session
from app.models.user import User
from flask import session as flask_session
from sqlalchemy import select



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
    logger.debug(f'new event accepted to add into db{request.form.to_dict()}')
    user_id = flask_session.get('user_id')
    if not user_id:
        return 'you are not authenticated'
    query = select(User).where(User.id == user_id)
    user = session.execute(query).scalar_one_or_none()
    if not user:
        return 'you are not authenticated'
    event = Event(name= request.form.get('name'), description= request.form.get('description'))
    session.add(event)
    session.commit()
    user_event_association = UserEventAssociation(user_id= user.id, event_id= event.id)
    session.add(user_event_association)
    session.commit()
    logger.debug('new event recorded into db')
    return 'event submitted'
