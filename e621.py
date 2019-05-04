import time, urllib, json
class Main:
    header = 'e621.py/1.0 by AutoPlay5/NathanGlades'
class Time:
    def __init__(self, s):
        self.epoch = int(s)
        self.year = time.strftime('%Y', time.localtime(s))
        self.month = time.strftime('%m', time.localtime(s))
        self.day = time.strftime('%d', time.localtime(s))
        self.hours = time.strftime('%H', time.localtime(s))
        self.minutes = time.strftime('%M', time.localtime(s))
        self.seconds = time.strftime('%S', time.localtime(s))
        self.formatted = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(s))

class Files:
    def __init__(self, url):
        self.url = url
    
    def download(self, path):
        dfurl = urllib.request.Request(self.url, data=None, headers={"User-Agent": Main.header})
        data = urllib.request.urlopen(dfurl).read()
        filename = path + self.url.replace('https://static1.e621.net', '').replace('/', '')
        write_file = open(filename, 'wb')
        write_file.write(data)
        return filename

class Post:
    def __init__(self):
        self.id = ''
        self.tags = []
        self.artist = []
        self.description = ''
        self.created_at = None
        self.creator_id = ''
        self.source = ''
        self.sauce = '' # Same as source
        self.score = 0
        self.fav_count = 0
        self.file = ''
        self.rating = ''
        self.has_comments = False
        self.thumbnail = ''
        self.status = ''
        self.raw_json = None
        self.file_type = ''
    
    def from_json(self, j_string):
        self.id = j_string['id']
        self.tags = j_string['tags'].split(' ')
        self.description = j_string['description']
        self.created_at = Time(j_string['created_at']['s'])
        self.creator_id = j_string['creator_id']
        self.source = j_string['source']
        self.sauce = self.source
        self.score = j_string['score']
        self.fav_count = j_string['fav_count']
        self.file = Files(j_string['file_url'])
        self.rating = j_string['rating']
        self.has_comments = j_string['has_comments']
        self.thumbnail = j_string['preview_url']
        self.status = j_string['status']
        self.raw_json = j_string
        self.artist = j_string['artist']
        self.file_type = j_string['file_ext']

class Search:
    def __init__(self):
        self.posts = []
        self.query = []
        self.url = None
    
    def search(self, tags):
        url = 'http://e621.net/post/index.json?' + urllib.parse.urlencode({'tags': tags})
        self.url = url
        url_request = urllib.request.Request(
            url,
            data = None,
            headers = {
                'User-Agent': Main.header
            }
        )
        f = json.loads(urllib.request.urlopen(url_request).read().decode('utf-8'))
        for i in f:
            if i != None:
                post = Post()
                post.from_json(i)
                self.posts.append(i)
    class Index:
        def __init__(self):
            self.posts = []
            url = 'http://e621.net/post/index.json'
            url_request = urllib.request.Request(
                url,
                data = None,
                headers = {
                    'User-Agent': Main.header
                }
            )
            f = json.loads(urllib.request.urlopen(url_request).read().decode('utf-8'))
            for i in f:
                if i != None:
                    post = Post()
                    post.from_json(i)
                    self.posts.append(i)
        def get_json(self):
            url = 'http://e621.net/post/index.json'
            url_request = urllib.request.Request(
                url,
                data = None,
                headers = {
                    'User-Agent': Main.header
                }
            )
            f = json.loads(urllib.request.urlopen(url_request).read().decode('utf-8'))
            return f