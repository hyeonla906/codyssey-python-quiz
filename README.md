# 게임 상식 퀴즈

Python으로 만든 콘솔 퀴즈 게임. 언차티드, 툼 레이더, 갓 오브 워 등 익숙한 게임을 주제로 선택.

## 수행 체크리스트

- [x] 기본 퀴즈 5개, 메뉴 5개
- [x] `Quiz`, `QuizGame` 클래스 사용
- [x] 퀴즈 풀기·추가·목록·최고 점수·종료
- [x] 빈칸·문자·범위 밖 숫자 입력 처리
- [x] `state.json` 저장·불러오기, 파일 오류 처리
- [x] Git 커밋 10개 이상, 브랜치 병합, clone·push·pull 실습

## 1. 환경 및 실행

| 항목 | 내용 |
|---|---|
| 환경 | Windows / PowerShell / VS Code |
| 언어 | Python 3.10 이상 / 표준 라이브러리 |
| 버전 관리 | Git / GitHub |

```powershell
git clone https://github.com/hyeonla906/codyssey-python-quiz.git
cd codyssey-python-quiz
python main.py
```

**메뉴:** `1` 퀴즈 풀기 / `2` 퀴즈 추가 / `3` 목록 / `4` 최고 점수 / `5` 종료.

## 2. 기능 및 실행 확인

| 항목 | 확인 내용 | 실행 화면 |
|---|---|---|
| 퀴즈 추가 | 문제·선택지 4개·정답 번호 입력 | <a href="docs/screenshots/add_quiz.png"><img src="docs/screenshots/add_quiz.png" width="260"></a> |
| 퀴즈 목록 | 기본 5문제 및 추가한 문제 확인 | <a href="docs/screenshots/list.png"><img src="docs/screenshots/list.png" width="260"></a> |
| JSON 저장 | 퀴즈 추가 후 `state.json` 저장 | <a href="docs/screenshots/json_save.png"><img src="docs/screenshots/json_save.png" width="260"></a> |
| 재실행·최고 점수 | 종료 후 다시 실행해 점수 유지 확인 | <a href="docs/screenshots/restart.png"><img src="docs/screenshots/restart.png" width="260"></a> |
| JSON 오류 | 손상된 파일 처리, 기본 퀴즈 복구 확인 | <a href="docs/screenshots/json_recovery.png"><img src="docs/screenshots/json_recovery.png" width="260"></a> |

**입력 처리:** 공백·빈칸·문자·범위 밖 숫자는 다시 입력. `Ctrl+C`·`EOFError`는 종료 처리.

## 3. JSON 데이터

`state.json`에 퀴즈와 최고 점수 저장. 파일이 없으면 기본 5문제 생성. 손상된 파일은 기본 데이터로 복구.

**저장 형식 예시:**

```json
{
  "quizzes": [
    {
      "question": "언차티드 시리즈의 주인공은?",
      "choices": ["네이선 드레이크", "조엘", "크레토스", "레온"],
      "answer": 1
    }
  ],
  "best_score": 100
}
```

`state.json`은 실행 중 생성되는 파일로 Git 업로드 제외.

## 4. Git / GitHub

| 확인 항목 | 실행 화면 |
|---|---|
| Git 커밋 기록 | <a href="docs/screenshots/git_log.png"><img src="docs/screenshots/git_log.png" width="260"></a> |
| 기능 브랜치 병합 | <a href="docs/screenshots/git_merge.png"><img src="docs/screenshots/git_merge.png" width="260"></a> |
| Git 사용자 설정 | <a href="docs/screenshots/git_config.png"><img src="docs/screenshots/git_config.png" width="260"></a> |

**실습:** `git init`, `add`, `commit`, `checkout`, `merge`, `push`, `clone`, `pull`.

## 5. 파일 구성

```text
main.py                메뉴·입력 처리·실행
quiz.py                Quiz 클래스
quiz_game.py           QuizGame 클래스·JSON 저장
state.json             실행 시 생성되는 저장 파일 (Git 제외)
docs/screenshots/      실행 및 Git 증거 사진
README.md              실습 정리
```
