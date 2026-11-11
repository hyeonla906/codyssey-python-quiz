# 게임 상식 퀴즈

Python으로 만든 터미널 퀴즈 게임.

- **주제:** 언차티드, 툼 레이더, 갓 오브 워, 더 라스트 오브 어스
- **선정 이유:** 익숙한 게임을 주제로 선택. Python 기능 학습에 집중
- **구현 내용:** 퀴즈 풀기·추가·목록·점수 확인·종료, 보너스 기능 5개

## 수행 체크리스트

- [x] 기본 퀴즈 5개
- [x] `Quiz`, `QuizGame` 클래스 2개 사용
- [x] 퀴즈 풀기·추가·목록·최고 점수·종료
- [x] 빈칸·문자·범위 밖 숫자 입력 처리
- [x] `state.json` 저장·불러오기·파일 오류 처리
- [x] Git 커밋 10개 이상, 브랜치 병합, clone·pull·push
- [x] 보너스: 랜덤 출제·문제 수 선택·힌트·삭제·플레이 기록

## 1. 개발 환경과 실행

| 항목 | 사용 환경 |
|---|---|
| 운영체제 / 터미널 | Windows / PowerShell |
| 작성 도구 | VS Code |
| 언어 | Python 3.10 이상 |
| 사용 모듈 | `json`, `random`, `datetime`, `pathlib` |
| 버전 관리 | Git / GitHub |

**처음 다운로드해서 실행**

```powershell
git clone https://github.com/hyeonla906/codyssey-python-quiz.git
cd codyssey-python-quiz
py --version
py main.py
```

- `git clone`: GitHub 저장소 복사
- `cd`: 프로젝트 폴더 이동
- `py --version`: Python 버전 확인
- `py main.py`: 퀴즈 게임 실행

**Python 문법 검사**

```powershell
py -m py_compile .\main.py .\quiz.py .\quiz_game.py
```

오류 메시지가 없으면 문법 검사 통과. 실제 기능은 프로그램 실행으로 별도 확인.

<img src="docs/screenshots/environment.png" width="340" alt="개발 환경 확인">

## 2. 코드 파일과 역할

| 파일 | 작업 내용 |
|---|---|
| [main.py](main.py) | 메뉴 출력, 입력 확인, 기능 선택, 종료 처리 |
| [quiz.py](quiz.py) | `Quiz` 클래스: 문제 1개의 내용·보기·정답·힌트 |
| [quiz_game.py](quiz_game.py) | `QuizGame` 클래스: 게임 진행·문제 관리·점수·저장 |

**전체 실행 순서**

1. `main.py`에서 `QuizGame()` 생성
2. `load_data()`로 저장된 문제와 점수 확인
3. 메뉴에서 실행할 기능 선택
4. 선택한 번호에 맞는 함수 실행
5. 문제 추가·삭제·게임 종료 시 데이터 저장

**왜 클래스를 2개로 나눴나?**

- `Quiz`: 퀴즈 문제 한 장을 관리
- `QuizGame`: 여러 문제를 관리하고 게임을 진행
- `main.py`: 메뉴와 사용자 입력 담당

문제 관리와 게임 진행을 나누어 기능별로 수정하기 쉽게 구성.

## 3. 메뉴와 기본 기능

```text
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 퀴즈 삭제 (보너스)
6. 종료
```

`main.py`의 `show_menu()`에서 메뉴 출력.

`read_number()`로 입력한 번호 확인 후 선택한 기능 실행.

<img src="docs/screenshots/menu.png" width="320" alt="기본 메뉴 실행 화면">

*사진은 초기 기본 기능 실습 화면. 현재 코드는 퀴즈 삭제 기능 추가로 메뉴 6개 사용.*

### 3-1. 퀴즈 풀기

**작업 과정**

1. 메뉴 1번 선택 → `game.play()` 실행
2. 등록된 문제 개수 확인
3. 풀 문제 수 입력
4. 문제 목록 복사 후 순서 섞기
5. 문제와 보기 4개 출력
6. 정답 번호 입력 후 정답·오답 확인
7. 최종 점수 계산 후 저장

**사용한 함수와 역할**

| 함수 / 코드 | 역할 |
|---|---|
| `play()` | 퀴즈 진행 |
| `len(self.quizzes)` | 등록된 문제 수 확인 |
| `random.shuffle()` | 문제 순서 섞기 |
| `show()` | 문제와 보기 출력 |
| `read_answer()` | 정답 번호 입력 확인 |
| `is_correct()` | 입력한 번호와 정답 비교 |
| `save_data()` | 결과 저장 |

