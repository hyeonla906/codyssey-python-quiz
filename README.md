# 게임 퀴즈

Python 콘솔 퀴즈 게임. 평소 좋아하는 언차티드, 툼 레이더, 갓 오브 워 등을 주제로 선택.

## 수행 체크리스트

- [x] 기본 퀴즈 5개, 메뉴 5개
- [x] `Quiz`, `QuizGame` 클래스 분리
- [x] 퀴즈 풀기·추가·목록·최고 점수·종료
- [x] 빈 입력·문자·범위 밖 숫자 처리
- [x] `state.json` 저장·불러오기, 오류 복구
- [x] Git 커밋 10개 이상, 브랜치 병합, clone·push·pull 실습

## 1. 환경 및 실행

| 항목 | 확인 |
|---|---|
| 개발 환경 | Windows / PowerShell / VS Code |
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
| 환경 | Python·Git·브랜치 확인 | <a href="docs/screenshots/environment.png"><img src="docs/screenshots/environment.png" width="260"></a> |
| 메뉴 | 1~5번 메뉴 출력 | <a href="docs/screenshots/menu.png"><img src="docs/screenshots/menu.png" width="260"></a> |
| 퀴즈 풀기 | 정답 판정·결과 확인 | <a href="docs/screenshots/play.png"><img src="docs/screenshots/play.png" width="260"></a> |
| 퀴즈 추가 | 문제·선택지 4개·정답 입력 | <a href="docs/screenshots/add_quiz.png"><img src="docs/screenshots/add_quiz.png" width="260"></a> |
| 퀴즈 목록 | 기본 5문제·추가 문제 확인 | <a href="docs/screenshots/list.png"><img src="docs/screenshots/list.png" width="260"></a> |
| 최고 점수 | 저장된 최고 점수 확인 | <a href="docs/screenshots/score.png"><img src="docs/screenshots/score.png" width="260"></a> |
| JSON 저장 | 새 문제 등록 후 저장 | <a href="docs/screenshots/json_save.png"><img src="docs/screenshots/json_save.png" width="260"></a> |
| 재실행 | 종료 후 데이터 유지 확인 | <a href="docs/screenshots/restart.png"><img src="docs/screenshots/restart.png" width="260"></a> |
| 파일 오류 | JSON 손상 후 기본 퀴즈 복구 | <a href="docs/screenshots/json_recovery.png"><img src="docs/screenshots/json_recovery.png" width="260"></a> |

| 안전 종료 | Ctrl+C 입력 시 저장 및 종료 확인 | <img src="docs/screenshots/safe_exit.png" width="260"> |

**입력 처리:** 공백 제거·빈칸·문자·범위 밖 숫자 재입력. `Ctrl+C`, `EOFError` 발생 시 가능한 데이터 저장 후 종료.

## 3. JSON 저장

프로젝트 루트 `state.json`에 퀴즈와 최고 점수 저장(UTF-8). 파일 없을 때 기본 5문제 생성, 손상 시 기본 데이터로 복구.

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

`quizzes`: 문제 목록 / `question`: 문제 / `choices`: 보기 4개 / `answer`: 정답 번호 / `best_score`: 최고 점수.

**확인:** `state.json`은 실행 시 생성. `.gitignore`로 Git 업로드 제외.


## 4. Git / GitHub

| 확인 항목 | 실행 화면 |
|---|---|
| Git 커밋 기록 | <img src="docs/screenshots/git_log.png" width="260"> |
| 기능 브랜치 병합 | <img src="docs/screenshots/git_merge.png" width="260"> |
| Git 사용자 설정 | <img src="docs/screenshots/git_config.png" width="260"> |
| 저장소 복제 | <img src="docs/screenshots/git_clone.png" width="260"> |
| Git pull | <img src="docs/screenshots/git_pull.png" width="260"> |

**실습:** `git init`, `add`, `commit`, `checkout`, `merge`, `push`, `clone`, `pull`.


## 5. 파일 구성

```text
main.py               메뉴·입력 처리·안전 종료
quiz.py               Quiz 클래스
quiz_game.py          QuizGame 클래스·JSON 저장
state.json            실행 시 생성되는 저장 파일 (Git 제외)
docs/screenshots/     실행 및 Git 증거 사진
README.md             실습 정리
```
