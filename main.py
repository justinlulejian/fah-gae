from flask import abort
from flask import Flask
from flask import jsonify
from flask import make_response
app = Flask(__name__)
app.config['DEBUG'] = True

# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

user_records = [
    {
        'id': 0,
        'time': u'12/15/2016 22:49',
        'username': u'Justin_N_Lulejian',
        'new_credits': 14148979,
        'sum_workunits': 2326,
        'team_num': 0
    },
    {   'id': 1,
        'time': u'12/15/2016 22:49',
        'username': u'DerpdeDerp',
        'new_credits': 9999999,
        'sum_workunits': 9999,
        'team_num': 0
    },
]

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/fah/api/userstats/v1.0/records', methods=['GET'])
def get_all_records():
    return jsonify({'records': user_records})


@app.route('/fah/api/userrecords/v1.0/records/<int:rec_id>', methods=['GET'])
def get_record(rec_id):
    record = [record for record in user_records if record['id'] == rec_id]
    if len(record) == 0:
        abort(404)
    return jsonify({'record': record[0]})

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return make_response(jsonify({}), 404)
