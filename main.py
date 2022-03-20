import bottle
import sqlite3

def make_post(author="Someone", body=""):
	con.execute("INSERT INTO posts (author, body) VALUES (?, ?)", (author, body))

# https://bottlepy.org/docs/dev/recipes.html#ignore-trailing-slashes
@bottle.hook('before_request')
def strip_path():
	bottle.request.environ['PATH_INFO'] = bottle.request.environ['PATH_INFO'].rstrip("/")

@bottle.route("/")
def index():
	posts = con.execute("SELECT * FROM posts").fetchall()
	s = """
	<!DOCTYPE html>
	<html>
	<head>
		<meta charset="utf-8" />
		<title>Example Page</title>
	</head>
	<body>
		<h1>Google Web Global Web page</h1>
	"""
	for post in posts:
		s += bottle.template("""
		<div class="post">
			<small>Post #{{postId}} &ndash; {{postAuthor}}</small>
			<p>{{postBody}}</p>
		</div>
		""", postId=post[0], postAuthor=post[1], postBody=post[2])
	if len(posts) == 0:
		s += "<p>No posts.</p>"
	s += """
	</body>
	</html>
	"""
	return s

@bottle.post("/api/make_post")
def index():
	data = bottle.request
	assert "Sorry this isn't complete" == None

# Questionable endpoint.
@bottle.route("/hewwo/<name>")
def index(name):
	return bottle.template("""
	<!DOCTYPE html>
	<html>
	<head>
		<meta charset="utf-8" />
		<title>hewwo {{name}}!!!!!!</title>
	</head>
	<body>
		<h1>OwO</h1>
		<p>haiii {{name}}!! <i>*glomps u*</i></p>
	</body>
	</html>
	""", name=name)

if __name__ == "__main__":
	con = sqlite3.connect("hewwo.db")
	
	con.executescript("""
		CREATE TABLE IF NOT EXISTS posts (
			id INTEGER PRIMARY KEY,
			author TEXT,
			body TEXT
		)
	""")
	
	# make_post("V", "Example Post 1")
	# make_post("V", "Example Post 2")
	
	bottle.run(host="localhost", port=8000)
	con.commit()
	con.close()
