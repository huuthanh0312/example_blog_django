from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.index, name="index"),
    path('category/<int:category_id>', views.category, name="category"),
    path('detail/<int:new_id>', views.detail, name="detail"),
    path('search/', views.search, name="search"),
    path('add-all/', views.add, name="add"),
    path('add-news/', views.add_news, name="add_news"),
    path('add-cate/', views.add_cate, name="add_cate"),
    path('admin-cate/<int:category_id>', views.admin_cate, name="admin_cate"),
    path('delete-news/<int:new_id>', views.delete_news, name="delete_news"),
    path('edit-news/<int:new_id>', views.edit_news, name="edit_news"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
