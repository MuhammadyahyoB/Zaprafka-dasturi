from django.urls import path
from . import views

urlpatterns = [
    # >>>>>>>>>>>>> Category list detail create <<<<<<<<
    path('category-list/', views.CategoryApiViewlist.as_view()),
    path('category-detail/<int:pk>/', views.CategoryApiViewDetail.as_view()),
    path('category-create/', views.CategoryApiViewCreate.as_view()),

    # >>>>>>>>>>>>> Yoqilgituri list detail create <<<<<<<<
    path('yoqilgituri-list/', views.YoqilgituriApiViewlist.as_view()),
    path('yoqilgituri-detail/<int:pk>/', views.YoqilgituriAppViewDetail.as_view()),
    path('yoqilgituri-create/', views.YoqilgituriAppViewCreate.as_view()),

    # >>>>>>>>>>>>> Zaprafka list detail create <<<<<<<<
    path('zaprafka-list/', views.ZaprafkaAppViewList.as_view()),
    path('zaprafka-detail/<int:pk>/', views.ZaprafkaAppViewDetail.as_view()),
    path('zaprafka-create/', views.ZaprafkaAppViewCreate.as_view()),
]
