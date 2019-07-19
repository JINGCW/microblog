from flask import request
# from flask_cors import CORS
from flask_login import login_required
from flask_restplus import Api, Resource

from app import create_app, db, cli
from app.models import User, Post, Message, Notification, Task

app = create_app()
# CORS(app, supports_credentials=True)
cli.register(app)
# initialize API
api = Api(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Message': Message,
            'Notification': Notification, 'Task': Task}


@api.route('/barline')
class GraphBarLine(Resource):
    # @login_required
    def post(self):
        end_date = request.args.get('end')
        return {'end_date': end_date}

    @login_required
    def get(self):
        return 'leave'


if __name__ == '__main__':
    # print(app.url_map)
    app.run(debug=True, host='0.0.0.0', port=8080)
