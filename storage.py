import redis
import yaml

import settings

USER_KEY = 'user'
NOT_IN_GAME = 'not_in_game'
IN_GAME = 'in_game'
PRESENCE = 'presence'


r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB)


def load():
    with open(settings.USERS_FILE_PATH, 'r') as stream:
        users = yaml.load(stream)

    for u in users:
        r.set('{}:{}'.format(USER_KEY, u['name']), u['pass'])
        r.lpush(NOT_IN_GAME, u['name'])
        r.lpush(PRESENCE, u['name'])
