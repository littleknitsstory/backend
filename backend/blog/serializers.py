from rest_framework import serializers

from blog.models import PostModel


class PostSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = PostModel
		fields = (
			'title',
			'slug',
			# 'published',
			'content',
			# 'category',
			# 'tags'
		)
		
		lookup_field = 'slug'
