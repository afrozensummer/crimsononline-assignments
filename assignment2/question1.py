import datetime
from PIL import Image
import re
class Content(object):
    '''
        Required properties:
        - title
        - subtitle
        - creator
        - publication date
        Required methods:
        - show
        - matches_url (question 1d)
        '''
    def __init__(self, title, subtitle, creator, publicationdate=datetime.datetime.now()):
        self.title = title
        self.subtitle = subtitle
        self.creator = creator
        self.publicationdate = publicationdate
    
    def show(self):
        print '{0} {1} {2} {3}'.format(self.title, self.subtitle, self.creator, self.publicationdate)
    
    def __str__(self):
        return '<{0}:{1}>'.format(self.__class__.__name__, title)
    
    def matches_url(address):
        s = r'thecrimson.com/(\w+)/(\d{4})/(\d{1,2})/(\d{1,2})/(\w+)'
        m = re.match(s, address)
        if not m:
            return False
        content = m.groups()[1]
        year = int(m.groups()[2])
        month = int(m.groups()[3])
        day = int(m.groups()[4])
        slug = m.groups()[5]
        
        if (year == publicationdate.year && month == publicationdate.month && day == publicationdate.day)
            return true
        return false


class Article(Content):
    '''
        Required properties:
        - All properties of Content
        - related_image
        Required methods:
        - All methods of Content
        '''
    def __init__ (self, headline, teasertext, creator, publicationdate=datetime.datetime.now(), related_image=None):
        super(Article, self).__init__(headline, subtitle, creator, publicationdate)
        self.related_image = related_image
    
    def show(self):
        print '{0}: {1}'.format(self.title, self.subtitle)
        self.related_image.show()

class Picture(Content):
    '''
        Required properties:
        - All properties of Content
        - image_file
        Required methods:
        - All methods of Content
        '''
    def __init__(self, title, caption, creator, image_file, publicationdate=datetime.datetime.now()):
        super(Picture, self).__init__(title, caption, creator, publicationdate)
        self.path = image_file
    
    def show(self):
        print '{0} {1}'.format(self.title, self.subtitle)
        Image.open(self.path).show()


'''
    Question 1e
    '''
def from_url(c_lst, url):
    matches = [content for content in c_lst if content.matches_url(url)]
    if len(matches) != 1:
        raise Exception
    else:
        return matches[0]

'''
    Question 1e
    '''
def posted_after(c_lst, dt):
    return [content for content in c_lst if content.publicationdate > dt]


