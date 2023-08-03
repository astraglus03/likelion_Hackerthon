from django.shortcuts import render, redirect
from .forms import UserForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login


# index 페이지 (첫 화면)
def index(request):
    return render(
        request,
        'helpyou/index.html',
    )

@csrf_exempt
# def signup(request):
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         if form.is_valid(): # 유효성 검사. 이 폼이 유효하지 않으면 오류 메시지 저장
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password) # 사용자 인증
#             login(request, user) #로그인
#             return redirect('index')
#         else:
#             form = UserForm()
#         return render(request, 'helpyou/signup.html', {'form':form})
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid(): # 검사
            # 아이디 중복 확인 체크가 되었는지 확인
            if form.cleaned_data['username_check']:
                # 비밀번호와 비밀번호 확인이 일치하는지 확인
                if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                    # 유저 생성
                    user = form.save()
                    return redirect('/')  # 회원가입 성공 시 이동할 URL
                else:
                    form.add_error('password2', '비밀번호가 일치하지 않습니다.')
            else:
                form.add_error('username_check', '아이디 중복 확인해주세요.')
    else: # GET 요청일 경우, 회원가입 화면 리턴
        form = UserForm()

    return render(request, 'helpyou/signup.html', {'form': form})

