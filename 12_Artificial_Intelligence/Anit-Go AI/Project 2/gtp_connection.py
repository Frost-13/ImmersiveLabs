"""
gtp_connection.py
Module for playing games of Go using GoTextProtocol

Parts of this code were originally based on the gtp module
in the Deep-Go project by Isaac Henrion and Amos Storkey
at the University of Edinburgh.
"""
import traceback
from sys import stdin, stdout, stderr
from board_util import GoBoardUtil, BLACK, WHITE, EMPTY, BORDER, PASS, \
                       MAXSIZE, coord_to_point
import numpy as np
import re
import signal, os

#for Boolean Minimax
import time



class GtpConnection():

    timel = 1
    genmoved = 0
    movelist = list()
    # Table is stored in a dictionary, with board code as key,
    # and minimax score as the value
    # Empty dictionary
    table = {}

    def __init__(self, go_engine, board, debug_mode = False):
        """
        Manage a GTP connection for a Go-playing engine

        Parameters
        ----------
        go_engine:
            a program that can reply to a set of GTP commandsbelow
        board:
            Represents the current board state.
        """
        self._debug_mode = debug_mode
        self.go_engine = go_engine
        self.board = board
        self.commands = {
            "protocol_version": self.protocol_version_cmd,
            "quit": self.quit_cmd,
            "name": self.name_cmd,
            "boardsize": self.boardsize_cmd,
            "showboard": self.showboard_cmd,
            "clear_board": self.clear_board_cmd,
            "komi": self.komi_cmd,
            "version": self.version_cmd,
            "known_command": self.known_command_cmd,
            "genmove": self.genmove_cmd,
            "list_commands": self.list_commands_cmd,
            "play": self.play_cmd,
            "legal_moves": self.legal_moves_cmd,
            "gogui-rules_game_id": self.gogui_rules_game_id_cmd,
            "gogui-rules_board_size": self.gogui_rules_board_size_cmd,
            "gogui-rules_legal_moves": self.gogui_rules_legal_moves_cmd,
            "gogui-rules_side_to_move": self.gogui_rules_side_to_move_cmd,
            "gogui-rules_board": self.gogui_rules_board_cmd,
            "gogui-rules_final_result": self.gogui_rules_final_result_cmd,
            "gogui-analyze_commands": self.gogui_analyze_cmd,
            "solve": self.solve_cmd,
            "timelimit": self.timelimit_cmd
        }

        # used for argument checking
        # values: (required number of arguments,
        #          error message on argnum failure)
        self.argmap = {
            "boardsize": (1, 'Usage: boardsize INT'),
            "komi": (1, 'Usage: komi FLOAT'),
            "known_command": (1, 'Usage: known_command CMD_NAME'),
            "genmove": (1, 'Usage: genmove {w,b}'),
            "play": (2, 'Usage: play {b,w} MOVE'),
            "legal_moves": (1, 'Usage: legal_moves {w,b}'),
            "solve": (0, 'Usage: solve'),
            "timelimit": (1, 'Usage: timelimit INT')
        }

    def write(self, data):
        stdout.write(data)

    def flush(self):
        stdout.flush()

    def start_connection(self):
        """
        Start a GTP connection.
        This function continuously monitors standard input for commands.
        """
        line = stdin.readline()
        while line:
            self.get_cmd(line)
            line = stdin.readline()

    def get_cmd(self, command):
        """
        Parse command string and execute it
        """
        if len(command.strip(' \r\t')) == 0:
            return
        if command[0] == '#':
            return
        # Strip leading numbers from regression tests
        if command[0].isdigit():
            command = re.sub("^\d+", "", command).lstrip()

        elements = command.split()
        if not elements:
            return
        command_name = elements[0]; args = elements[1:]
        if self.has_arg_error(command_name, len(args)):
            return
        if command_name in self.commands:
            try:
                self.commands[command_name](args)
            except Exception as e:
                self.debug_msg("Error executing command {}\n".format(str(e)))
                self.debug_msg("Stack Trace:\n{}\n".
                               format(traceback.format_exc()))
                raise e
        else:
            self.debug_msg("Unknown command: {}\n".format(command_name))
            self.error('Unknown command')
            stdout.flush()

    def has_arg_error(self, cmd, argnum):
        """
        Verify the number of arguments of cmd.
        argnum is the number of parsed arguments
        """
        if cmd in self.argmap and self.argmap[cmd][0] != argnum:
            self.error(self.argmap[cmd][1])
            return True
        return False

    def debug_msg(self, msg):
        """ Write msg to the debug stream """
        if self._debug_mode:
            stderr.write(msg)
            stderr.flush()

    def error(self, error_msg):
        """ Send error msg to stdout """
        stdout.write('? {}\n\n'.format(error_msg))
        stdout.flush()

    def respond(self, response=''):
        """ Send response to stdout """
        stdout.write('= {}\n\n'.format(response))
        stdout.flush()

    def reset(self, size):
        """
        Reset the board to empty board of given size
        """
        self.board.reset(size)

    def board2d(self):
        return str(GoBoardUtil.get_twoD_board(self.board))

    def protocol_version_cmd(self, args):
        """ Return the GTP protocol version being used (always 2) """
        self.respond('2')

    def quit_cmd(self, args):
        """ Quit game and exit the GTP interface """
        self.respond()
        exit()

    def name_cmd(self, args):
        """ Return the name of the Go engine """
        self.respond(self.go_engine.name)

    def version_cmd(self, args):
        """ Return the version of the  Go engine """
        self.respond(self.go_engine.version)

    def clear_board_cmd(self, args):
        """ clear the board """
        self.reset(self.board.size)
        self.respond()

    def boardsize_cmd(self, args):
        """
        Reset the game with new boardsize args[0]
        """
        self.reset(int(args[0]))
        self.respond()

    def showboard_cmd(self, args):
        self.respond('\n' + self.board2d())

    def komi_cmd(self, args):
        """
        Set the engine's komi to args[0]
        """
        self.go_engine.komi = float(args[0])
        self.respond()

    def known_command_cmd(self, args):
        """
        Check if command args[0] is known to the GTP interface
        """
        if args[0] in self.commands:
            self.respond("true")
        else:
            self.respond("false")

    def list_commands_cmd(self, args):
        """ list all supported GTP commands """
        self.respond(' '.join(list(self.commands.keys())))

    def timelimit_cmd(self, args):
        if int(args[0]) >= 1 and int(args[0]) <= 100:
            self.timel = args[0]
        self.respond()

    def legal_moves_cmd(self, args):
        """
        List legal moves for color args[0] in {'b','w'}
        """
        board_color = args[0].lower()
        color = color_to_int(board_color)
        moves = GoBoardUtil.generate_legal_moves(self.board, color)
        gtp_moves = []
        for move in moves:
            coords = point_to_coord(move, self.board.size)
            gtp_moves.append(format_point(coords))
        sorted_moves = ' '.join(sorted(gtp_moves))
        self.respond(sorted_moves)

    def play_cmd(self, args):
        """
        play a move args[1] for given color args[0] in {'b','w'}
        """
        try:
            board_color = args[0].lower()
            board_move = args[1]
            if board_color != "b" and board_color !="w":
                self.respond("illegal move: \"{}\" wrong color".format(board_color))
                return
            color = color_to_int(board_color)
            if args[1].lower() == 'pass':
                self.respond("illegal move: \"{} {}\" wrong coordinate".format(args[0], args[1]))
                return
            coord = move_to_coord(args[1], self.board.size)
            if coord:
                move = coord_to_point(coord[0],coord[1], self.board.size)
            else:
                self.error("Error executing move {} converted from {}"
                           .format(move, args[1]))
                return
            if not self.board.play_move(move, color):
                self.respond("illegal move: \"{} {}\" ".format(args[0], board_move))
                return
            else:
                self.debug_msg("Move: {}\nBoard:\n{}\n".
                                format(board_move, self.board2d()))
            self.respond()
        except Exception as e:
            self.respond('illegal move: \"{} {}\" {}'.format(args[0], args[1], str(e)))


    def endOfGameNega(self, state):
        """if the current player has no moves, it's game over and a win for the opponent"""
        if GoBoardUtil.generate_legal_moves(state, state.current_player) == []:
            return True
        else:
            return False


    def code(self, state):
        id = ""
        #print("new id: ")
        for point in range(0, self.board.size*self.board.size + 3 * (self.board.size+1) ):
            #print("colour: "+ str(state.get_color(point)))
            id = id + str(state.get_color(point))
            #print("current id: "+ str(id))
        #print("final id: "+ str(id))
        #numerals = "0123456789abcdefghijklmnopqrstuvwxyz"
        return sum("0123".index(x)*4**i for i, x in enumerate(id[::-1]))

    def storeResult(self, state, result):
        id = ""
        rid = ""
        #print("new rid: ")
        for point in range(0, self.board.size*self.board.size + 3 * (self.board.size+1) ):
            #print("colour: "+ str(state.get_color(point)))
            id = id + str(state.get_color(point))
            #print("current rid: "+ str(id))
        #print("final rid: "+ str(id))
        rid = id[::-1]
        #numerals = "0123456789abcdefghijklmnopqrstuvwxyz"
        self.store(sum("0123".index(x)*4**i for i, x in enumerate(id[::-1])),result)
        self.store(sum("0123".index(x)*4**i for i, x in enumerate(rid[::-1])),result)


    #def storeResult(self, state, result):
        #self.store(self.code(state), result)
        #self.store(self.rcode(state), result)

    # Used to print the whole table with print(tt)
    def __repr__(self):
        return self.table.__repr__()

    def store(self, Code, score):
        self.table[Code] = score

    # Python dictionary returns 'None' if key not found by get()
    def lookup(self, Code):
        return self.table.get(Code)

    #**************************************************************************
    def negamaxBooleanFirst(self, state):
        moves = GoBoardUtil.generate_legal_moves(state, state.current_player)
        if not moves:
            #return the state of win here
            return False
        for m in moves:
            # make another copy to avoid having to implement undo
            stateN = state.copy()
            stateN.play_move(m, stateN.current_player)
            result = self.lookup(self.code(stateN))
            if result != None:
                if not result:
                    continue
            isWin = not self.negamaxBoolean(stateN)
            if isWin:
                self.movelist.append(m)
                return True
            else:
                self.storeResult(state, False)
        return False


    def negamaxBoolean(self, state):

        moves = GoBoardUtil.generate_legal_moves(state, state.current_player)
        #where should i copy the board?
        if not moves:
            #return the state of win here
            return False
        result = self.lookup(self.code(state))
        if result != None:
            return result
        for m in moves:
            stateN = state.copy()
            stateN.play_move(m, stateN.current_player)
            isWin = not self.negamaxBoolean(stateN)

            if isWin:
                self.storeResult(state, True)
                #print(self.table)
                return True
        self.storeResult(state, False)
        #print(self.table)
        return False


    def handler(self, arg1, arg2):
        raise TimeoutException()

    def solve_cmd(self, args):
        #this is an intiger
        color = self.board.current_player

        #make a copy of the board
        state = self.board.copy()

        signal.signal(signal.SIGALRM, self.handler)
        signal.alarm(int(self.timel))

        #print(self.board.__dict__)
        win = False
        try:

            win = self.negamaxBooleanFirst(state)

        except TimeoutException:
            if self.genmoved != 1:
                self.respond("unknown")
            return "unknown"
        signal.alarm(0)

        if not win:
            # doing this because for some reason, things don't format correctly
            temp = GoBoardUtil.opponent(color)
            if temp == 1:
                temp = 'b'
            else:
                temp = 'w'
            if self.genmoved != 1:
                self.respond(temp)

            return str(temp)
        else: # game won
            if self.board.current_player == 1:
                color1 = 'b'
            elif self.board.current_player == 2:
                color1 = 'w'

            winmove = self.movelist[0]

            temp = point_to_coord(winmove, self.board.size)
            winner = format_point(temp)
            while self.movelist:
                self.movelist.clear()
            if self.genmoved != 1:
                self.respond(color1 + " " + str(winner).lower())
            statment = color1 + " " + str(winner).lower()
            return statment

    def genmove_cmd(self, args):
        """
        Generate a move for the color args[0] in {'b', 'w'}, for the game of gomoku.
        """
        self.genmoved = 1
        result = self.solve_cmd(args)
        self.genmoved = 0
        c = str(result).split()
        if c[0] == args[0] or c[0] == "draw":
            board_color = args[0].lower()
            color = color_to_int(board_color)
            move = c[1]
            move_coord = point_to_coord(move, self.board.size)
            move_as_string = format_point(move_coord)
            self.board.play_move(move, color)
            self.respond(move_as_string.lower())
        else:
            board_color = args[0].lower()
            color = color_to_int(board_color)
            move = self.go_engine.get_move(self.board, color)
            move_coord = point_to_coord(move, self.board.size)
            move_as_string = format_point(move_coord)
            if self.board.is_legal(move, color):
                self.board.play_move(move, color)
                self.respond(move_as_string.lower())
            else:
                self.respond("resign")

    def gogui_rules_game_id_cmd(self, args):
        self.respond("NoGo")

    def gogui_rules_board_size_cmd(self, args):
        self.respond(str(self.board.size))

    def legal_moves_cmd(self, args):
        """
            List legal moves for color args[0] in {'b','w'}
            """
        board_color = args[0].lower()
        color = color_to_int(board_color)
        moves = GoBoardUtil.generate_legal_moves(self.board, color)
        gtp_moves = []
        for move in moves:
            coords = point_to_coord(move, self.board.size)
            gtp_moves.append(format_point(coords))
        sorted_moves = ' '.join(sorted(gtp_moves))
        self.respond(sorted_moves)

    def gogui_rules_legal_moves_cmd(self, args):
        empties = self.board.get_empty_points()
        color = self.board.current_player
        legal_moves = []
        for move in empties:
            if self.board.is_legal(move, color):
                legal_moves.append(move)

        gtp_moves = []
        for move in legal_moves:
            coords = point_to_coord(move, self.board.size)
            gtp_moves.append(format_point(coords))
        sorted_moves = ' '.join(sorted(gtp_moves))
        self.respond(sorted_moves)

    def gogui_rules_side_to_move_cmd(self, args):
        color = "black" if self.board.current_player == BLACK else "white"
        self.respond(color)

    def gogui_rules_board_cmd(self, args):
        size = self.board.size
        str = ''
        for row in range(size-1, -1, -1):
            start = self.board.row_start(row + 1)
            for i in range(size):
                point = self.board.board[start + i]
                if point == BLACK:
                    str += 'X'
                elif point == WHITE:
                    str += 'O'
                elif point == EMPTY:
                    str += '.'
                else:
                    assert False
            str += '\n'
        self.respond(str)

    def gogui_rules_final_result_cmd(self, args):
        empties = self.board.get_empty_points()
        color = self.board.current_player
        legal_moves = []
        for move in empties:
            if self.board.is_legal(move, color):
                legal_moves.append(move)
        if not legal_moves:
            result = "black" if self.board.current_player == WHITE else "white"
        else:
            result = "unknown"
        self.respond(result)

    def gogui_analyze_cmd(self, args):
        self.respond("pstring/Legal Moves For ToPlay/gogui-rules_legal_moves\n"
                     "pstring/Side to Play/gogui-rules_side_to_move\n"
                     "pstring/Final Result/gogui-rules_final_result\n"
                     "pstring/Board Size/gogui-rules_board_size\n"
                     "pstring/Rules GameID/gogui-rules_game_id\n"
                     "pstring/Show Board/gogui-rules_board\n"
                     )

