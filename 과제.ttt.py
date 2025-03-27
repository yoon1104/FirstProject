#게임보드 출력 함수
def print_board(board):
    for r in range(3):
        print(" " + board[r][0] + " | " + board[r][1] + " | " + board[r][2])
        if r != 2:
            print("---|---|---")

#승부확인 함수
def check_winner(board, player):
    # 가로 또는 세로 체크
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    # 대각선 체크
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

# 3x3 게임 보드 생성
board = [[' ' for _ in range(3)] for _ in range(3)]

while True:
    print_board(board)

    # 사용자 입력 받기
    while True:
        try:
            x = int(input("다음 수의 x좌표를 입력하시오 (0~2): "))
            y = int(input("다음 수의 y좌표를 입력하시오 (0~2): "))

            if 0 <= x < 3 and 0 <= y < 3 and board[x][y] == ' ':
                break
            else:
                print("잘못된 위치입니다. 다시 입력하세요.")
        except ValueError:
            print("숫자를 입력하세요!")

    # 사용자의 수를 'X'로 표시
    board[x][y] = 'X'

    # 승리 체크
    if check_winner(board, 'X'):
        print_board(board)
        print("플레이어(X) 승리!")
        break

    # 보드가 가득 찼는지 확인 (무승부)
    if is_full(board):
        print_board(board)
        print("무승부")
        break

    # 컴퓨터가 놓을 위치 찾기 (첫 번째 빈칸에 'O' 놓기)
    done = False
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ' and not done:
                board[i][j] = 'O'
                done = True
                break
        if done:
            break

    # 컴퓨터 승리 체크
    if check_winner(board, 'O'):
        print_board(board)
        print("컴퓨터 승리")
        break

    # 보드가 가득 찼는지 확인 (무승부)
    if is_full(board):
        print_board(board)
        print("무승부")
        break
