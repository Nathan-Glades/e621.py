e621.py API written by @nathan.glades

**WARNING ABOUT THIS CURRENT VERSION**
The API is broken, currently, because e621 seems to have changed the way their website behaves. I'm currently working on a fix. However the following classes/functions do not work
* Search class
  * self.results
* Post class
  * self.score
  * self.rating
  * self.sources

The user agent will also need to be changed, because they seem to have blocked the one I was using. In order to change the user agent, you can modify line 22, and line 87 to
```Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36```


    Search:
    e621.search([tags], [pagenumber]):
        self.results(): Returns list of dicts containg the thumbnail, id, score, user, and comments
    
    Post:
    e621.post([postid]):
        self.image(): Link to fullsize image
        self.download(): Saves image to disk
        self.tags(): Returns dict of tags
        self.score(): Returns score of post
        self.rating(): Returns rating of post
        self.sources(): Returns sources of post
        self.general(): Returns general tags
        self.copyright(): Reutnr copyright tags
        self.characters(): Returns character tags
        self.artists(): Returns artist tags


Still to come:
* Comments
  * Comment text
  * Comment score
  * Comment profile picture
* User profile
  * Avatar
  * Posts
  * Comments
