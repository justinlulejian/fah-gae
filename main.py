
"""."""
import flask
import stats
app = flask.Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def hello():
    """Return an HTTP greeting."""
    return 'Hello World!'


# Get all user records available.
@app.route('/fah/api/donatorstats/v1.0/all', methods=['GET'])
def get_all_records():
    all_records = stats.UserDataEntry.query().fetch()
    if len(all_records) == 0:
      flask.abort(404)
    all_records_response = {}
    record_counter = 1
    for record in all_records:
      all_records_response[record_counter] = record.to_dict()
      record_counter += 1
    return flask.jsonify(all_records_response)


# Get all of a specific user's records available.
@app.route(
    '/fah/api/donatorstats/v1.0/donator/<string:donator>',
    methods=['GET'])
def get_all_donator_records(donator):
  all_records = (
      stats.UserDataEntry.query(
          stats.UserDataEntry.username == donator).fetch())
  if len(all_records) == 0:
    flask.abort(404)
  all_records_response = {}
  record_counter = 1
  for record in all_records:
    all_records_response[record_counter] = record.to_dict()
    record_counter += 1
  return flask.jsonify(all_records_response)

# Get only a specified number of a specific user's records.

# Get all of a specific user's records available.
@app.route(
    '/fah/api/donatorstats/v1.0/donator/<string:donator>/<int:num_recs>',
    methods=['GET'])
def get_some_donator_records(donator, num_recs):
  all_records = (
      stats.UserDataEntry.query(
          stats.UserDataEntry.username == donator).fetch(num_recs))
  if len(all_records) == 0:
    flask.abort(404)
  all_records_response = {}
  record_counter = 1
  for record in all_records:
    all_records_response[record_counter] = record.to_dict()
    record_counter += 1
  return flask.jsonify(all_records_response)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return flask.make_response(
        flask.jsonify({'error_message': 'No resource found.'}), 404)
