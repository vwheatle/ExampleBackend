<form action="/api/make_post" method="post" target="resultFrame">
	<ul>
		<li><label for="name">Name:&nbsp;</label><input type="text" name="name" />
		<li><label for="body">Body:&nbsp;</label><textarea name="body"></textarea>
	</ul>
	<input type="submit" value="Post" />
</form>
<iframe name="resultFrame" id="resultFrame" hidden></iframe>
