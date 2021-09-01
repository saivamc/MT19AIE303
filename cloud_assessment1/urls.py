"""cloud_assessment1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from visitors import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('visitors/',views.home),
    path('visitors/viewVisitors', views.show),
    path('visitors/addVisitors', views.addVisitors),
    path('visitors/createVisitor', views.addVisitor),
    path('show',views.home),
    path('visitors/goToHome',views.home),
]

# # Use include() to add paths from the catalog application
# from django.urls import include

# urlpatterns += [
    # path('visitors/', include('visitors.urls')),
    # path('show', views.show),
# ]

# #Add URL maps to redirect the base URL to our application
# from django.views.generic import RedirectView
# urlpatterns += [
    # path('', RedirectView.as_view(url='visitors/', permanent=True)),
    # ]

# # Use static() to add url mapping to serve static files during development (only)
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