**정답은 어떻게 확인하나?**

`quiz.py`의 `is_correct()` 사용.

```python
def is_correct(self, choice):
    return choice == self.answer
```

- `choice`: 사용자가 입력한 번호
- `self.answer`: 문제에 저장된 정답 번호
- `==`: 두 값이 같은지 비교

두 번호가 같으면 정답, 다르면 오답.

**왜 문제 목록을 복사하나?**

```python
questions = self.quizzes.copy()
random.shuffle(questions)
```

원래 문제 목록은 그대로 두고, 이번 게임에서 사용할 문제 순서만 변경하기 위해 복사.

**실행 확인**

```powershell
py main.py
```

메뉴 1번 → 문제 수 선택 → 답 입력 → 점수 확인.

| 문제 수 선택 | 퀴즈 결과 |
|---|---|
| <img src="docs/screenshots/bonus_count_select.png" width="260" alt="문제 수 선택"> | <img src="docs/screenshots/play.png" width="260" alt="퀴즈 진행 결과"> |

### 3-2. 퀴즈 추가

**작업 과정**

1. 메뉴 2번 → `add_quiz()` 실행
2. 문제 내용 입력
3. `for` 반복문으로 보기 4개 입력
4. 정답 번호 1~4 입력
5. 힌트 입력(선택)
6. 새 `Quiz` 생성 후 목록에 추가
7. `save_data()`로 저장

**새로운 문제는 어떻게 추가하나?**

```python
new_quiz = Quiz(question, choices, answer, hint)
self.quizzes.append(new_quiz)
```

- `Quiz(...)`: 입력한 내용으로 문제 생성
- `.append()`: 만들어진 문제를 목록 마지막에 추가

**왜 정답 번호를 1~4로 제한하나?**

보기는 4개이므로 정답도 1~4 사이에서 선택.

잘못된 번호는 `read_number()`에서 다시 입력받도록 처리.

<img src="docs/screenshots/add_quiz.png" width="360" alt="퀴즈 추가 실행 결과">

### 3-3. 퀴즈 목록

메뉴 3번 → `show_list()` 실행.

- `len()`으로 등록된 문제 수 확인
- `for` 반복문으로 문제 목록 출력
- `enumerate(..., start=1)`로 번호를 1부터 표시
- 문제가 없으면 안내 문구 출력

**왜 `for`를 사용하나?**

등록된 문제가 몇 개든 같은 방식으로 하나씩 출력하기 위해 사용.

<img src="docs/screenshots/list.png" width="360" alt="퀴즈 목록 확인">

### 3-4. 최고 점수

메뉴 4번 → 저장된 `best_score` 출력.

게임 종료 시 현재 점수와 최고 점수 비교.

```python
if self.best_score is None or score > self.best_score:
    self.best_score = score
```

- `None`: 아직 최고 점수가 없는 상태
- `score > self.best_score`: 기존 최고 점수보다 높은지 비교

**왜 점수가 낮아지면 저장하지 않나?**

최고 점수는 가장 높은 기록만 유지하기 위해 사용.

<img src="docs/screenshots/score.png" width="360" alt="최고 점수 확인">

## 4. 입력 오류와 안전 종료

### 입력 오류 처리

`main.py`에서 사용자 입력 확인.

| 코드 | 역할 |
|---|---|
| `.strip()` | 앞뒤 공백 제거 |
| `int()` | 입력한 글자를 숫자로 변환 |
| `try` / `except ValueError` | 숫자로 바꿀 수 없는 입력 처리 |
| `while True` | 올바른 값을 입력할 때까지 반복 |
| `continue` | 잘못 입력하면 다시 입력받기 |
| `return` | 정상 입력값 전달 |

**숫자가 아닌 문자를 입력하면?**

예: `abc`

`int()`로 변환할 수 없으므로 `ValueError` 발생.

`except ValueError`에서 오류를 처리하고 다시 입력받도록 구성.

**빈칸이나 범위를 벗어난 숫자를 입력하면?**

안내 문구 출력 후 다시 입력.

### 안전 종료

`Ctrl+C` 또는 입력 중단 시 오류 메시지 대신 종료 안내 출력.

`finally`에서 `save_data()` 실행.

**왜 `finally`를 사용하나?**

정상 종료뿐 아니라 입력 중단으로 게임이 끝날 때도 가능한 데이터를 저장하기 위해 사용.

