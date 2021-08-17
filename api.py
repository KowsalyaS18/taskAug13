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


@app.route('/missing', methods=['GET'])
def missing_val():
    df = pd.read_csv('data.csv')
    percent_missing = df.isnull().sum() * 100 / len(df)
    return percent_missing.to_dict()


@app.route('/nul', methods=['GET'])
def fill_null_val():
    df = pd.read_csv('data.csv')
    res=df.fillna("N/A")
    result=res.to_json(orient="records")
    parsed = json.loads(result)
    return jsonify(parsed)

@app.route('/gpa', methods=['GET'])
def student_filer():
    data = pd.read_csv('student.csv')
    list_=['gpa_sem1', 'gpa_sem2', 'gpa_sem3', 'gpa_sem4', 'gpa_sem5', 'gpa_sem6', 'gpa_sem7', 'gpa_sem8']
    data['max_gpa'] = data[list_].max(axis=1)
    data['max_sem'] = data[['gpa_sem1', 'gpa_sem2', 'gpa_sem3', 'gpa_sem4', 'gpa_sem5', 'gpa_sem6', 'gpa_sem7', 'gpa_sem8']].idxmax(axis=1)
    result=data.to_json(orient="records")
    parsed=json.loads(result)
    return jsonify(parsed)

if __name__ == '__main__':
    app.run(debug=True)
