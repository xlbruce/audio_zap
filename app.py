from flask import Flask, request
import logging
import os

FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT)
logger = logging.getLogger(__name__)

env_file = '.env'
# Load env vars from file if they exist
if os.path.exists(env_file):
    with open(env_file, 'r') as f:
        line = f.readline()
        while line:
            line = f.readline()
            if line.startswith('#'): continue
            key, value = line.split('=')
            logger.debug(f'Setting [{key}] variable')
            os.environ[key] = value

app = Flask(__name__)
telegram_url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_TOKEN')}"

@app.route("/healthcheck")
def healthcheck():
    return "App is running"

@app.route("/telegram", methods=['POST'])
def telegram():
    logging.debug(f"request content: {request.get_json()}")
    return '{"ok": true}'

