import bottle
from bottle import route, run, Response, template
import json
import image
# from flask import Flask
# app = Flask(__name__)

def call_service():
    directoryName = 'photos'
    image.process(directoryName)

@route('/')
def index():
    """Home page"""
    title = "Image Processor App"
    # call_service()
    return template('index.tpl',data="Request completed!", title=title)

if __name__ == '__main__':
	run(host='localhost', port=8000, debug=True, reloader=True)
	
serverApp = bottle.default_app()