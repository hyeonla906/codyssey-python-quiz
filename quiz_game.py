
from quiz import Quiz


class QuizGame:
    def __init__(self):
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

    def show_list(self):
        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
            return

        print(f"\n등록된 퀴즈: {len(self.quizzes)}개")

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"{number}. {quiz.question}")
