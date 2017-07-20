
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
import logging


from google.appengine.ext import ndb





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
        income_from_form=self.request.get('money')
        income_from_form= int(income_from_form)
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
              'money':income_from_form,
              

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



# class Resume (ndb.Model):

#     resumetitle =ndb.StringProperty()
#     name = ndb.StringProperty()
#     jobtitle = ndb.StringProperty()
#     email = ndb.StringProperty()
#     phonenumber = StringProperty()
#     personalwebsitelink = StringProperty()
#     professionalprofile = StringProperty()

#     skillentrys = ListProperty()
#     pastjobs = ListProperty()
#     degrees = ListProperty()


class ResumeHandler(webapp2.RequestHandler):
    """docstring for ResumeHandler"""
    def get(self):

        

        template = jinja_environment.get_template('startresume.html')
        self.response.write(template.render())

    def post(self):

        # resume_model = Resume(
        #     resumetitle=resumetitle, 
        #     name=name, 
        #     jobtitle=capjob_title, 
        #     email=email, 
        #     phonenumber=phone_number,
        #     personalwebsitelink=personal_websitelink,
        #     skillentrys=skillentrys,
        #     pastjobs=jobentrys,
        #     degrees=degree_entrys,
        #     )

        # resumetitle = self.request.get('resumetitle')


        name = self.request.get('name')

        job_title = self.request.get('jobtitle')

        capname = name.upper()
        job_title = self.request.get('jobtitle')
        capjob_title = job_title.upper()

 
        email = self.request.get('email')
        phone_number = self.request.get('phonenumber')
        personal_websitelink = self.request.get('personalwebsite')
        professional_profile =self.request.get('professionalprofile')
        skill_name = self.request.get('skillname')
        skill_description = self.request.get('skill')
        job_position = self.request.get('jobposition')
        jp_description =self.request.get('jobposition_description')
        education_entry = self.request.get('educationentry')




        # skillentrys =[]
        skillnames = []
        skilldes = []
        num = 0 
        while True:

            next_skill_name = self.request.get('skillname%r' % num, default_value = -1)
            next_skill_description = self.request.get('skill%r' % num, default_value = -1)
            if next_skill_name == -1 or next_skill_description == -1:
                break
            skillnames.append(next_skill_name)
            skilldes.append(next_skill_description)
            num += 1

        # jobentrys =[]
        pastjobs = []
        pastjobdes = []
        num2 = 0 
        while True:
            next_job_position = self.request.get('jobposition%r' % num2, default_value = -1)
            next_jp_description = self.request.get('des%r' %num2, default_value = -1)
            if next_job_position == -1 or next_jp_description == -1:
                break
            pastjobs.append(next_job_position)
            pastjobdes.append(next_jp_description)
            num2 += 1

        # degree_entrys = []
        degrees = []
        schools = []
        num3 = 0 
        while True:
            next_degree_ = self.request.get('degree%r' %num3, default_value = -1)
            next_school = self.request.get('school%r' %num3, default_value = -1)
            if next_degree_ == -1 or next_school == -1:
                break
            degrees.append(next_degree_)
            schools.append(next_school)
            num3 += 1


        

        template =jinja_environment.get_template('finishedresume.html')
        self.response.write(template.render(
            {
            'name': capname,
            'jobtitle': capjob_title,

            'email': email,
            'phonenumber': phone_number,
            'personalwebsite': personal_websitelink,
            'professionalprofile': professional_profile,

            'skillname': skill_name,
            'skill': skill_description,
            'jobposition': job_position,
            'jobposition_description': jp_description,
            'educationentry': education_entry,



            'skillnames': skillnames,
            'skilldes': skilldes,

            'pastjobs': pastjobs,
            'pastjobdes': pastjobdes,

            'degrees': degrees,
            'schools': schools

            }))




app = webapp2.WSGIApplication([

    ('/baby', BabyHandler),

    ('/',SignupHandler),
    ('/home', HomeHandler ),

    ('/resume',ResumeHandler),


], debug=True)
