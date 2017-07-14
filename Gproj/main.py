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
import logging

from google.appengine.ext import ndb

jinja_enviroment = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))

# class Skill(ndb.model):
# 	skill = ndb.StringProperty()
# 	skill_description = ndb.StringProperty()

# class Job_Position(ndb.model):
# 	job_Position = ndb.StringProperty()
# 	job_description = ndb.StringProperty()


# class Education(ndb.model):
# 	degree = ndb.StringProperty()
# 	School = ndb.StringProperty()


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
  		professional_profile =self.request.get('professionalprofile')
  		skill_name = self.request.get('skillname')
  		skill_description = self.request.get('skill')
  		job_position = self.request.get('jobposition')
  		jp_description =self.request.get('jobposition_description')
  		education_entry = self.request.get('educationentry')

  		

  		template =jinja_enviroment.get_template('finishedresume.html')
  		self.response.write(template.render(
  			{
  			'name': name,
  			'jobtitle': job_title,
  			'email': email,
  			'phonenumber': phone_number,
  			'personalwebsite': personal_websitelink,
  			'professionalprofile': professional_profile,
  			'skillname': skill_name,
  			'skill': skill_description,
  			'jobposition': job_position,
  			'jobposition_description': jp_description,
  			'educationentry': education_entry,
  			}))

  		


  		 

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/resume', ResumeHandler)
], debug=True)
