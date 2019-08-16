from flask import Flask
import json

app = Flask(__name__)


@app.route('/api/hello', methods=['GET'])
def start():
    return json.dumps(
        {
            'code': 0,
            'data': 'Hello!',
        }
    )


if __name__ == '__main__':
    app.run()
