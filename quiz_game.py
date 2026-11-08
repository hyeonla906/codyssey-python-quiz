
import json
from pathlib import Path
from quiz import Quiz


class QuizGame:
    def __init__(self):
        self.file_path = Path(__file__).resolve().parent / "state.json"

        self.quizzes = [
            Quiz(
                "언차티드 시리즈의 주인공은 누구일까요?",
                ["네이선 드레이크", "조엘", "크레토스", "레온"],
                1
            ),
            Quiz(
                "언차티드에서 네이선의 오랜 친구이자 스승 같은 인물은?",
                ["샘 드레이크", "빅터 설리번", "엘레나 피셔", "클로이 프레이저"],
                2
            ),
            Quiz(
                "툼 레이더 시리즈의 주인공은 누구일까요?",
                ["엘리", "앨로이", "라라 크로프트", "질 발렌타인"],
                3
            ),
            Quiz(
                "갓 오브 워 시리즈의 주인공은 누구일까요?",
                ["아트레우스", "토르", "발두르", "크레토스"],
                4
            ),
            Quiz(
                "더 라스트 오브 어스 1편에서 조엘과 함께 여행하는 소녀는?",
                ["엘리", "애비", "테스", "마를린"],
                1
            )
        ]

        self.best_score = None
        self.load_data()

    def show_list(self):
        print("\n==============================")
        print("          퀴즈 목록")
        print("==============================")

        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
        else:
            print(f"등록된 퀴즈: {len(self.quizzes)}개")

            for number, quiz in enumerate(self.quizzes, start=1):
                print(f"{number}. {quiz.question}")

        input("\n목록을 확인했으면 Enter를 누르세요...")

    def play(self, read_number):
        if len(self.quizzes) == 0:
            print("퀴즈가 없습니다.")
            return

        correct = 0
        total = len(self.quizzes)

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"\n[문제 {number}/{total}]")
            quiz.show()

            answer = read_number("정답 (1~4): ", 1, 4)

            if quiz.is_correct(answer):
                print("정답입니다!")
                correct += 1
            else:
                print(f"오답! 정답은 {quiz.answer}번입니다.")

        score = correct * 100 // total

        print(f"\n최종 점수: {score}점")
        print(f"{total}문제 중 {correct}문제 정답")

        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("새로운 최고 점수!")

        self.save_data()
        input("결과를 확인했으면 Enter를 누르세요...")

    def add_quiz(self, read_number):
        print("\n새로운 퀴즈 추가")

        while True:
            question = input("문제를 입력하세요: ").strip()

            if question:
                break

            print("문제를 입력해야 합니다.")

        choices = []

        for number in range(1, 5):
            while True:
                choice = input(f"선택지 {number}: ").strip()

                if choice:
                    choices.append(choice)
                    break

                print("선택지를 입력해야 합니다.")

        answer = read_number("정답 번호 (1~4): ", 1, 4)

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)

        print("퀴즈가 추가되었습니다!")
        self.save_data()

    def save_data(self):
        data = {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score
        }

        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            print("저장 완료: state.json")

        except OSError as error:
            print(f"저장 실패: {error}")

    def load_data(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            if not isinstance(data["quizzes"], list):
                raise ValueError("퀴즈 목록 형식이 잘못되었습니다.")

            loaded_quizzes = []

            for item in data["quizzes"]:
                question = item["question"]
                choices = item["choices"]
                answer = item["answer"]

                if not isinstance(question, str) or not question.strip():
                    raise ValueError("문제 내용이 잘못되었습니다.")

                if not isinstance(choices, list) or len(choices) != 4:
                    raise ValueError("선택지는 4개여야 합니다.")

                if not all(isinstance(c, str) and c.strip() for c in choices):
                    raise ValueError("선택지 내용이 잘못되었습니다.")

                if type(answer) is not int or not 1 <= answer <= 4:
                    raise ValueError("정답 번호가 잘못되었습니다.")

                loaded_quizzes.append(Quiz(question, choices, answer))

            loaded_score = data["best_score"]

            if loaded_score is not None:
                if type(loaded_score) is not int or not 0 <= loaded_score <= 100:
                    raise ValueError("점수 형식이 잘못되었습니다.")

            self.quizzes = loaded_quizzes
            self.best_score = loaded_score

            print(f"저장된 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개)")

        except FileNotFoundError:
            print("저장 파일이 없어 기본 퀴즈를 사용합니다.")
            self.save_data()

        except (OSError, ValueError, KeyError, TypeError, IndexError) as error:
            print(f"파일 읽기 오류: {error}")
            print("기본 퀴즈 5개로 복구합니다.")
            self.save_data()
