from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='helpyou'

urlpatterns = [
    path('', views.index),  # 첫 화면(메인페이지)
    path('signup/', views.signup, name='signup'), # 회원가입
    path('login/', auth_views.LoginView.as_view(template_name='helpyou/login.html'), name='login'), # 로그인
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), # 로그아웃
    # path('category/{self.categorybig}/{self.categorysmall}', views.category_page),  # 카테고리/과일/사과
    #path('category/<str:categorybig>/<str:categorysmall>/<int:pk>/', views.ProductDetail.as_view()), # 카테고리/사과/과일/pk번호
    #path('cart/<int:pk>/', views.Cart.as_view()),                   # 장바구니
    #path('payment/<int:pk>/', views.Payment.as_view()),         # 결제
    # path('mypage/', views.MyPage.as_view()),           # 마이페이지
]