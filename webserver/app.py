# +
from flask import Flask, request, jsonify
import os
import re
import redis
import psycopg2

app = Flask(__name__)


# -

def get_limit(default = 5):
    limit = request.args.get('limit', default)
    try:
        limit = int(limit)
    except ValueError:
        limit = default
    if limit > 10:
        limit = default
    return limit


# +
@app.route('/')
def hello_world():
    if 'IN_DOCKER' in os.environ:
        return '\n\nHello, World! Run in docker\n\n\n'

    return '\n\nHello, World!\n\n\n'

@app.route('/send', methods=['POST'])
def send_message():
    content = request.get_json(silent=True)

    if 'message' in content:
        message = re.sub(r'[^A-Za-z0-9 ]+', '', content['message'])
        
        if message:
            q = redis.Redis(host='redis')
            q.rpush("queue:raw", message)
            app.logger.info("The message was pushed in the queue")
            
            return {"status": "ok"}, 200
        return {
            "status": "failed",
            "error": "message is empty"
        }, 400
            
    return {
        "status": "failed",
        "error": "message not in request"
    }, 400

@app.route('/last', methods=['GET'])
def show_messages():
    limit = get_limit()
    pg = None
    
    try:
        pg = psycopg2.connect(user="docker", password="docker", database="docker", host='db')
        cursor = pg.cursor()
        cursor.execute("select * from messages order by id desc limit %s" % limit)
        rows = cursor.fetchall()
        
        app.logger.info("Returned last messages from the db")
        
        return jsonify([{
            'id': row[0],
            'message': row[1],
            'processed_at': row[2]
        } for row in rows])
    
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)
    finally:
        if pg:
            cursor.close()
            pg.close()


# -

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