<img src="docs/screenshots/safe_exit.png" width="340" alt="안전 종료 확인">

## 5. JSON 저장과 불러오기

**저장 목적**

게임을 껐다가 다시 실행해도 문제·최고 점수·플레이 기록 유지.

- 파일 이름: `state.json`
- 저장 위치: 프로젝트 폴더
- 저장 함수: `save_data()`
- 불러오기 함수: `load_data()`
- 저장 방식: Python 기본 제공 `json` 사용

**사용한 코드**

| 코드 | 역할 |
|---|---|
| `json.dump()` | 데이터를 JSON 파일에 저장 |
| `json.load()` | JSON 파일 내용 불러오기 |
| `encoding="utf-8"` | 한글 저장·읽기 |
| `try` / `except` | 파일 읽기·저장 오류 처리 |

**저장 데이터 예시**

```json
{
  "quizzes": [
    {
      "question": "언차티드의 주인공은?",
      "choices": [
        "네이선 드레이크",
        "조엘",
        "크레토스",
        "레온"
      ],
      "answer": 1,
      "hint": "이름에 드레이크가 포함"
    }
  ],
  "best_score": 80,
  "history": [
    {
      "played_at": "2026-11-11T15:00:00+09:00",
      "score": 80,
      "correct": 4,
      "total": 5,
      "hints_used": 0
    }
  ]
}
```

- `quizzes`: 문제 목록
- `question`: 문제 내용
- `choices`: 보기 4개
- `answer`: 정답 번호
- `hint`: 힌트
- `best_score`: 최고 점수
- `history`: 플레이 기록

**저장 파일이 없다면?**

기본 퀴즈 5개로 시작하고 저장 파일 생성.

**파일이 손상되었다면?**

오류 안내 후 기본 퀴즈로 복구.

**왜 `.gitignore`에 등록했나?**

`state.json`은 실행할 때 생성되는 개인 게임 데이터이므로 GitHub 업로드에서 제외.

**저장 파일 확인**

```powershell
Get-Content .\state.json -Encoding UTF8
```

| JSON 저장 | 재실행 후 데이터 유지 | 파일 오류 복구 |
|---|---|---|
| <img src="docs/screenshots/json_save.png" width="210" alt="JSON 저장"> | <img src="docs/screenshots/restart.png" width="210" alt="재실행 확인"> | <img src="docs/screenshots/json_recovery.png" width="210" alt="JSON 오류 복구"> |

## 6. 보너스 기능 5개

### 6-1. 랜덤 출제

```python
questions = self.quizzes.copy()
random.shuffle(questions)
```

- 원본 문제 목록 복사
- 복사한 목록의 순서를 무작위로 변경
- 게임을 실행할 때마다 문제 순서가 달라질 수 있도록 처리

**왜 `shuffle()`을 사용하나?**

매번 같은 순서로 문제를 푸는 것을 줄이기 위해 사용.

### 6-2. 문제 수 선택

```python
questions = questions[:count]
```

- `len(self.quizzes)`로 전체 문제 수 확인
- `read_number()`로 풀 문제 수 입력
- `[:count]`로 선택한 개수만큼 문제 사용

**왜 `[:count]`를 사용하나?**

전체 문제 중 원하는 개수만 골라서 진행하기 위해 사용.

| 문제 수 선택 | 퀴즈 결과 |
|---|---|
| <img src="docs/screenshots/bonus_count_select.png" width="260" alt="문제 수 선택"> | <img src="docs/screenshots/bonus_count_result.png" width="260" alt="선택한 문제 수로 진행한 결과"> |

### 6-3. 힌트와 점수 감점

- `quiz.py`에 `hint` 추가
- 정답 입력 중 `h` 또는 `H` 입력 시 힌트 표시
- 한 문제당 힌트 1회 사용
- 힌트 사용 횟수 기록
- 힌트 1회당 10점 감점

**점수 계산 코드**

```python
score = max(0, correct * 100 // total - hints_used * 10)
```

- `correct`: 맞힌 문제 수
- `total`: 푼 문제 수
- `//`: 나눈 결과의 소수점 이하 버림
- `hints_used`: 힌트 사용 횟수
- `max(0, ...)`: 점수가 0점보다 낮아지지 않도록 처리

**계산 예시**

4문제 중 3문제 정답 = 75점

힌트 1회 사용 = 10점 감점

최종 점수 = **65점**

**왜 힌트 중복 사용을 막았나?**

같은 문제에서 힌트를 반복 사용하지 않도록 `used_hint`로 확인.

