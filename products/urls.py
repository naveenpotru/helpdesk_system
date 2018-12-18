from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^api/v1/products/(?P<pk>[0-9]+)$', # urls with details i.e /products/(1-9)
        views.get_delete_update_product,
        name='get_delete_update_product'
    ),
    url(
        r'^api/v1/products/$', # urls list all and create new one
        views.get_post_products,
        name='get_post_products'
    )
]