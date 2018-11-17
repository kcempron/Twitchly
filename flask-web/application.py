import logging
import os
import twitchly_db
import twitch_user

from flask import (Flask, redirect, render_template, request,
                   send_from_directory)

database = twitchly_db.Database()
application = Flask(__name__, static_folder='static')


@application.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('static/css', path)

@application.route('/fonts/<path:path>')
def send_fonts(path):
    return send_from_directory('static/fonts', path)

@application.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)

@application.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('static/img', path)

@application.route('/')
@application.route('/index.html')
def send_index():
    return render_template('index.html')

@application.route('/about.html')
@application.route('/about')
def send_about():
    return render_template('about.html')

@application.route('/contact.html')
@application.route('/contact')
def send_contact():
    return render_template('contact.html')


@application.route('/user.html')
@application.route('/user')
def send_user():
    username = request.args.get("username")
    if username:
        user_id = twitch_user.get_user_id(username)
        user_info = database.get_user_info(user_id)
        return render_template('user-profile.html', username=username, userinfo=user_info)

    return render_template('user-search.html')

@application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    application.run()

