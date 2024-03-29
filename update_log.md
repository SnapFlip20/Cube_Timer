# 시험판
* 0.0.0(2021/3/18)
    * 메인 화면 크기 설정
    * (임시)로고 이미지 제작
    * 타이머 설정(시작, 정지, 초기화 버튼 추가)
* 0.0.1(2021/4/2)
    * 타이머를 스페이스 바로 작동시키게끔 변경
    * 타이머 설명문 추가
    * 스크램블 박스 추가
    * 자동 스크램블 생성기(/scr.genScramble.py) 추가
    * 생성된 스크램블로 섞었을 시 큐브 윗면의 이미지를 반환하는 파일(/scr.showScrambleImg.py) 추가
    * 큐브 이미지 파일(/image) 추가
    * 몇몇 예외 처리 추가
* 0.0.2(2021/4/3)
    * 파일 /scr.genScramble.py 와 /scr.showScrambleImg.py 을 Cube_Timer.py에서 사용할 수 있게끔 적용
* 0.0.3(2021/4/3)
    * 버전을 변경할 때 메인 윈도우의 title과 배치 파일 push.bat에 있는 버전명도 함께 변경되도록 수정
* 0.0.4(2021/4/7)
    * 큐브 섞는 기준을 "윗면:흰색 앞면:빨간색" 에서 "윗면:흰색 앞면:초록색" 으로 변경
    * 스크램블 생성/표시 부분을 함수로 분리
    * 스크램블 새로고침 버튼 추가
    * 타이머를 멈췄을 때 스크램블도 자동으로 새로고침되도록 변경
* 0.0.5(2021/4/7)
    * 측정된 기록을 record.cbtm 파일에 저장되도록 구현
* 0.0.7(2021/4/10)
    * 최근 기록을 표시해주는 load_record 함수 추가
    * 기록 수정하기 버튼 추가
    * 도움말 버튼 추가
* 0.0.8(2021/4/11)
    * 기록 수정하기 버튼에 세부 메뉴 추가

# 정식판
* 0.1.0(2021/4/14)
    * 최근 기록 표시해주는 부분에서 최근 기록이 맨 위에 표시되게 수정
    * 최근 5회 평균 표시
    * 최근 12회 평균 표시
    * 최고 기록 표시
    * 최근 1회 기록 삭제 기능 추가
    * 최근 12회 기록 삭제 기능 추가
    * 모든 기록 삭제 기능 추가
    * mainWindow.after 값을 10에서 1로 변경
* 0.1.1(2021/5/2)
    * 코드 정리(불필요한 주석 제거 등)
    * 여러 함수를 실행시켜주는 bundle1 함수 추가
* 0.1.2(2022/5/11)
    * 글시체를 '나눔고딕'에서 '맑은 고딕'으로 변경(임시)
    * 메인 화면에 표시되는 텍스트들의 위치 약간 수정
* 0.1.3(2022/10/12)
    * 평균 5회, 평균 12회 계산 방식 수정
    * 전체 평균 표시
* 0.1.4(2022/10/13)
    * 약간의 버그 수정, 코드 정리
* 0.1.5(2022/10/13)
    * DNF 처리 기능 추가
    * 설정, 통계 버튼 추가, 버튼 위치 변경
* 0.1.7(2022/10/15)
    * 일부 알림 메세지가 팝업으로 뜨도록 수정
    * 기록 측정 시작/종료 시 타이머 텍스트 색상 변경
    * 시간 단위를 변환해 주는 time_converter 함수 추가
    * 도움말 내용 추가
    * '텍스트 파일로 저장' 버튼 기능 임시 삭제
* 0.2.0(2022/11/19)
    * record.cbtm의 DB 구조를 수정한 recordDB.cbtm 추가(test)
    * 측정된 기록을 새로운 구조로 저장하는 record_new 함수 추가
    * time_converter 함수 적용(화면에 표시되는 모든 기록이 mm:ss.ms 꼴로 표시되게 수정)
* 0.2.1(2022/11/20)
    * 일부 오류 수정
    * 메인 화면에 표시되는 텍스트들의 위치 약간 수정
    * recordDB.cbtm의 저장 방식 변경
* 0.2.3(2022/11/20)
    * 2초 페널티 추가 여부를 기록하는 isP.cbtm 추가(test)
    * penalty_add 함수 추가
    * recordDB.cbtm, isP.cbtm 임시적으로 적용
* 0.2.5(2022/11/21)
    * recordDB.cbtm, isP.cbtm 최종 적용
* 0.2.5.1(2022/11/22)
    * 일부 오류 수정, 디버깅 기록 삭제
    * 2초 페널티 추가 기능 구현
* 0.2.6(2022/11/24)
    * 불필요한 코드 삭제, 정리
* 0.2.7(2022/11/25)
    * 최근 기록 목록에서 2초 페널티가 추가된 기록 옆에 (+2s) 문자가 표시되도록 수정
* 0.2.8(2022/12/25)
    * 통계 버튼 삭제
    * 텍스트 파일로 저장 기능 구현
* 0.3.0(2023/1/10)
    * 설정 버튼 삭제
    * 예외 처리 기능 수정
    * 일부 label 레이아웃 변경
    * 로고 변경
* 0.3.1(2023/1/12)
    * 아이콘 이미지 추가
    * 불필요한 코드 삭제
    * 단축키 기능 추가
    * 타이머가 실행되고 있는 도중에 기록 수정을 할 수 없도록 변경
* 0.3.1a(2023/6/23)
    * 데이터 파일 record.cbtm, recordDB.cbtm 통합
* 0.3.1b(2023/6/26)
    * 데이터 파일 isP.cbtm, recordDB.cbtm 통합
    * 타이머가 실행되고 있는 도중에 스크램블을 변경할 수 없도록 변경
* 0.3.2(2023/6/27)
    * 코드 정리, 불필요한 주석 제거
* 0.3.3(2023/12/25)
    * 특정 환경에서 타이머를 오랫동안 실행시켰을 때 처리 속도가 심각하게 느려지는 문제 해결
    * 도움말 화면을 팝업 형태로 변경
    * 코드 주석 전체적으로 수정