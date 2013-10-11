from question1 import *

content_list = ["Hi", "www.google.com"]

#Test for from_url:
print 'TESTING from_url'
url1 = "http://www.google.com"
url2 = "http://www.facebook.com"
url3 = "http://www.thecrimson.com"
c1 = from_url(content_list, url1)
c2 = from_url(content_list, url2)
c3 = from_url(content_list, url3)

print 'CONTENT MATCHING {0}:'.format(url1)
if c1:
    c1.show()
print '\nCONTENT MATCHING {0}:'.format(url2)
if c2:
    c2.show()
print '\nCONTENT MATCHING {0}:'.format(url3)
if c3:
    c3.show()

print '\n'

#Test for posted_after:
print 'TESTING posted_after'
time1 = 2/12/13
time2 = 1/3/12
time3 = 2/2/12

print 'CONTENT POSTED AFTER {0]'.format(time1)
for c in posted_after(content_list, time1):
    c.show()
print '\nCONTENT POSTED AFTER {0]'.format(time2)
for c in posted_after(content_list, time2):
    c.show()
print '\nCONTENT POSTED AFTER {0]'.format(time3)
for c in posted_after(content_list, time3):
    c.show()