from quiz_game import QuizGame


def read_number(message, minimum, maximum):
    while True:
        text = input(message).strip()

        if text == "":
            print("빈칸은 입력할 수 없습니다.")
            continue

        try:
            number = int(text)
        except ValueError:
            print("숫자를 입력해 주세요.")
            continue

        if number < minimum or number > maximum:
            print(f"{minimum}~{maximum} 사이의 숫자를 입력하세요.")
            continue

        return number

def read_answer(message):
    while True:
        text = input(message).strip().lower()

        if text == "h":
            return "h"

        if text == "":
            print("빈칸은 입력할 수 없습니다.")
            continue

        try:
            number = int(text)
        except ValueError:
            print("1~4 또는 h를 입력하세요.")
            continue

        if number < 1 or number > 4:
            print("1~4 사이의 숫자를 입력하세요.")
            continue

        return number

def show_menu():
    print("\n==============================")
    print("        게임 상식 퀴즈")
    print("==============================")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")


def main():
    game = QuizGame()

    try:
        while True:
            show_menu()
            choice = read_number("선택: ", 1, 5)

            if choice == 1:
                game.play(read_number, read_answer)

            elif choice == 2:
                game.add_quiz(read_number)

            elif choice == 3:
                game.show_list()

            elif choice == 4:
                if game.best_score is None:
                    print("아직 퀴즈를 풀지 않았습니다.")
                else:
                    print(f"최고 점수: {game.best_score}점")

            else:
                print("게임 종료")
                break

    finally:
        # 정상 종료, Ctrl+C, EOF 입력 중단 시 가능한 데이터 저장
        game.save_data()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 안전하게 종료합니다.")
