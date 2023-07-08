import os

v_bar = '┃'
h_bar = '━'

# big block letter word
r_win_msg = """
██████╗░███████╗██████╗░  ░██╗░░░░░░░██╗██╗███╗░░██╗
██╔══██╗██╔════╝██╔══██╗  ░██║░░██╗░░██║██║████╗░██║
██████╔╝█████╗░░██║░░██║  ░╚██╗████╗██╔╝██║██╔██╗██║
██╔══██╗██╔══╝░░██║░░██║  ░░████╔═████║░██║██║╚████║
██║░░██║███████╗██████╔╝  ░░╚██╔╝░╚██╔╝░██║██║░╚███║
╚═╝░░╚═╝╚══════╝╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝
"""
b_win_msg = """
██████╗░██╗░░░░░░█████╗░░█████╗░██╗░░██╗  ░██╗░░░░░░░██╗██╗███╗░░██╗
██╔══██╗██║░░░░░██╔══██╗██╔══██╗██║░██╔╝  ░██║░░██╗░░██║██║████╗░██║
██████╦╝██║░░░░░███████║██║░░╚═╝█████═╝░  ░╚██╗████╗██╔╝██║██╔██╗██║
██╔══██╗██║░░░░░██╔══██║██║░░██╗██╔═██╗░  ░░████╔═████║░██║██║╚████║
██████╦╝███████╗██║░░██║╚█████╔╝██║░╚██╗  ░░╚██╔╝░╚██╔╝░██║██║░╚███║
╚═════╝░╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝
"""


# useful tools
class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  WHITE = '\033[94m'


def pprint(text='', color=bcolors.ENDC, end='\n'):
  print(f"{color}{text}{bcolors.ENDC}", end=end)


