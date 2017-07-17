
#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2
import jinja2
import os 
import urllib2
import json

jinja_environment = jinja2.Environment(
	loader = jinja2.FileSystemLoader(
		os.path.dirname(__file__)))
class SignupHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('signup.html')
        self.response.write(template.render())
 
    
class HomeHandler(webapp2.RequestHandler):
    def post(self):  

        name_from_form = self.request.get('parent')
        page_from_form=self.request.get('parentAge')
        page_from_form= int(page_from_form)
        job_from_form= self.request.get('pJob')

        kamount_from_form = self.request.get('children')
        kage_from_form=self.request.get('kAge')
        kage_from_form= int(kage_from_form)
                
        template = jinja_environment.get_template('homepage.html')

        self.response.write(template.render(
            {
              'name': name_from_form,
              'parentAge':page_from_form,
              'pJob':job_from_form,
              'kAmount':kamount_from_form,
              'pAge':page_from_form,
              'kAge':kage_from_form,
              
            }
            ))


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
    ('/baby', BabyHandler),
    ('/signup',SignupHandler),
    ('/home', HomeHandler )
], debug=True)
