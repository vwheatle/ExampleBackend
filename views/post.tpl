<div class="post">
	<small class="postInfo"
		><form action="/api/delete_post" method="post" target="resultFrame" class="postDeleteForm"
			><input type="number" name="id" value="{{id}}" hidden
			/><input type="submit" value="x"
		/></form
		><span class="postId">Post #{{id}}</span
		> &ndash; <span class="postAuthor">{{author}}</span
	></small>
	<p class="postBody">{{body}}</p>
</div>
