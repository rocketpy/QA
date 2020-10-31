"""
#  for uniques user use module Faker

def registration:
    URL = "ip"
    PARAMS = {'name':'test','password':'test1','primary_email':'test667@gmail.com','primary_mobile_number':'9999999999','country_abbrev':'US'} 
    r = requests.post(url = URL,params = PARAMS,auth=HTTPDigestAuth('user', 'pass')) 
    response = r.text 
    print response
"""
