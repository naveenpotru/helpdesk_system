
from django.contrib import admin
from django.conf.urls import include, url
from .views import RegisterView


# urls
urlpatterns = [
    url(r'^', include('products.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', RegisterView.as_view()),
    url(r'^admin/', admin.site.urls),
]