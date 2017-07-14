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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('apphome.html')
        self.response.write(template.render())
 
    def post(self):
        name_from_form = self.request.get('parent')
        page_from_form=self.request.get('parentAge')
        page_from_form= int(page_from_form)
        job_from_form= self.request.get('pJob')

        kamount_from_form = self.request.get('children')
        kage_from_form=self.request.get('kAge')
        kage_from_form= int(kage_from_form)
		        



        student_model = Student(name=name_from_form, grade=grade_from_form)
        student_model.put()

        template = jinja_environment.get_template('apphome.html')
        self.response.write(template.render(
            {
              'name': name_from_form
            }
            ))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
