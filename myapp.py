from flask import Flask
application = Flask(__name__)


@application.route('/')
def hello():
    return "This is a test file"


if __name__ == '__main__':
    application.run(host='0.0.0.0')
