e621.py API written by @nathan.glades

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