"""NDB Datastore objects for the F@H Stats API."""

from google.appengine.ext import ndb


class UserDataEntry(ndb.Model):
  """Individual user log taken from the official F@H Stats API."""
  
  entry_date = ndb.DateTimeProperty()  # Time the entry was found/logged.
  username = ndb.StringProperty()
  userid = ndb.IntegerProperty()
  rank = ndb.IntegerProperty()
  wus = ndb.IntegerProperty()
  credit = ndb.IntegerProperty()
  active_7 = ndb.IntegerProperty()
