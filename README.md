e621.py API written by @nathan.glades

**Functions**
  Files:
    download(self, path): Downloads the files
  Post:
    from_json(self, j_string): Creates post class from
      id            Post ID
      tags          Post Tags
      artist        Post Artist
      description   Post Description
      created_at    Time post was created at
        epoch       Time in epoch
        year        Year post was created
        month       Month post was created
        day         Day post was created
        hours       Hour post was created
        minutes     Minuet post was created
        seconds     Second post was created
        formatted   Date and time formatted as '%Y-%m-%d %H:%M:%S'
      creator_id    Post creator ID
      source        Source of the image
      sauce         Sauce of the image
      score         Score of the post
      fav_count     Number of favourites
      file          File of the post
        url         Url of the file
      has_comments  Does the post have comments
      thumbnail     URL of the post thumbnail
      status        Status of the post
      raw_json      Raw JSON data of the post
      file_type     Type of the post file
  Search:
    search(self, tags):
      posts         List of posts from result (type Post)
      query         Tags
      url           URL of the query
    Index:          Data of the index with no query
      posts         List of posts from result (type Post)
      