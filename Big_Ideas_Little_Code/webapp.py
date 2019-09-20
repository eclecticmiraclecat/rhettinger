from typing import Dict
from bottle import get, run, post, view, abort
from bottle import response, request, static_file, template
import pubsub
import pubsub as comb
import secrets
import session

secret = 'the life expectancy of a lannister stark or targaryen is short'

User = str
logged_in_users: Dict[bytes, User] = {}

@get('/')
@view('main')
def show_main_page(user=None):
    user = user or get_logged_in_user()
    if user is None:
        return template('login', null=None)
    heading = 'Posts from people you follow'
    posts = pubsub.posts_for_user(user)
    return dict(user=user, posts=posts, heading=heading, comb=comb)

@post('/')
def check_credentials():
    user = request.forms.get('user', '')
    password = request.forms.get('password', '')
    if not pubsub.check_user(user, password):
        return show_main_page()
    token = secrets.token_bytes(32)
    logged_in_users.setdefault(token, user)
    response.set_cookie('token', token, max_age=60, secret=secret)
    return show_main_page(user)

def get_logged_in_user():
    token = request.get_cookie('token', secret=secret)
    if token is not None:
        return logged_in_users.get(token)
    return None

@post('/postmessage')
def post_message():
    user = get_logged_in_user()
    if user is None:
        return template('login', null=None)
    text = request.forms.get('text', '')
    if text:
        pubsub.post_message(user, text)
    return show_main_page(user)

@get('/search')
@view('main')
def show_search():
    user = get_logged_in_user()
    phrase = request.query.get('phrase', '')
    posts = pubsub.search(phrase, limit=10)
    heading = f'Posts matching: {phrase}'
    return dict(user=user, posts=posts, heading=heading, comb=comb)

def verify_user_exists(user):
    user in pubsub.user_info or abort(404, f'Unknown user: {user!r}')

@get('/<user>')
@view('user')
def show_user_page(user):
    verify_user_exists(user)
    return dict(user=user, posts=pubsub.user_posts[user], heading="Recent posts", comb=comb)

@get('/<user>/followers')
@view('follow')
def show_followers(user):
    verify_user_exists(user)
    return dict(
        users = pubsub.followers[user],
        who_does_what = f'Who follows {user}',
        comb = comb,
    )

@get('/<user>/following')
@view('follow')
def show_following(user):
    verify_user_exists(user)
    return dict(
        users = pubsub.following[user],
        who_does_what = f'Who {user} is following',
        comb = comb,
    )

@get('/static/<filename>')
def fetch_static(filename):
    response.set_header('Cache-Control', 'max-age=600')
    return static_file(filename, root='static')

if __name__ == '__main__':
    run(host='localhost', port=8080)
