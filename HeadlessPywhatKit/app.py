from flask import Flask, request, session, current_app, config,send_file
import requests
from HeadlessPywhatKit.whats import WhatsApp

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/send_message')
def send_message_to_number():
    print(request.args)
    current_app.config['ok'].send_user_message(request.args.get('phone'), request.args.get('message'))
    return 'done'


@app.route('/send_user_image')
def send_user_image():
    current_app.config['ok'].send_image(request.args.get('phone'), request.args.get('filename'))
    return 'done'


@app.route("/send_user_document")
def send_user_document():
    global ok
    current_app.config['ok'].send_document(request.args.get('phone'), filename=request.args.get('filename'))
    return 'done'

@app.route("/login")
def send_login_image():
    app.config['ok'] = WhatsApp()
    return send_file('C:\\Users\\admin\\PycharmProjects\\HeadlessAsyncPywhatKit\\HeadlessPywhatKit\\hello.png')


@app.route('/playonyt')
def playonyt():
    """Will play video on following topic, takes about 10 to 15 seconds to load"""
    topic = request.args.get("topic")
    url = 'https://www.youtube.com/results?q=' + topic
    count = 0
    cont = requests.get(url)
    data = cont.content
    data = str(data)
    lst = data.split('"')
    for i in lst:
        count += 1
        if i == 'WEB_PAGE_TYPE_WATCH':
            break
    if lst[count - 5] == "/results":
        raise Exception("No video found.")

    print("Videos found, opening most recent video")
    WhatsApp().driver.get("https://www.youtube.com" + lst[count - 5])
    return "https://www.youtube.com" + lst[count - 5]


def create_app():
    return app