# chee class
class chess:

  processing_chee = {"type": 'r0', "pos": [0, 0]}

  def __init__(self):
    self.board = [
      ['b3', 'b2', 'b4', 'b5', 'b6', 'b5', 'b4', 'b2', 'b3'],
      ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
      ['  ', 'b1', '  ', '  ', '  ', '  ', '  ', 'b1', '  '],
      ['b0', '  ', 'b0', '  ', 'b0', '  ', 'b0', '  ', 'b0'],
      ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
      # ====== river =====
      # ====== river =====
      ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
      ['r0', '  ', 'r0', '  ', 'r0', '  ', 'r0', '  ', 'r0'],
      ['  ', 'r1', '  ', '  ', '  ', '  ', '  ', 'r1', '  '],
      ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
      ['r3', 'r2', 'r4', 'r5', 'r6', 'r5', 'r4', 'r2', 'r3'],
    ]

    for i in range(10):
      for j in range(9):
        if self.board[i][j] == '  ':  # empty
          self.board[i][j] = 'N'

    self.encode_dict = {
      'r0': '兵',
      'r1': '炮',
      'r2': '傌',
      'r3': '俥',
      'r4': '像',
      'r5': '仕',
      'r6': '帥',
      'b0': '卒',
      'b1': '包',
      'b2': '馬',
      'b3': '車',
      'b4': '象',
      'b5': '士',
      'b6': '將',
      'N': '  '
    }

    self.start_game()

  def start_game(self):
    # currently without checking win or lose
    welcome_msg = '''
    
░█████╗░██╗░░██╗██╗███╗░░██╗███████╗░██████╗███████╗  ░█████╗░██╗░░██╗███████╗███████╗
██╔══██╗██║░░██║██║████╗░██║██╔════╝██╔════╝██╔════╝  ██╔══██╗██║░░██║██╔════╝██╔════╝
██║░░╚═╝███████║██║██╔██╗██║█████╗░░╚█████╗░█████╗░░  ██║░░╚═╝███████║█████╗░░█████╗░░
██║░░██╗██╔══██║██║██║╚████║██╔══╝░░░╚═══██╗██╔══╝░░  ██║░░██╗██╔══██║██╔══╝░░██╔══╝░░
╚█████╔╝██║░░██║██║██║░╚███║███████╗██████╔╝███████╗  ╚█████╔╝██║░░██║███████╗███████╗
░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝╚═════╝░╚══════╝  ░╚════╝░╚═╝░░╚═╝╚══════╝╚══════╝
\n
    '''
    pprint(welcome_msg, bcolors.OKCYAN)
    pprint("who go first? (red or black)", bcolors.OKCYAN)
    first = input()
    os.system("clear")
    if first == "red" or first == "RED":
      turn = 0
    else:
      turn = 1

    flag = 0
    # 0 -> 沒問題
    # 1 -> 兩階段
    # 2 -> 後面階段
    while 1:
      self.render_board()
      if turn % 2 == 0:  #  red  turn
        pprint("\n\n====  紅方下  ====", bcolors.FAIL)
        now_go = 'r'

      else:  # black turn
        pprint("\n\n====  黑方下  ====", bcolors.OKBLUE)
        now_go = 'b'

      if flag == 1 or flag == 0:
        while 1:

          user_own_piece = input("輸入你要移動的棋的座標(原始位置) (x y): ")
          user_from_x, user_from_y = [int(i) for i in user_own_piece]
          if now_go not in self.board[user_from_y][user_from_x][0]:
            pprint("invalid move: 下你自己的棋", color=bcolors.FAIL)
            continue
          if user_from_x > 8 or user_from_x < 0:
            pprint("invalid input x", bcolors.FAIL)
            continue
          if user_from_y > 9 or user_from_y < 0:
            pprint("invalid input y", bcolors.FAIL)
            continue
          break

      while 1:
        user_move = input("輸入你要下的座標(目標位置)       (x y): ")
        if user_move == '0':
          while 1:

            user_own_piece = input("輸入你要移動的棋的座標(原始位置) (x y): ")
            user_from_x, user_from_y = [int(i) for i in user_own_piece]
            if now_go not in self.board[user_from_y][user_from_x][0]:
              pprint("invalid move: 下你自己的棋", color=bcolors.FAIL)
              continue
            if user_from_x > 8 or user_from_x < 0:
              pprint("invalid input x", bcolors.FAIL)
              continue
            if user_from_y > 9 or user_from_y < 0:
              pprint("invalid input y", bcolors.FAIL)
              continue
            break
            
        else:
          user_to_x, user_to_y = [int(i) for i in user_move]
          if user_to_x > 8 or user_to_x < 0:
            pprint("invalid input x", bcolors.FAIL)
            flag = 2
            continue
          if user_to_y > 9 or user_to_y < 0:
            pprint("invalid input y", bcolors.FAIL)
            flag = 2
            continue
          flag = 0
        break


      os.system("clear")

      # pprint("from : " + user_own_piece)
      # pprint("to   : " + user_move)

      chee_type = self.board[user_from_y][user_from_x]
      self_pos = [user_from_x, user_from_y]
      target_pos = [user_to_x, user_to_y]

      result = self.move(chee_type, self_pos, target_pos)

      if result == -1:
        flag = 2  # re-choose
        continue
      elif result is not None:
        pprint(result)

      turn += 1

      win_lose = self.detect_win_lose()

      if win_lose == -1:  # not yet
        pass
      else:  # someone wins
        if win_lose == 0:  # red wins
          # r_win_msg = '''
          # #############################################
          # #               GAME OVER!!                 #
          # #                 RED WIN                   #
          # #############################################
          # '''
          # b_win_msg = '''
          # #############################################
          # #               GAME OVER!!                 #
          # #                BLACK WIN                  #
          # #############################################
          # '''
          pprint(r_win_msg, bcolors.OKGREEN)
        elif win_lose == 1:  # black wins
          pprint(b_win_msg, bcolors.OKGREEN)

        break

  # ================
  # || 判斷輸贏 ||
  # ================
  def detect_win_lose(self):

    # detect red or black wins

    # return 0  if red   wins
    # return 1  if black wins
    # return -1 if no one wins currently

    red_king_found = 0
    black_king_found = 0

    for y_line in self.board:
      if 'r6' in y_line:
        red_king_found = 1
      if 'b6' in y_line:
        black_king_found = 1

    if red_king_found == 0:  # there's no king in red -> red lose
      return 1  # black wins
    elif black_king_found == 0:  # black lose
      return 0  # red wins
    else:
      return -1

  # ================
  # || 渲染棋盤 ||
  # ================
  def render_board(self):
    # pprint x line number
    pprint(" " * 4, end='')
    for x_number in range(9):
      pprint(x_number, end=' ' * 4)
    pprint()

    pprint("  " + h_bar * 45)
    for y in range(10):  # 0 ~ 9

      # pprint y line number
      pprint(y, end=" ")

      for x in range(9):
        try:
          element = self.encode_dict[self.board[y][x]]
        except:
          element = "N "  # 2 space
        if element in ['兵', '炮', '傌', '俥', '像', '仕', '帥']:
          pprint("┃ ", end='')
          pprint(element, end=" ", color=bcolors.FAIL)
        else:
          pprint("┃ ", end='')
          pprint(element, end=" ", color=bcolors.WHITE)
      pprint("┃")
      pprint("  " + h_bar * 45)

      if y == 4:
        # pprint river
        side = "=" * 19
        pprint('\n' + "  " + side + " River " + side + '=')
        pprint("  " + side + " Border " + side + '\n')
        pprint("  " + h_bar * 45)

  def remove_same_point(self, a):
    return set(tuple(element) for element in a)

  # ================
  # || 兵: 規則檢查 ||
  # ================
  # Tested
  def checker_0(self, chee_type, chee_pos):
    # chee_type: 'r0', chee_pos: [0, 1]
    #                            [x, y]
    chee_x = chee_pos[0]
    chee_y = chee_pos[1]
    allow_pos = []

    # 只能向前走

    if chee_type[0] == 'r':  # red

      allow_pos.append([chee_x, chee_y - 1])

      if chee_y <= 4:  # 過河後可以左右走
        allow_pos.append([chee_x + 1, chee_y])  # right
        allow_pos.append([chee_x - 1, chee_y])  # left

    else:  # black
      allow_pos.append([chee_x, chee_y + 1])

      if chee_y >= 5:
        allow_pos.append([chee_x - 1, chee_y])
        allow_pos.append([chee_x + 1, chee_y])

    return allow_pos

  # ================
  # || 炮: 規則檢查 ||
  # ================
  # Tested
  def checker_1(self, chee_type, chee_pos):
    chee_x = chee_pos[0]
    chee_y = chee_pos[1]
    allow_pos = []

    if chee_type[0] == 'r':  # red

      # find obstacle & eaten object
      """
      炮     O            O
          obstacle      eaten
      """
      pointer = [chee_x, chee_y]
      eat_mode = 0

      # down
      pointer = [chee_x, chee_y]
      eat_mode = 0
      while 1:
        pointer[1] += 1  # go down for 1 step
        try:
          if self.board[pointer[1]][pointer[0]] != 'N':  # not empty
            if not eat_mode:  # meet obstacle
              eat_mode = 1
            else:  # meet eaten, the end
              allow_pos.append([pointer[0], pointer[1]])
              break

          elif not eat_mode:  # empty. "not eat_mode" to avoid empty jump
            allow_pos.append([pointer[0], pointer[1]])
        except IndexError:
          break

      # up
      pointer = [chee_x, chee_y]
      eat_mode = 0
      while 1:
        pointer[1] -= 1  # go up for 1 step
        if pointer[1] >= 0:
          if self.board[pointer[1]][pointer[0]] != 'N':  # not empty
            if not eat_mode:  # meet obstacle
              eat_mode = True
            else:  # meet eaten, the end
              allow_pos.append([pointer[0], pointer[1]])
              break

          elif not eat_mode:
            allow_pos.append([pointer[0], pointer[1]])

        else:  # out of board
          break

      # right
      pointer = [chee_x, chee_y]
      eat_mode = 0
      while 1:
        pointer[0] += 1  # go right for 1 step
        try:
          if self.board[pointer[1]][
              pointer[0]] != 'N':  # not empty => detect a chee
            if not eat_mode:  # meet obstacle
              eat_mode = True
            else:  # meet eaten, the end
              # pprint("right")
              allow_pos.append([pointer[0], pointer[1]])
              break

          elif not eat_mode:
            allow_pos.append([pointer[0], pointer[1]])

        except IndexError:
          break

      # left
      pointer = [chee_x, chee_y]
      eat_mode = 0
      while 1:
        pointer[0] -= 1  # go left for 1 step
        if pointer[0] >= 0:  # avoid out of board
          if self.board[pointer[1]][
              pointer[0]] != 'N':  # not empty => detect a chee
            if not eat_mode:  # meet obstacle
              eat_mode = True
            else:  # meet eaten, the end
              allow_pos.append([pointer[0], pointer[1]])
              break
          elif not eat_mode:
            allow_pos.append([pointer[0], pointer[1]])

        else:  # out of board
          break

    else:  # black

      # find obstacle & eaten object  chess().checker_1('r1',[1,7])
      """
      炮     O            O
          obstacle      eaten
      """
      pointer = [chee_x, chee_y]
      eat_mode = 0

      # down
      pointer = [chee_x, chee_y]
      eat_mode = 0
      while 1:
        pointer[1] += 1  # go down for 1 step
        try:
          if self.board[pointer[1]][pointer[0]] != 'N':  # not empty
            if not eat_mode:  # meet obstacle
              eat_mode = 1
            else:  # meet eaten, the end
              allow_pos.append([pointer[0], pointer[1]])
              break

          elif not eat_mode:  # empty. "not eat_mode" to avoid empty jump
            allow_pos.append([pointer[0], pointer[1]])
        except IndexError:
          break

      # up
      pointer = [chee_x, chee_y]
      eat_mode = 0
      while 1:
        pointer[1] -= 1  # go up for 1 step
        if pointer[1] >= 0:
          if self.board[pointer[1]][pointer[0]] != 'N':  # not empty
            if not eat_mode:  # meet obstacle
              eat_mode = True
            else:  # meet eaten, the end
              allow_pos.append([pointer[0], pointer[1]])
              break

          elif not eat_mode:
            allow_pos.append([pointer[0], pointer[1]])

        else:  # out of board
          break

      # right
      pointer = [chee_x, chee_y]
      eat_mode = 0
      while 1:
        pointer[0] += 1  # go right for 1 step
        try:
          if self.board[pointer[1]][
              pointer[0]] != 'N':  # not empty => detect a chee
            if not eat_mode:  # meet obstacle
              eat_mode = True
            else:  # meet eaten, the end
              allow_pos.append([pointer[0], pointer[1]])
              break

        except IndexError:
          break

      # left
      pointer = [chee_x, chee_y]
      eat_mode = 0
      while 1:
        pointer[0] -= 1  # go left for 1 step
        if pointer[0] >= 0:  # avoid out of board
          if self.board[pointer[1]][
              pointer[0]] != 'N':  # not empty => detect a chee
            if not eat_mode:  # meet obstacle
              eat_mode = True
            else:  # meet eaten, the end
              allow_pos.append([pointer[0], pointer[1]])
              break

        else:  # out of board
          break

    return allow_pos

  # ================
  # || 馬: 規則檢查 ||
  # ================
  # Tested successfully
  def checker_2(self, chee_type, chee_pos):
    # chee_type: 'r0', chee_pos: [0, 1]
    #                            [x, y]
    chee_x = chee_pos[0]
    chee_y = chee_pos[1]
    allow_pos = []

    # 繞過卡腳後可以去
    try:
      if self.board[chee_y][chee_x + 1] == 'N':  # 卡腳
        allow_pos.append([chee_x + 2, chee_y - 1])
        allow_pos.append([chee_x + 2, chee_y + 1])
    except IndexError:
      pass  # list index out of range

    try:
      if self.board[chee_y][chee_x - 1] == 'N':  # 卡腳
        allow_pos.append([chee_x - 2, chee_y - 1])
        allow_pos.append([chee_x - 2, chee_y + 1])
    except IndexError:
      pass

    try:
      if self.board[chee_y - 1][chee_x] == 'N':  # 卡腳
        allow_pos.append([chee_x + 1, chee_y - 2])
        allow_pos.append([chee_x - 1, chee_y - 2])
    except IndexError:
      pass

    try:
      if self.board[chee_y + 1][chee_x] == 'N':  # 卡腳
        allow_pos.append([chee_x + 1, chee_y + 2])
        allow_pos.append([chee_x - 1, chee_y + 2])
    except:
      pass

    return allow_pos

  # ================
  # || 車: 規則檢查 ||
  # ================
  # Tested successfully
  def checker_3(self, chee_type, chee_pos):
    # chee_type: 'r0', chee_pos: [0, 1]
    #                            [x, y]
    chee_x = chee_pos[0]
    chee_y = chee_pos[1]
    allow_pos = []

    for i in range(chee_x + 1, 9):  # right
      allow_pos.append([i, chee_y])

      if self.board[chee_y][i] != 'N':  # meet first obstacle
        break

    for i in range(chee_y + 1, 10):  # down
      allow_pos.append([chee_x, i])
      if self.board[i][chee_x] != 'N':  # meet first obstacle
        break

    for i in range(chee_x - 1, -1, -1):  # left
      allow_pos.append([i, chee_y])
      if self.board[chee_y][i] != 'N':
        break

    for i in range(chee_y - 1, -1, -1):  # up
      allow_pos.append([chee_x, i])
      if self.board[i][chee_x] != 'N':
        break

    return allow_pos

  # ================
  # || 象: 規則檢查 ||
  # ================
  def checker_4(self, chee_type, chee_pos):
    # chee_type: 'r0', chee_pos: [0, 1]
    #                            [x, y]
    chee_x = chee_pos[0]
    chee_y = chee_pos[1]
    allow_pos = []

    # 繞過卡腳後可以去
    try:
      if self.board[chee_y][chee_x + 1] == 'N':  # 卡腳
        allow_pos.append([chee_x + 2, chee_y - 2])
        allow_pos.append([chee_x + 2, chee_y + 2])
    except IndexError:
      pass

    try:
      if self.board[chee_y][chee_x - 1] == 'N':  # 卡腳
        allow_pos.append([chee_x - 2, chee_y - 2])
        allow_pos.append([chee_x - 2, chee_y + 2])
    except IndexError:
      pass

    try:
      if self.board[chee_y - 1][chee_x] == 'N':  # 卡腳
        allow_pos.append([chee_x + 2, chee_y - 2])
        allow_pos.append([chee_x - 2, chee_y - 2])
    except IndexError:
      pass

    try:
      if self.board[chee_y + 1][chee_x] == 'N':  # 卡腳
        allow_pos.append([chee_x + 2, chee_y + 2])
        allow_pos.append([chee_x - 2, chee_y + 2])
    except IndexError:
      pass

      # 不能過河

    for i in range(len(allow_pos)):
      if chee_type[0] == 'r':  # red
        if allow_pos[i][1] <= 4:  # y must smaller than 4
          allow_pos[i] = chee_pos
      if chee_type[0] == 'b':  # black
        if allow_pos[i][1] > 4:
          allow_pos[i] = chee_pos
    try:
      allow_pos.remove(chee_pos)
    except:
      pass
    return allow_pos

  # ================
  # || 士: 規則檢查 ||
  # ================
  # Tested successfully
  def checker_5(self, chee_type, chee_pos):
    # chee_type: 'r0', chee_pos: [0, 1]
    #                            [x, y]
    chee_x = chee_pos[0]
    chee_y = chee_pos[1]
    allow_pos = []

    for i in [[chee_x + 1, chee_y + 1], [chee_x + 1, chee_y - 1],
              [chee_x - 1, chee_y + 1], [chee_x - 1, chee_y - 1]]:
      if chee_type[
          0] == 'r' and i[0] >= 3 and i[0] <= 5 and i[1] >= 7 and i[1] <= 9:
        allow_pos.append(i)
      elif chee_type[
          0] == 'b' and i[0] >= 3 and i[0] <= 5 and i[1] >= 0 and i[1] <= 2:
        allow_pos.append(i)

    return allow_pos

  # b_m 將
  def checker_max(self, chee_type, chee_x, chee_y):
    # True: 中間沒間隔

    g_x, g_y = 0, 0

    if chee_type[0] == 'r':
      #find black general
      for _y in range(10):
        for _x in range(9):
          if self.board[_y][_x] == 'b6':
            g_x, g_y = _x, _y
      if chee_x != g_x: # not in the same line
        return [-1, -1]
      # allow_flag = True # True if the general can place there, False if cannot
      for y in range(g_y+1, chee_y):
        if self.board[y][chee_x] != 'N':
          return [-1, -1]

      # all empty
      return [g_x, g_y]
      
    else:
      #find red general
      for _y in range(10):
        for _x in range(9):
          if self.board[_y][_x] == 'r6':
            g_x, g_y = _x, _y
      if chee_x != g_x: # not in the same line
        return [-1, -1]
      # allow_flag = True # True if the general can place there, False if cannot
      # print(chee_y, g_y)
      for y in range(chee_y+1, g_y-1, 1):
        if self.board[y][chee_x] != 'N':
                  
          return [-1, -1]

      # all empty
      return [g_x, g_y]

    """
    if b_m[0] == r_m[0]:
      for i in (b_m[1], r_m[1]+1):
        if self.board[i][b_m[0]] != 'N':
          return False
      return True
    else:
      return False"""
    
  
  # ================
  # || 將: 規則檢查 ||
  # ================
  # Tested successfully
  def checker_6(self, chee_type, chee_pos):
    # chee_type: 'r0', chee_pos: [0, 1]
    #                            [x, y]
    chee_x = chee_pos[0]
    chee_y = chee_pos[1]
    allow_pos = []

    # target_x = 5 ; 9
    def check_road(target_x, target_y, self_type):
      # 如果和對方再同一排
      if self_type == 'r':
        for i in range(10):
          if self.board[i][target_x] == 'b6':
            for y_ in range(7, 10):
              for r in range(i, y_ + 1):
                #print(649, self.board[r][y_])
                if self.board[r][y_] != 'N':
                  return True
          return True
      if self_type == 'b':
        for i in range(10):
          if self.board[i][target_x] == 'r6':
            for y_ in range(0, 4):
              for r in range(i, y_ + 1):
                #print(656, self.board[r][y_])
                if self.board[r][y_] != 'N':
                  return True
          return True

    for i in [[chee_x + 1, chee_y], [chee_x - 1, chee_y], [chee_x, chee_y + 1],
              [chee_x, chee_y - 1]]:
      if chee_type[
          0] == 'r' and i[0] >= 3 and i[0] <= 5 and i[1] >= 7 and i[1] <= 9:
        #if check_road(i[0], i[1], chee_type[0]) == True:
        allow_pos.append(i)
      elif chee_type[
          0] == 'b' and i[0] >= 3 and i[0] <= 5 and i[1] >= 0 and i[1] <= 2:
        #if check_road(i[0], i[1], chee_type[0]) == True:
        allow_pos.append(i)

    
        
        
            
    end = self.checker_max(chee_type, chee_x, chee_y)
    if end != [-1, -1]: 
      # true if both general can capture each other
      # print("in end")
      allow_pos.append(end)
    

    

    return allow_pos

  # 移動
  def move(self, chee_type, self_pos, target_pos):
    # return -1 if invalid move, need to rechoose again
    if self.board[target_pos[1]][
        target_pos[0]][0] == chee_type[0]:  # same color
      print('go die!\nbro, you just captured yourself')
      return -1

    try:
      if target_pos[0] < 0 or target_pos[1] < 0 or target_pos[
          0] > 9 or target_pos[0] > 9:
        return 'go die!'
    except:
      return 'error: go die!'

    if chee_type[0] == 'N':
      return -1
    elif chee_type[1] == '0':
      alllow_pos = self.checker_0(chee_type, self_pos)
    elif chee_type[1] == '1':
      alllow_pos = self.checker_1(chee_type, self_pos)
    elif chee_type[1] == '2':
      alllow_pos = self.checker_2(chee_type, self_pos)
    elif chee_type[1] == '3':
      alllow_pos = self.checker_3(chee_type, self_pos)
    elif chee_type[1] == '4':
      alllow_pos = self.checker_4(chee_type, self_pos)
    elif chee_type[1] == '5':
      alllow_pos = self.checker_5(chee_type, self_pos)
    elif chee_type[1] == '6':
      alllow_pos = self.checker_6(chee_type, self_pos)

    if target_pos in alllow_pos:
      self.board[target_pos[1]][target_pos[0]] = chee_type
      self.board[self_pos[1]][self_pos[0]] = 'N'
    elif target_pos in alllow_pos and self.board[target_pos[1]][
        target_pos[0]] != chee_type:
      pprint('別亂搞', bcolors.FAIL)
    else:
      pprint("別作夢", bcolors.FAIL)
      return -1


game = chess()
"""
To Do List:
    Date 2023/5/8 Mon.
    1. show error ( why user cannot move to that position )
    2. become another's turn until user finish
       if user made an invalid move, user should make another move again, not just become another's
    3. clear screen for each rendering

Current
"""
"""

[
 9
 8
 7
 6
 5
 4
 3 
 2
 1
 0 
  0 1 2 3 4 5 6 7 8

]

board:

━━━━━━━━━━━━━━━━━━━━
| r0 |    | r0 |   ┃
━━━━━━━━━━━━━━━━━━━━


"""
