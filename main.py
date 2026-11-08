
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

    while True:
        show_menu()
        choice = read_number("선택: ", 1, 5)

        print(f"[확인] 입력된 번호: {choice}")

        if choice == 1:
            game.play(read_number)

        elif choice == 2:
            game.add_quiz(read_number)

        elif choice == 3:
            print("[확인] 퀴즈 목록 기능 실행")
            game.show_list()
        elif choice == 4:
            if game.best_score is None:
                print("아직 퀴즈를 풀지 않았습니다.")
            else:
                print(f"최고 점수: {game.best_score}점")

        else:
            print("게임 종료")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 안전하게 종료합니다.")
