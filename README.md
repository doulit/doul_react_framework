# doul_react_framework

## 주소
    http://ec2-54-180-118-173.ap-northeast-2.compute.amazonaws.com/

## 구성

* 파이썬 3.7+
* 장고 2.2+
* 리액트 16+

## 서버설정 참고
    리액트_서버구동
    nginx 
        -> https://codechacha.com/ko/deploy-react-with-nginx/

    Django 서버구동
    uwsgi 
        -> https://brownbears.tistory.com/16
        -> https://wayhome25.github.io/django/2018/03/04/django-deploy-04-uwsgi/
        
        
        uwsgi --http :8000 --module backend.wsgi

        uwsgi --http :8000 --home ~/.pyenv/versions/mysite-env --chdir /home/ubuntu/doul_react_framework/backend -w mysite.wsgi
### Model 수정
    python manage.py makemigrations 
    python manage.py migrate

### python 가상(venv)
    python -m venv venv
    윈도우
    venv\Scripts\activate
    리눅스
    source venv/bin/activate

    deactivate

### 리눅스
    #sudo apt-get install libmysqlclient-dev
    sudo apt-get install python-pip python3.8-dev libmysqlclient-dev libssl-dev
    sudo pip3 install mysqlclient
### 윈도우 mysqlclient 설치
    https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient
    이곳에서 자신의 python 버전(cp), 파이썬 비트(win)에 맞는 mysqlclient를 다운로드 받는다.

    (venv) C:\Users\temp\Downloads> pip install {다운 받은 whl 파일 이름}    
### 맥북 mysqlclient 에러시(ssl에러시)
    sudo env LDFLAGS="-I/usr/local/opt/openssl@1.1/include -L/usr/local/opt/openssl@1.1/lib" pip install mysqlclient


