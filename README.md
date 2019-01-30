설치방법
--------

1. chromedriver (http://chromedriver.chromium.org/downloads) 설치

2. 콩체크 로그인용 환경변수 설정
   - KONG_USERNAME
   - KONG_PASSWORD

3. (Google Cloud Storage 이용시) 환경변수 설정
   - GOOGLE_APPLICATION_CREDENTIALS

실행방법
--------

1. gen_attendance() 를 실행하면 attend.png 로 스크린샷이 떨어짐
2. upload_cloud_storage() 를 실행하면 /autokong/attend.png 로 public object 가 생성됨

