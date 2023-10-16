from django.contrib import admin
from django.urls import path, include
# from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('counter.urls')),
    # path('counter/', include('counter_app.urls')),
]
