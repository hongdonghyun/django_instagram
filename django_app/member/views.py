from django.contrib.auth import authenticate, login as django_login
from django.http import HttpResponse
from django.shortcuts import render, redirect


def login(request):
    # member/login.html생성
    # username,password,button이 있는 html생성
    # POST요청이 올 경우 로그인 완료 후 post_list이동
    # 실패할 경우 HttpResponse로 Login invalid 띄우기



    if request.method == "POST":
        # 요청받은 POST데이터에서 id,password키가 가진 값들을
        # username,password변수에 할당 (문자열
        username = request.POST['id']
        password = request.POST['password']
        # authenticate함수를 사용해서 User객체를 얻어 user에 할당
        # 인증에 실패할 경우 user변수에는 None할당
        user = authenticate(request, username=username, password=password)
        # user변수가 None이 아닐 경우
        if user is not None:
            # Django의 session을 이용해 이번 request와 user객체를 사용해 로그인 처리
            # 이후의 request/response에서는 사용자가 인증된 상태
            django_login(request, user)
            # 로그인 완료후에는 post_list뷰로 리다이렉트 처리
            return redirect('post_list')
        # user변수가 None일 경우
        else:
            #로그인에 실패했음을 알림
            return HttpResponse("Login invalid")
    #GET요청이 왔을경우 단순 로그인 폼만 보여준다
    else:
        #만약 이미 로그인 된 상태일 경우에는
        #post_list로 redirect
        #아닐경우 login.html을 render해서 리턴
        if request.user.is_authenticated:
            return redirect('post_list')
        return render(request, 'member/login.html')
