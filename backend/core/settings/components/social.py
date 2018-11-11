SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']
SOCIAL_AUTH_RAISE_EXCEPTIONS = True
RAISE_EXCEPTIONS = True

SOCIAL_AUTH_VK_OAUTH2_KEY = 'id_app'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'secret_key'
SOCIAL_AUTH_VK_OAUTH2_SCOPE = [
  'notify',
  'friends',
  'email',
]


AUTHENTICATION_BACKENDS = (
    'social_core.backends.vk.VKOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'social_core.pipeline.social_auth.associate_by_email',
)
