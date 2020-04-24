# -*- coding: utf-8 -*-

"""
@Author             : Bao
@Date               : 2020/4/24 17:00
@Desc               : 
@Last modified by   : Bao
@Last modified date : 2020/4/24 17:00
"""

import argparse
import logging
import bottle
from urllib.parse import quote
from bottle import request, template, static_file

from src.function import run

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser()
parser.add_argument(
    '--port',
    default=23333,
    type=int,
    help=''
)
parser.add_argument(
    '--web_name',
    default='HTTP Server',
    type=str,
    help=''
)
parser.add_argument(
    '--web_title',
    default='HTTP Server',
    type=str,
    help=''
)
parser.add_argument(
    '--web_desc',
    default='web demo',
    type=str,
    help=''
)
args = parser.parse_args()

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s -   %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.INFO
)

release = True
port = args.port
web_title = args.web_title
web_name = args.web_name
web_desc = args.web_desc
examples = [(x, quote(x)) for x in [
    'example'
]]

logger.info('port: {}'.format(port))
logger.info('web name: {}'.format(web_name))
logger.info('web description: {}'.format(web_desc))

app = bottle.Bottle()
history = []


@app.route('/', method=['GET', 'POST'])
def index():
    global history

    inputs = request.params.inputs
    logging.info('user inputs: {}'.format(inputs))

    if inputs == '':
        history.clear()
        return template('static/index.html', web_title=web_title, web_name=web_name, web_desc=web_desc, exams=examples)

    outputs, history = run(inputs, history)
    logger.info(outputs)
    logger.info(history)
    return template('static/index.html', web_title=web_title, web_name=web_name, web_desc=web_desc, exams=examples,
                    inputs=inputs, outputs=outputs, history=history)


@app.route('/static/<filepath>')
def server_static(filepath):
    return static_file(filepath, root='static/')


bottle.run(app, host='0.0.0.0', port=port, server='tornado')
