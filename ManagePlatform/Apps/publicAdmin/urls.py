from django.urls import path
from . import views

app_name = 'publicAdmin'


urlpatterns = [
    path('11', views.IndexView.as_view(), name='index'),
    # path('tags/', views.TagsManageView.as_view(), name='tags'),
    # path('tags/<int:tag_id>/', views.TagEditView.as_view(), name='tag_edit'),
    # path('hotnews/', views.HotNewsManageView.as_view(), name='hotnews_manage'),
    # path('hotnews/<int:hotnews_id>/', views.HotNewsEditView.as_view(), name='hotnews_edit'),
    # path('hotnews/add/', views.HotNewsAddView.as_view(), name='hotnews_add'),
    # path('tags/<int:tag_id>/news/', views.NewsByTagIdView.as_view(), name='news_by_tagid'),

]