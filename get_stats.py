"""Cron for obtaining user stats on an hourly basis."""
import datetime
from google.appengine.api import urlfetch
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import json
import logging
import stats


def retrieve_store_userdata_content(user_data_url, username):
  """Send an HTTP request to F@H API to get updated stats for donator.

  Args:
    user_data_url: A string of URL where the user data is located.
  """
  logging.debug('Retrieving user data for: %s', username)
  user = json.loads(urlfetch.fetch(user_data_url % username).content)
  stats.UserDataEntry(
      username=user['name'], userid=user['id'], rank=user['rank'],
      wus=user['wus'], credit=user['credit'], active_7=user['active_7'],
      entry_date=datetime.datetime.now()).put()


class GetStatsTaskHandler(webapp.RequestHandler):
  """Cron class for getting donator stats."""

  def post(self):
    # TODO(justinlulejian): Remove hardcoding to me.
    username = 'Justin_N_Lulejian'
    retrieve_store_userdata_content(
        'http://folding.stanford.edu/stats/api/donor/%s', username)
    self.response.write('Got stats for %s.', username)

  def get(self):
    # TODO(justinlulejian): Remove hardcoding to me.
    username = 'Justin_N_Lulejian'
    retrieve_store_userdata_content(
        'http://folding.stanford.edu/stats/api/donor/%s', username)
    self.response.write('Got stats for %s.' % username)


application = webapp.WSGIApplication([('/cron/get_stats', GetStatsTaskHandler)],
                                     debug=True)
if __name__ == '__main__':
    run_wsgi_app(application)
