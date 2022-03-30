#!/usr/bin/env python

import bottle
import sqlite3

# https://bottlepy.org/docs/dev/recipes.html#ignore-trailing-slashes
@bottle.hook('before_request')
def strip_path():
	bottle.request.environ['PATH_INFO'] = bottle.request.environ['PATH_INFO'].rstrip("/")

@bottle.route("/static/<filepath:path>")
def server_static(filepath):
	return bottle.static_file(filepath, root="./static/")

# https://bottlepy.org/docs/dev/tutorial.html#templates
# https://bottlepy.org/docs/dev/tutorial.html#plugins
# https://github.com/chucknado/bottle_heroku_tutorial

def make_post(author="Someone", body=""):
	con.execute("INSERT INTO posts (author, body) VALUES (?, ?)", (author, body))

def delete_post(postId):
	con.execute("DELETE FROM posts WHERE id = ?", (str(postId),))

@bottle.route("/")
def index():
	s = ""
	
	posts = con.execute("SELECT * FROM posts").fetchall()
	for post in posts:
		p = { 'id': post[0], 'author': post[1], 'body': post[2] }
		s += bottle.template("post.tpl", **p)
	if len(posts) == 0:
		s = "<p>No posts.</p>"
	
	s += bottle.template("compose.tpl")
	
	return bottle.template("main.tpl", {
		'title': "Google Global Home page I forgot",
		'content': s
	})

@bottle.post("/api/make_post")
def index():
	postAuthor = bottle.request.forms.get("name")
	postBody = bottle.request.forms.get("body")
	
	if postAuthor is None or postBody is None \
	or postAuthor == "" or postBody == "":
		return "fission mailed"
	
	make_post(postAuthor, postBody)

@bottle.post("/api/delete_post")
def index():
	postId = bottle.request.forms.get("id")
	
	if postId is None:
		return "fission mailed"
	
	delete_post(postId)

if __name__ == "__main__":
	con = sqlite3.connect("hewwo.db")
	
	con.executescript("""
		CREATE TABLE IF NOT EXISTS posts (
			id INTEGER PRIMARY KEY,
			author TEXT,
			body TEXT
		)
	""")
	
	bottle.run(host="localhost", port=8000, debug=True)
	con.commit()
	con.close()
