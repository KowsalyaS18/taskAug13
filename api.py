import json
import flask
from flask import request,jsonify
import pandas as pd


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['POST'])
def api():
    ip=request.get_json()
    print(ip)
    df=get_working_df()
    res = filter(df,ip)
    result = res.to_json(orient="records")
    parsed = json.loads(result)
    return jsonify(parsed)


def get_working_df():
    df = pd.read_csv('data.csv')
    return df


def filter(df,ip):
    for key, val in ip.items():
        if len(val) != 0:
            df = (df[(df[key] == val[0])])
    return df


if __name__ == '__main__':
    app.run(debug=True)
