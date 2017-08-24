from flask import Flask, render_template, request
from flask_restful import Resource, Api
import os


app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    return render_template('index.html')


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class DataSet(Resource):
    def post(self):
        param = request.get_json(force=True)
        user = param["user"]
        data = param["data"]
        base_path = os.path.dirname(os.path.realpath(__file__))
        user_dir = os.path.join(base_path, "dataset", user)
        os.makedirs(user_dir, exist_ok=True)
        index = 1
        while True:
            data_file_path = os.path.join(user_dir, str(index)+".log")
            if not os.path.exists(data_file_path):
                break
            index += 1
        with open(data_file_path, "w+") as f:
            f.write(data)


api.add_resource(DataSet, '/dataset')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=False)
