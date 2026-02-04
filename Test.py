import random


CHOICES = ("가위", "바위", "보")


def get_player_choice() -> str:
    while True:
        choice = input("가위/바위/보 중 하나를 입력하세요 (종료: q): ").strip()
        if choice.lower() == "q":
            return "q"
        if choice in CHOICES:
            return choice
        print("입력이 올바르지 않습니다. 다시 입력해 주세요.")


def decide_winner(player: str, computer: str) -> str:
    if player == computer:
        return "draw"
    if (
        (player == "가위" and computer == "보")
        or (player == "바위" and computer == "가위")
        or (player == "보" and computer == "바위")
    ):
        return "player"
    return "computer"


def play_rock_paper_scissors() -> None:
    print("가위바위보 게임에 오신 것을 환영합니다!")
    print("3승을 먼저 달성하면 승리합니다.")

    player_score = 0
    computer_score = 0
    round_number = 1

    while True:
        print(f"\n{round_number}라운드")
        player_choice = get_player_choice()
        if player_choice == "q":
            print("게임을 종료합니다.")
            return

        computer_choice = random.choice(CHOICES)
        print(f"컴퓨터의 선택: {computer_choice}")

        result = decide_winner(player_choice, computer_choice)
        if result == "draw":
            print("무승부입니다!")
        elif result == "player":
            player_score += 1
            print("플레이어 승리!")
        else:
            computer_score += 1
            print("컴퓨터 승리!")

        print(f"현재 점수 - 플레이어: {player_score}, 컴퓨터: {computer_score}")
        if player_score == 3:
            print("축하합니다! 플레이어가 최종 승리했습니다.")
            return
        if computer_score == 3:
            print("아쉽네요. 컴퓨터가 최종 승리했습니다.")
            return

        round_number += 1


if __name__ == "__main__":
    play_rock_paper_scissors()
