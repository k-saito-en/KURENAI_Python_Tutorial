# 三目並べ
#
# 特にインポートするモジュールはありません
#
# 定数の定義
#
#
# play() の中で棋譜を作成する (要完成)
#
'三目並べのプログラムです'
OPEN = 0
FIRST = 1
SECOND = 2
DRAW = 3
#
# 恒常的な変数
#
turn = 1
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# テスト用の棋譜
log1 = [[0, 0], [1, 1], [1, 0], [2, 0], [0, 2], [0, 1], [2, 1], [2, 2], [1, 2], [EVEN]]
log2 = [[0, 0], [1, 0], [1, 1], [2, 2], [0, 1], [2, 0], [FIRST]]
log3 = [[0, 1], [0, 0], [2, 1], [1, 1], [2, 2], [2, 0], [1, 0],
        [0, 2], [SECOND]]
#
# 手番関連の関数
#
# 手番を文字列に


def show_turn():
    '手番を示す文字列を返す'
    if turn == FIRST:
        return '先手'
    elif turn == SECOND:
        return '後手'
    else:
        return '手番の値が不適切です'

# 手番の初期化


def init_turn():
    '手番を初期化する'
    global turn
    turn = 1

# 手番の交代


def change_turn():
    '手番を交代する'
    global turn
    if turn == FIRST:
        turn = SECOND
    elif turn == SECOND:
        turn = FIRST

# 手番関連の関数のテスト


def test_turn():
    '手番をテストする'
    init_turn()
    print(show_turn(), "の番です")
    change_turn()
    print(show_turn(), "の番です")
    change_turn()
    print(show_turn(), "の番です")
#
# 盤面関連の関数
#
# 盤面を表示する文字列


def show_board():
    '盤面を表す文字列を返す'
    s = ' :0 1 2\n---------\n'
    for i in range(3):
        s = s + str(i) + ': '
        for j in range(3):
            cell = ''
            if board[i][j] == OPEN:
                cell = ' '
            elif board[i][j] == FIRST:
                cell = 'O'
            elif board[i][j] == SECOND:
                cell = 'X'
            else:
                cell = '?'
            s = s + cell + ' '
        s = s + '\n'
    return s
#
# 盤面の初期化


def init_board():
    '盤面をすべて空(OPEN)に初期化する'
    for i in range(3):
        for j in range(3):
            board[i][j] = OPEN
#
# 盤面の i, j の位置の値を返す


def examine_board(i, j):
    '盤面の i 行 j 列の値を返す'
    return board[i][j]
#
# 盤面の i, j に手番 t を登録, 状態を文字列で返す


def set_board(i, j, t):
    '''
    盤面の i, j に手番 t を登録, 状態を文字列で返す
    返す値は
    'ok' 成功
    'Not empty' 空いている場所ではない
    'illegal turn' 手番が正しくない
    'illegal slot' 指定された場所が正しくない
    '''
    if (i >= 0) and (i < 3) and (j >= 0) and (j < 3):
        if (t > 0) and (t < 3):
            if examine_board(i, j) == 0:
                board[i][j] = t
                return 'OK'
            else:
                return 'Not empty'
        else:
            return 'illegal turn'
    else:
        return 'illegal slot'
#
# 盤面のテスト関数


def test_board1():
    '盤面についてのテストプログラムの1つめです'
    init_board()
    print(show_board())
    print(set_board(0, 0, 1))
    print(show_board())
    print(set_board(1, 1, 2))
    print(show_board())
    print(set_board(1, 1, 1))
    print(show_board())
#
# 水平方向での手番 t の勝ちの判定


def check_board_horizontal(t):
    '水平方向に手番 t が勝ちであることを判定します'
    for i in range(3):
        if (board[i][0] == t) and (board[i][1] == t) and (board[i][2] == t):
            return True
    return False

# 垂直方向での手番 t の勝ちの判定


def check_board_vertical(t):
    '垂直方向に手番 t が勝ちであることを判定します'
    for j in range(3):
        if (board[0][j] == t) and (board[1][j] == t) and (board[2][j] == t):
            return True
    return False

# 対角方向での手番 t の勝ちの判定


def check_board_diagonal(t):
    '対角方向に手番 t が勝ちであることを判定します'
    if (board[0][0] == t) and (board[1][1] == t) and (board[2][2] == t):
        return True
    return False

# 逆対角方向での手番 t の勝ちの判定


def check_board_inverse_diagonal(t):
    '逆対角方向に手番 t が勝ちであることを判定します'
    if (board[0][2] == t) and (board[1][1] == t) and (board[2][0] == t):
        return True
    return False

# 手番 t の勝ちの単純な判定


def is_win_simple(t):
    '手番 t が勝ちであることを判定します。相手が勝っていることはチェックしません'
    if check_board_horizontal(t) or check_board_vertical(t) or check_board_diagonal(t) or check_board_inverse_diagonal(t):
        return True
    return False
#
