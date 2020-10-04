from django.conf.urls import url
from .views import Post


urlpatterns = [
    url('blog', blogpost, name='blogpost')
]
