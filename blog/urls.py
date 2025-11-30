from django.urls import path
import blog.views

urlpatterns = [
    path('', blog.views.index, name='index'),
    path('<article_id>/detail/', blog.views.detail, name='detail'),
    path('<article_id>/update/', blog.views.update, name='update'),
]
