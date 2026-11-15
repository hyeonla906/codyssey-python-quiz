# 게임 상식 퀴즈

Python으로 만든 터미널 퀴즈 게임. 퀴즈 풀기·추가·목록·최고 점수 확인·종료 기능 구현.

- **주제:** 언차티드, 툼 레이더, 갓 오브 워, 더 라스트 오브 어스
- **선정 이유:** 익숙한 게임 문제로 Python 문법과 프로그램 흐름 학습
- **저장 방식:** JSON 파일에 문제와 최고 점수 저장, 재실행 시 불러오기

## 목차

1. [환경 및 실행](#1-환경-및-실행)
2. [파일과 클래스](#2-파일과-클래스)
3. [기본 기능](#3-기본-기능)
4. [입력 오류 및 종료](#4-입력-오류-및-종료)
5. [JSON 저장 및 복구](#5-json-저장-및-복구)
6. [Git 실습](#6-git-실습)

## 1. 환경 및 실행

| 항목 | 내용 |
|---|---|
| 작업 환경 | Windows / PowerShell / VS Code |
| 언어 | Python 3 |
| 표준 라이브러리 | json, pathlib |
| 버전 관리 | Git / GitHub |

처음 내려받아 실행:

    git clone https://github.com/hyeonla906/codyssey-python-quiz.git
    cd codyssey-python-quiz
    py main.py

이미 내려받았다면 프로젝트 폴더에서 실행:

    py main.py

환경 및 문법 확인:

    py --version
    git --version
    py -m py_compile main.py quiz.py quiz_game.py

문법 검사에 문제가 없으면 오류 메시지 없이 종료.

## 2. 파일과 클래스

| 파일 | 역할 |
|---|---|
| [main.py](main.py) | 메뉴 출력, 숫자 입력 확인, 기능 연결, 종료 |
| [quiz.py](quiz.py) | 문제 하나의 내용·보기·정답 관리 |
| [quiz_game.py](quiz_game.py) | 기본 문제 5개, 출제·추가·목록·점수·파일 저장 |
| state.json | 문제 목록과 최고 점수 저장. 실행 시 생성, Git 업로드 제외 |
| .gitignore | 업로드에서 제외할 파일 지정 |
| docs/screenshots/ | 실행 및 Git 실습 증거 사진 |

- **Quiz:** 문제 하나를 관리. show()로 문제 출력, is_correct()로 정답 확인.
- **QuizGame:** 여러 문제와 게임 진행 관리. __init__()에서 초기 설정 후 저장 데이터 불러오기.
- **main.py:** QuizGame 객체를 만들고 사용자가 선택한 기능 실행.

제작 순서: 문제 클래스 → 기본 문제 등록 → 메뉴와 입력 처리 → 출제와 점수 계산 → 문제 추가와 목록 → JSON 저장과 복구.

## 3. 기본 기능

    1. 퀴즈 풀기
    2. 퀴즈 추가
    3. 퀴즈 목록
    4. 점수 확인
    5. 종료

| 메뉴 | 동작 | 관련 코드 |
|---|---|---|
| 1. 퀴즈 풀기 | 등록된 모든 문제를 순서대로 출제, 정답 확인 및 점수 계산 | play() |
| 2. 퀴즈 추가 | 문제·보기 4개·정답 번호 입력 후 저장 | add_quiz() |
| 3. 퀴즈 목록 | 등록된 문제 수와 문제 제목 출력 | show_list() |
| 4. 점수 확인 | 최고 점수 표시. 플레이 전에는 안내 문구 출력 | main() |
| 5. 종료 | 데이터를 저장하고 프로그램 종료 | main(), save_data() |

### 퀴즈 풀기와 점수

문제 출력 → 1~4 중 정답 번호 입력 → 정답 비교 → 맞힌 개수 누적 → 점수 계산 및 저장.

    score = correct * 100 // total

맞힌 개수를 전체 문제 수에 대한 100점 기준 점수로 계산. 소수점 아래는 버림.
예: 5문제 중 4문제를 맞히면 80점. 등록된 문제가 없으면 안내 후 메뉴로 복귀.

이번 점수가 기존 최고 점수보다 높으면 최고 점수 갱신.

### 퀴즈 추가와 목록

문제·보기 4개·정답 번호 입력 → 새 Quiz 객체 생성 → 문제 목록에 추가 → JSON 저장.

빈 문제나 빈 보기는 다시 입력. 목록에서는 반복문으로 문제 번호와 제목 출력.

## 4. 입력 오류 및 종료

| 상황 | 처리 |
|---|---|
| 입력 앞뒤 공백 | strip()으로 제거 |
| 빈칸 입력 | 안내 후 재입력 |
| 숫자 대신 문자 입력 | int() 변환 오류를 try/except로 처리 |
| 허용 범위 밖 숫자 | 범위 안내 후 재입력 |
| 문제나 보기 내용이 빈칸 | 내용 입력 요청 |
| Ctrl+C 또는 입력 중단 | finally에서 저장 시도 후 종료 안내 |

숫자는 read_number(message, minimum, maximum)에서 확인.
메뉴는 1~5, 정답은 1~4 범위로 제한.

## 5. JSON 저장 및 복구

- 위치: quiz_game.py와 같은 폴더의 state.json
- 인코딩: UTF-8
- json.dump(): Python 데이터를 JSON 파일에 저장
- json.load(): JSON 파일을 읽어 Python 데이터로 변환
- 저장 내용: quizzes(문제 목록), best_score(최고 점수)
- 파일이 없으면 기본 문제 5개와 초기 점수로 시작
- 파일이 손상되었거나 필수 데이터 형식이 잘못되면 안내 후 기본 데이터로 복구하고 저장
- 저장 실패 시 오류 안내
- state.json은 개인 실행 데이터이므로 Git 업로드 제외

데이터 구조 예시:

    {
      "quizzes": [
        {
          "question": "언차티드 시리즈의 주인공은 누구일까요?",
          "choices": ["네이선 드레이크", "조엘", "크레토스", "레온"],
          "answer": 1
        }
      ],
      "best_score": 80
    }

아직 퀴즈를 풀지 않았으면 최고 점수는 null로 저장.

파일 확인:

    Get-Content ./state.json -Encoding UTF8

확인 순서:

1. 퀴즈를 풀고 메뉴 4번에서 최고 점수 확인.
2. 퀴즈를 추가한 뒤 메뉴 3번에서 목록 확인.
3. 종료 후 다시 실행하여 추가 문제와 최고 점수 유지 확인.
4. JSON 파일에서 문제 목록과 점수 저장 내용 확인.

## 6. Git 실습

기능별 커밋, 브랜치 생성·병합, 저장소 복제와 변경 내용 가져오기 실습.

| 명령어 | 사용 목적 |
|---|---|
| git init | 로컬 저장소 시작 |
| git add README.md | 커밋할 변경 선택 |
| git commit -m "설명" | 변경 내용 기록 |
| git push origin main | GitHub에 업로드 |
| git pull origin main | 원격 변경 내용 가져오기 |
| git checkout main | main 브랜치로 이동 |
| git clone 저장소주소 | 저장소 복제 |

브랜치 실습:

    git switch -c practice
    # 파일을 수정한 다음 실행
    git add README.md
    git commit -m "Update README"
    git switch main
    git merge practice

커밋 수와 기록 확인:

    git rev-list --count HEAD
    git log --oneline --graph --all
    git remote -v
    git status

기존 Git 실습 증거:

- [브랜치 생성과 이동](docs/screenshots/git_checkout.png)
- [브랜치 병합](docs/screenshots/git_merge.png)
- [커밋 기록](docs/screenshots/git_log.png)
- [저장소 복제](docs/screenshots/git_clone.png)
- [복제 폴더에서 수정 및 업로드](docs/screenshots/git_clone_push.png)
- [원래 폴더에서 pull 확인](docs/screenshots/git_pull_verified.png)

GitHub: https://github.com/hyeonla906/codyssey-python-quiz
