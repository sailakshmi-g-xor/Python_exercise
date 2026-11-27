import sys


WINNING_LINES = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


def winner(board):
    for first, second, third in WINNING_LINES:
        mark = board[first]
        if mark != " " and mark == board[second] == board[third]:
            return mark
    return None


def render(board):
    cells = [str(index + 1) if cell == " " else cell for index, cell in enumerate(board)]
    rows = [" " + " | ".join(cells[start : start + 3]) for start in (0, 3, 6)]
    return "\n---+---+---\n".join(rows)


def play(moves):
    board = [" "] * 9
    player = "X"
    messages = []

    for move in moves:
        if winner(board) is not None or " " not in board:
            break

        token = str(move).strip()
        is_integer = token.isdigit() or (
            token[:1] in ("+", "-") and token[1:].isdigit()
        )
        if not is_integer:
            messages.append(f"Invalid move {token}: not a number")
            continue

        cell = int(token)
        if not 1 <= cell <= 9:
            messages.append(f"Invalid move {token}: must be 1-9")
            continue
        if board[cell - 1] != " ":
            messages.append(f"Invalid move {token}: cell taken")
            continue

        board[cell - 1] = player
        if winner(board) is not None:
            break
        if " " not in board:
            break
        player = "O" if player == "X" else "X"

    winning_player = winner(board)
    if winning_player is not None:
        result = f"{winning_player} wins"
    elif " " not in board:
        result = "Draw"
    else:
        result = "Game in progress"
    return board, result, messages


def main():
    board, result, messages = play(line.rstrip("\r\n") for line in sys.stdin)
    for message in messages:
        print(message)
    print(render(board))
    print(result)


if __name__ == "__main__":
    main()