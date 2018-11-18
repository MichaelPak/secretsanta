import os


REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.environ.get('REDIS_PORT', 6379))
REDIS_DB = int(os.environ.get('REDIS_DB', 0))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USERS_FILE_NAME = os.environ.get('USERS_FILE_NAME', 'users.yml')
USERS_FILE_PATH = os.path.join(BASE_DIR, USERS_FILE_NAME)

