
import webapp2
import jinja2
import os 
import urllib2
import json

jinja_environment = jinja2.Environment(
	loader = jinja2.FileSystemLoader(
		os.path.dirname(__file__)))


class BabyHandler(webapp2.RequestHandler):
	def get(self):
		response = urllib2.urlopen('https://randomuser.me/api/?results=10')
		content = response.read()
		content_dictionary = json.loads(content)
		template = jinja_environment.get_template('BSFv3.html')
		self.response.out.write(template.render( {
			'contents' : content_dictionary
		}))



app = webapp2.WSGIApplication([
    ('/baby', BabyHandler)
], debug=True)
