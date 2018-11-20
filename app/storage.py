import redis
import yaml

from app import settings

USER_KEY = 'user'
NOT_IN_GAME = 'not_in_game'
IN_GAME = 'in_game'
REF_KEY = 'ref'
PRESENCE = 'presence'


r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)


def load():
    with open(settings.USERS_FILE_PATH, 'r') as stream:
        users = yaml.load(stream)

    for u in users:
        r.set('{}:{}'.format(USER_KEY, u['name']), u['pass'])
        r.sadd(NOT_IN_GAME, u['name'])
        r.sadd(PRESENCE, u['name'])


def check_password(login, password):
    return password == str(r.get('{}:{}'.format(USER_KEY, login)))


def get_user(login):
    if r.sismember(NOT_IN_GAME, login):
        r.srem(NOT_IN_GAME, login)

        user = r.srandmember(PRESENCE)
        r.srem(PRESENCE, user)

        r.set('{}:{}'.format(REF_KEY, login), user)
        r.sadd(IN_GAME, login)
        return user
    elif r.exists('{}:{}'.format(REF_KEY, login)):
        user = r.get('{}:{}'.format(REF_KEY, login))
        return user
    else:
        raise RuntimeError('Something going wrong...')


def in_game_list():
    users = r.smembers(IN_GAME)
    return users