def point_to_coord(point, boardsize):
    """
    Transform point given as board array index
    to (row, col) coordinate representation.
    Special case: PASS is not transformed
    """
    if point == PASS:
        return PASS
    else:
        NS = boardsize + 1
        return divmod(point, NS)

def format_point(move):
    """
    Return move coordinates as a string such as 'a1', or 'pass'.
    """
    column_letters = "ABCDEFGHJKLMNOPQRSTUVWXYZ"
    #column_letters = "abcdefghjklmnopqrstuvwxyz"
    if move == PASS:
        return "pass"
    row, col = move
    if not 0 <= row < MAXSIZE or not 0 <= col < MAXSIZE:
        raise ValueError
    return column_letters[col - 1]+ str(row)

def move_to_coord(point_str, board_size):
    """
    Convert a string point_str representing a point, as specified by GTP,
    to a pair of coordinates (row, col) in range 1 .. board_size.
    Raises ValueError if point_str is invalid
    """
    if not 2 <= board_size <= MAXSIZE:
        raise ValueError("board_size out of range")
    s = point_str.lower()
    if s == "pass":
        return PASS
    try:
        col_c = s[0]
        if (not "a" <= col_c <= "z") or col_c == "i":
            raise ValueError
        col = ord(col_c) - ord("a")
        if col_c < "i":
            col += 1
        row = int(s[1:])
        if row < 1:
            raise ValueError
    except (IndexError, ValueError):
        # e.g. "a0"
        raise ValueError("wrong coordinate")
    if not (col <= board_size and row <= board_size):
        # e.g. "a20"
        raise ValueError("wrong coordinate")
    return row, col

def color_to_int(c):

    """convert character to the appropriate integer code"""
    color_to_int = {"b": BLACK , "w": WHITE, "e": EMPTY,
                    "BORDER": BORDER}
    return color_to_int[c]

class TimeoutException(Exception):
    def __init__(self, *args, **kwargs):
        pass
