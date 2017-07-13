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
import os 
import jinja2
import random

jinja_enviroment = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write('Hello world!')

class ResumeHandler(webapp2.RequestHandler):
	"""docstring for ResumeHandler"""
	def get(self):

  		
  		template = jinja_enviroment.get_template('startresume.html')
  		self.response.write(template.render())

  	def post(self):

  		name = self.request.get('name')
  		job_title = self.request.get('jobtitle')
  		email = self.request.get('email')
  		phone_number = self.request.get('phonenumber')
  		personal_websitelink = self.request.get('personalwebsite')



  		template =jinja_enviroment.get_template('finishedresume.html')
  		self.response.write(template.render(
  			{
  			'name': name,
  			'jobtitle': job_title,
  			'email': email,
  			'phonenumber': phone_number,
  			'personalwebsite': personal_websitelink,
  			}))

  		


  		 

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/resume', ResumeHandler)
], debug=True)
