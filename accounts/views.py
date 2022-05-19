from django.shortcuts import render

## creating api for google athentication 
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

# class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
#     adapter_class = GoogleOAuth2Adapter
#     callback_url = 'http://127.0.0.1:8000/accounts/google/login/callback/'
#     client_class = OAuth2Client

class GoogleLogin(SocialLoginView): # if you want to use Implicit Grant, use this
    adapter_class = GoogleOAuth2Adapter

# https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=http://127.0.0.1:8000/accounts/google/login/callback/&prompt=consent&response_type=code&client_id=256779612453-jc5jgen5q9jp336npq94mrl3cd9sv128.apps.googleusercontent.com&scope=openid%20email%20profile&access_type=offline
# https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=http://127.0.0.1:8000/accounts/google/login/callback/&prompt=consent&response_type=code&client_id=256779612453-jc5jgen5q9jp336npq94mrl3cd9sv128.apps.googleusercontent.com&scope=openid%20email%20profile&access_type=offline
# https://accounts.google.com/o/oauth2/v2/auth?redirect_uri=http://127.0.0.1:8000/accounts/google/login/callback/&prompt=consent&response_type=token&client_id=256779612453-jc5jgen5q9jp336npq94mrl3cd9sv128.apps.googleusercontent.com&scope=openid%20email%20profile