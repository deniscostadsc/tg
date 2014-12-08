from google.appengine.ext import ndb


class Document(ndb.Model):
    text = ndb.StringProperty(required=True)


class Classification(ndb.Model):
    document = ndb.KeyProperty(Document, required=True)
    ip = ndb.StringProperty(required=True)
    value = ndb.FloatProperty(required=True, choices=(0.0, 0.5, 1.0))
