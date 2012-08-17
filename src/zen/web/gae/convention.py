from zen import router

__author__ = 'renzo'

'''
Created on 02/02/2011

@author: Renzo Nuccitelli
'''

import webapp2

def _get(self,param,default_value=""):
    values=self.request.get_all(param)
    if not values: return default_value
    if len(values)==1: return values[0]
    return values

class Handler(webapp2.RequestHandler):
    def get(self):
        self.make_convention()

    def post(self):
        self.make_convention()

    def put(self):
        self.make_convention()

    def delete(self):
        self.make_convention()

    def make_convention(self):
        instance_handler, method, args = router.to_handler(self.request.path)
        instance_handler.handler=self
        kwargs={a:_get(a) for a in self.request.arguments()}
        method(*args,**kwargs)


app = webapp2.WSGIApplication([("/.*",Handler)], debug = False)

