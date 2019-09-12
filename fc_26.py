# 백업 프로그램

# 공개 유틸리티인 zip을 이용하여 작업 폴더(디렉토리)를 날짜와 시간정보를 담은 압축파일로 백업하는 프로그램 제작해보기

# 백업할 파일과 디렉토리들은 리스트의 형태로 지정해 둔다.
# 주 백업 디렉토리를 두고, 백업은 그 안에 저장되어야 한다.
# 백업된 파일들은 zip파일로 압축해 둔다.
# zip 파일의 이름은 현재 날짜와 시간으로 한다.
# 커맨드 명령으로 사용되며, 기본으로 제공되는 zip명령을 이용한다. (참고: 명령줄 인터페이스에서 사용할 수 있는 어떤 압축 유틸이던지 사용가능)

# 백업이 필요한 디렉토리 
    # C:\Projects\fs_26\

# 백업 파일 이름
    # 20190912030405.zip
    # 연도(4)+월(2)+일(2)+시(2)+분(2)+초(2).7z
# 백업 파일을 둘 디렉토리
    # C:\Projects\fs_26backup

# 7z 명령
    # 7z a -r C:\Projects\fs_26backup\20190912030405.zip "C:\Projects\fs_26"

'''
SW 개발 단계

1. 무엇을 만들 것인가? (분석 단계)
2. 어떻게 만들 것인가? (설계 단계)
3. 만들기 (구현 단계)
4. 테스트 (테스트 및 디버깅 단계)
5. 실제로 사용하기 (활용 또는 배포 단계)
6. 유지 및 보수 (개선 단계)
'''

import os # Windows system의 명령어를 사용하기 위해 os
import time # 시간을 알기 위해 time

# 윈도우 OS 기준으로 프로그램
source = ['C:\\Projects\\fs_26']  # 역슬래시는 기본적으로 두번 써줄것, 뒷면의 문자와 결합해 다른 결과가 나올 수 있기 때문
target_dir = 'C:\\Projects\\fs_26backup'

# os.sep 는 "\\" 이고, '%Y%m%d%H%M%S'는 '연도+월+일+시간+분+초'
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
# print(target)         # target 테스트

# 만약 백업파일을 저장할 디렉토리가 없다면 디렉토리를 만든다.
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 명령창(cmd) 에서 7z 명령을 수행하기 위한 문자열
# -r 은 하위 디렉토리까지 포함하는 옵션

zip_command = "7z a -r {0} {1}" .format(target, ' '.join(source))

# 백업을 수행
print("Zip command is:")
print(zip_command)
print("Running:")

if os.system(zip_command)==0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')