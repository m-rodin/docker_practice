from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    if 'IN_DOCKER' in os.environ:
        return '\n\nHello, World! Run in docker\n\n\n'

    return '\n\nHello, World!\n\n\n'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
