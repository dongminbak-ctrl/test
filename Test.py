import random


def play_number_guessing_game() -> None:
    print("숫자 맞추기 게임에 오신 것을 환영합니다!")
    print("1부터 20 사이의 숫자를 맞춰보세요.")

    secret_number = random.randint(1, 20)
    attempts = 0

    while True:
        try:
            guess = int(input("숫자를 입력하세요: ").strip())
        except ValueError:
            print("숫자를 입력해야 합니다.")
            continue

        attempts += 1

        if guess < secret_number:
            print("너무 낮아요!")
        elif guess > secret_number:
            print("너무 높아요!")
        else:
            print(f"정답입니다! {attempts}번 만에 맞췄어요.")
            break


if __name__ == "__main__":
    play_number_guessing_game()
