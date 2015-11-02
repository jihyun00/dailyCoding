""" virtualenv에 대한 소개
pyvenv를 이용하여 가상 환경 관리

활성화시키는 방법
ex) tutorial-env/Scripts/activate

가상환경 실행 후, pip을 이용하여 필요한 package 설치 가능
ex) pip install requests==2.6.0

버전 업그레이드 하는 방법
pip install --upgrade requests

pacakge 정보 보기
pip show requests

가상 환경에 설치된 package 보기
pip list

필요한 package들에 대한 정보를 requirements.txt 파일에 넣어둠

pip install -r requirements.txt
명령어를 수행하면 requirements.txt에 있는 패키지 중 
설치되지 않은 패키지를 설치

"""
