from rest_framework import serializers
from .models import Review, Feedback


# class ContactSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Contact
#         fields = (
#             'id',
#             'phone',
#             'email',
#             'created_at'
#         )


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'id',
            'user_name',
            'comment',
            'email',
            'created_at'
        )


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = (
            'id',
            'name',
            'feedback',
            'email',
            'created_at'
        )