| 힌트 입력 | 힌트 출력 | 감점 결과 |
|---|---|---|
| <img src="docs/screenshots/bonus_hint_prompt.png" width="200" alt="힌트 안내"> | <img src="docs/screenshots/bonus_hint_show.png" width="200" alt="힌트 출력"> | <img src="docs/screenshots/bonus_hint_score.png" width="200" alt="감점 결과"> |

### 6-4. 퀴즈 삭제

**작업 과정**

1. 메뉴 5번 선택
2. 삭제할 문제 번호 입력
3. 선택한 문제 내용 확인
4. `y` 입력 시 삭제, 그 외 입력은 취소
5. 삭제된 목록을 `state.json`에 저장

**삭제 코드**

```python
self.quizzes.pop(number - 1)
```

**왜 `number - 1`을 사용하나?**

- 화면에서 문제 번호는 1부터 시작
- Python 목록의 첫 번째 위치는 0부터 시작
- 번호 차이를 맞추기 위해 1을 빼서 사용

<img src="docs/screenshots/bonus_delete_result.png" width="420" alt="퀴즈 삭제 결과">

### 6-5. 플레이 기록 저장

- `datetime`으로 게임 날짜·시간 기록
- 최종 점수 기록
- 정답 수와 전체 문제 수 기록
- 힌트 사용 횟수 기록
- `history`에 추가 후 JSON 저장

**왜 `history`를 사용하나?**

최고 점수 하나만 저장하는 것과 별도로, 게임을 실행했던 결과를 여러 개 남기기 위해 사용.

**기록 확인 명령어**

```powershell
Get-Content .\state.json -Raw -Encoding UTF8 | ConvertFrom-Json | Select-Object -ExpandProperty history
```

별도의 기록 메뉴는 없으며 JSON 파일에서 확인.

<img src="docs/screenshots/bonus_history_result.png" width="420" alt="플레이 기록 JSON 확인">

## 7. Git / GitHub 작업 기록

**수행 내용**

- Git 커밋 10개 이상
- 기능별 수정 내용 커밋
- 별도 브랜치에서 작업 후 `main`에 병합
- GitHub 저장소 복제
- `push`와 `pull` 확인

**사용한 명령어**

| 명령어 | 역할 |
|---|---|
| `git init` | Git 저장소 시작 |
| `git add` | 기록할 파일 선택 |
| `git commit -m "설명"` | 변경 내용 기록 |
| `git branch` | 브랜치 확인 |
| `git switch` | 브랜치 이동 |
| `git merge` | 브랜치 작업 병합 |
| `git push` | GitHub에 업로드 |
| `git pull` | GitHub 변경 내용 가져오기 |
| `git clone` | 저장소 복제 |

**왜 브랜치를 사용했나?**

기본 `main`과 기능 작업을 구분하고, 작업 내용을 확인한 뒤 합치기 위해 사용.

**Git 상태 및 기록 확인**

```powershell
git status
git branch --show-current
git --no-pager log --oneline --graph --all -15
git remote -v
```

- `git status`: 변경 파일 확인
- `git branch --show-current`: 현재 브랜치 확인
- `git log`: 커밋 기록 확인
- `git remote -v`: 연결된 GitHub 저장소 확인

**실행 사진 — 커밋·병합·설정**

<p>
  <img src="docs/screenshots/git_log.png" width="210" alt="커밋 기록">
  <img src="docs/screenshots/git_merge.png" width="210" alt="브랜치 병합">
  <img src="docs/screenshots/git_config.png" width="210" alt="Git 설정">
</p>

**실행 사진 — 복제·변경 내용 가져오기**

<p>
  <img src="docs/screenshots/git_clone.png" width="260" alt="Git clone">
  <img src="docs/screenshots/git_pull.png" width="260" alt="Git pull">
</p>

- 복제 실습: 별도 폴더에서 README 수정 후 commit·push, 원래 폴더에서 pull로 반영 확인

## 8. 파일 구성

```text
codyssey-python-quiz/
├─ main.py                 메뉴·입력·종료
├─ quiz.py                 문제 1개 관리
├─ quiz_game.py            게임 진행·점수·JSON 저장
├─ state.json              실행 후 생성 (Git 제외)
├─ .gitignore              Git 업로드 제외 파일 설정
├─ README.md               과제 내용 정리
├─ docs/screenshots/       실행·Git 증거 사진
└─ logs/verified/          일부 보너스 작업 기록
```

**저장소:** https://github.com/hyeonla906/codyssey-python-quiz