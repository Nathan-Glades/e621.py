# e621.net API written by:
# Discord   :   autoplay5#7704
# Twitter   :   @LostKidWalmart
# Instagram :   @nathan.glades

from urllib.request import Request, urlopen
from urllib.parse import unquote, quote
from urllib.error import HTTPError

class e621:
    class SearchError(Exception):
        def __init__(self, message, errors):

            super(e621.SearchError, self).__init__(message)

            self.errors = errors
    class search:
        def __init__(self, tags, page):
            self.tags = tags
            self.page = page
            self.webaddr = 'https://e621.net/post/index/{}/{}'.format(self.page, self.tags)

            urlheader = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'}

            request = Request(self.webaddr, headers = urlheader)
            try:
                self.urlread = urlopen(request).read().decode('utf-8')
            except HTTPError:
                raise e621.SearchError('403 Forbiden page', '403')
        
        def results_raw(self):
            start = self.urlread.index('value="Cancel">\n\t\t\t</form>\n\t\t</div>\n\n\t\t<div>\n  \n    \n      <span class="')
            end = self.urlread.index('</span>\n    \n  \n</div>\n\n\n\t\t\n\n\t\t<div id="paginator">\n\t\t\t<div class="pagination" use_link_style="true">')

            return self.urlread[start:end]
        
        def results(self):
            if 'No posts matched your search.' in self.urlread:
                return None
            elif self.urlread == None:
                return None
            else:
                r = self.results_raw()
                r = r.split('value="Cancel">\n\t\t\t</form>\n\t\t</div>\n\n\t\t<div>\n  \n    \n      ')[1]

                r = r.split('<span class="thumb"')

                r_final = []

                r.pop(0)

                for x in r:
                    t = {
                        "id": "",
                        "rating": "",
                        "score": "",
                        "user": "",
                        "thumb": ""
                    }
                    t['id'] = x.split(' id="p')[1].split('" onclick="return PostModeMenu.click(event,')[0]
                    info = x.split('\r\r')[1]
                    info = info.split('" width="')[0]
                    info = info.split('\r')

                    t['rating'] = info[0].split('Rating: ')[1].split('\r')[0]
                    t['score'] = info[1].split('Score: ')[1].split('\r')[0]
                    t['user'] = info[2].split('User: ')[1].split('\r')[0]

                    t['tumb'] = 'https://static1.e621.net/data/preview/' + x.split('src="https://static1.e621.net/data/preview/')[1].split('" title="')[0]

                    r_final.append(t)

                return r_final

    class post:
        def __init__(self, id_):
            self.id = id_
            self.webaddr = 'https://e621.net/post/show/' + str(id_)

            urlheader = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'}

            request = Request(self.webaddr, headers = urlheader)

            self.urlread = urlopen(request).read().decode('utf-8')
        
        def image(self):
            in_ = self.urlread.index('\n\t\t\n\t\t\t\n\t\t\t<a href="https://static1.e621.net/data')  + 20
            in_end = self.urlread.index('">Download</a>\n\t\t\t\n\t\t\t\t')

            return self.urlread[in_:in_end]
        
        def download(self):
            img = self.image()
            img_name = img.split('https://static1.e621.net/data')[1].split('/')[3]

            print(img_name)

            img_file = open(img_name, 'wb')
            urlheader = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'}

            request = Request(img, headers = urlheader)
            img_file.write(urlopen(request).read())
        
        def tags(self):
            return {
                "general": self.general(),
                "copyright": self.copyright(),
                "characters": self.characters(),
                "artists": self.artists()
            }
        
        def score(self):
            ssb = self.stats_sidebar()
            sl = ssb.split('</span></li>\n\n\t\t<li>\n\t\t\tScore: <span id="post-score-1695812" style="cursor:help;" class="greentext">')[1]
            sl = sl.split('</span>\n\n\t\t\t\n\n\t\t\t\n\t\t</li>\n\n\t\t')[0]

            return int(sl)

        def rating(self):
            ssb = self.stats_sidebar()
            sl = ssb.split('</li>\n\n\t\t<li>Rating: <span class=\'greentext\'>')[1]
            sl = sl.split('</span></li>\n\n\t\t<li>\n\t\t\tScore: ')[0]

            return sl
        
        def sources(self):
            ssb = self.source_link_raw()

            sl = ssb.split('<div class=\'sourcelink-url\'>\n\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\t<a href="')
            sl.pop(0)

            sl = sl[0].split('" target="_blank" rel="nofollow noreferrer noopener">')

            sl_final = []

            for x in sl:
                if 'href' in x:
                    sl_final.append(x.split('<a href="')[1])
                else:
                    sl_final.append(x)
            
            sl_final.pop(len(sl_final)-1)
            return sl_final
        
        def general(self):
            tar = self.tags_general_raw()
            tar = tar.split('href="/post/search?tags=')

            ret = []

            for x in tar:
                ret.append(unquote(x[:x.index('">')]))
            
            ret.pop(0)
            
            return ret
        
        def copyright(self):
            tar = self.tags_copyright_raw()
            tar = tar.split('href="/wiki/show?title=')

            ret = []

            for x in tar:
                ret.append(unquote(x[:x.index('">')]))
            
            ret.pop(0)
            
            return ret
        
        def characters(self):
            tar = self.tags_characters_raw()
            tar = tar.split('href="/wiki/show?title=')

            ret = []

            for x in tar:
                ret.append(unquote(x[:x.index('">')]))
            
            ret.pop(0)
            
            return ret
        
        def artists(self):
            tar = self.tags_artist_raw()
            tar = tar.split('href="/artist/show?name=')

            ret = []

            for x in tar:
                ret.append(unquote(x[:x.index('">')]))
            
            ret.pop(0)
            
            return ret
        
        def tags_general_raw(self):
            start = self.urlread.index('<li class="tag-type-general">')
            end = self.urlread.index('</li>\n        </ul>\n      </div>\n\n\t\t\t<div id="stats">')

            return self.urlread[start:end]
        
        def tags_copyright_raw(self):
            start = self.urlread.index('<li class="tag-type-copyright">')
            end = self.urlread.index('onclick=\'hideCategory("species")\'>')

            return self.urlread[start:end]
        
        def tags_characters_raw(self):
            start = self.urlread.index('<li class="tag-type-character">')
            end = self.urlread.index('onclick=\'hideCategory("copyright")\'>')

            return self.urlread[start:end]
        
        def tags_artist_raw(self):
            start = self.urlread.index('<li class="tag-type-artist">')
            end = self.urlread.index('onclick=\'hideCategory("species")\'>')

            return self.urlread[start:end]
        
        def stats_sidebar(self):
            start = self.urlread.index('<li class="sourcelink">Source:\n\t\t\t\t<div class=\'sourcelink-url\'>\n\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\t<a ')
            end = self.urlread.index('</span></span></li>\n\t\t\n\t</ul>\n</div>\n\n\t\t\t<div>\n\n</div>\n\n\t\t\t<div>\n')

            return self.urlread[start:end]
        
        def source_link_raw(self):
            sb = self.stats_sidebar()
            sb_start = sb.index('<li class="sourcelink">Source:\n\t\t\t\t<div class=\'sourcelink-url\'>\n\t\t\t\t\t\n\t\t\t\t\t\t\n\t\t\t\t\t\t\t')
            sb_end = sb.index('</a><br>\n\t\t\t\t\t\t\n\t\t\t\t\t\n\t\t\t\t</div>\n\t\t\t')

            return sb[sb_start:sb_end]