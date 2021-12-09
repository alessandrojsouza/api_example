from django.urls import path

from app.views import todo_list, todo_post, todo_byId, todo_del, todo_update


urlpatterns = [
    path('', todo_list),
    path('add', todo_post),
    path('task/<int:id>', todo_byId),
    path('del/<int:id>', todo_del),
    path('update/<int:id>', todo_update)
]