"""
pattern_util.py
Utility functions for rule based simulations.
"""

import numpy as np
from pattern import *
import random

from board_util import GoBoardUtil, EMPTY, PASS, BORDER, WHITE, coord_to_point
import linecache
import gtp_connection as gtp

class PatternUtil(object):

    @staticmethod
    def neighborhood_33(board, point):
        """
        Get the pattern around point.
        Returns
        -------
        patterns :
        Set of patterns in the same format of what michi pattern base provides. Please refer to pattern.py to see the format of the pattern.
        """
        positions = [point-board.NS-1, point-board.NS, point-board.NS+1,
                     point-1, point, point+1,
                     point+board.NS-1, point+board.NS, point+board.NS+1]

        pattern = ""
        #print(board.current_player)
        for d in positions:
            if board.board[d] == board.current_player:
                pattern += 'X'
            elif board.board[d] == GoBoardUtil.opponent(board.current_player):
                pattern += 'x'
            elif board.board[d] == EMPTY:
                pattern += '.'
            elif board.board[d] == BORDER:
                pattern += ' '
            #print(pattern)
        return pattern

    @staticmethod
    def generate_pattern_moves(board):
        """
        Generate a list of moves that match pattern.
        This only checks moves that are neighbors of the moves in the last two steps.
        See last_moves_empty_neighbors() in simple_board for detail.
        """
        color = board.current_player
        pattern_checking_set = board.last_moves_empty_neighbors()
        moves = []
        for p in pattern_checking_set:
            if (PatternUtil.neighborhood_33(board, p) in pat3set):
                assert p not in moves
                assert board.board[p] == EMPTY
                moves.append(p)
        return moves

    @staticmethod
    def filter_moves_and_generate(board, moves, check_selfatari):
        """
        Move filter function.
        """
        color = board.current_player
        while len(moves) > 0:
            candidate = random.choice(moves)
            if PatternUtil.filter(board, candidate, color, check_selfatari):
                moves.remove(candidate)
            else:
                return candidate
        return None

    @staticmethod
    def filter_moves(board, moves, check_selfatari):
        color = board.current_player
        good_moves = []
        for move in moves:
            if not PatternUtil.filter(board,move,color,check_selfatari):
                good_moves.append(move)
        return good_moves

    # return True if move should be filtered
    @staticmethod
    def filleye_filter(board, move, color):
        assert move != None
        return not board.is_legal(move, color)

    # return True if move should be filtered
    @staticmethod
    def selfatari_filter(board, move, color):
        return (  PatternUtil.filleye_filter(board, move, color)
                or PatternUtil.selfatari(board, move, color)
                )

    # return True if move should be filtered
    @staticmethod
    def filter(board, move, color, check_selfatari):
        if check_selfatari:
            return PatternUtil.selfatari_filter(board, move, color)
        else:
            return PatternUtil.filleye_filter(board, move, color)

    @staticmethod
    def selfatari(board, move, color):
        max_old_liberty = PatternUtil.blocks_max_liberty(board, move, color, 2)
        if max_old_liberty > 2:
            return False
        cboard = board.copy()
        # swap out true board for simulation board, and try to play the move
        isLegal = cboard.play_move(move, color)
        if isLegal:
            new_liberty = cboard._liberty(move, color)
            if new_liberty==1:
                return True
        return False

    @staticmethod
    def blocks_max_liberty(board, point, color, limit):
        assert board.board[point] == EMPTY
        max_lib = -1 # will return this value if this point is a new block
        neighbors = board._neighbors(point)
        for n in neighbors:
            if board.board[n] == color:
                num_lib = board._liberty(n, color)
                if num_lib > limit:
                    return num_lib
                if num_lib > max_lib:
                    max_lib = num_lib
        return max_lib

    @staticmethod
    def generate_move_with_filter(board, use_pattern, check_selfatari):
        """
        Arguments
        ---------
        check_selfatari: filter selfatari moves?
        Note that even if True, this filter only applies to pattern moves
        use_pattern: Use pattern policy?
        """
        move = None
        if use_pattern:
            moves,_ = PatternUtil.pattern(board)
            move = PatternUtil.filter_moves_and_generate(board, moves,
                                                         check_selfatari)
        if move == None:
            move = GoBoardUtil.generate_random_move(board, board.current_player,False)
        return move

    @staticmethod
    def generate_all_policy_moves(board, pattern, check_selfatari):
        """
        generate a list of policy moves on board for board.current_player.
        Use in UI only. For playing, use generate_move_with_filter
        which is more efficient
        """
        if pattern:
            pattern_moves = []
            pattern_moves = PatternUtil.generate_pattern_moves(board)
            pattern_moves = PatternUtil.filter_moves(board, pattern_moves, check_selfatari)
            if len(pattern_moves) > 0:
                return pattern_moves, "Pattern"
        return GoBoardUtil.generate_random_moves(board, True), "Random"

    @staticmethod
    def playGame(board, color, **kwargs):
        """
        Run a simulation game according to give parameters.
        """
        komi = kwargs.pop('komi', 0)
        limit = kwargs.pop('limit', 1000)
        random_simulation = kwargs.pop('random_simulation',True)
        use_pattern = kwargs.pop('use_pattern',True)
        check_selfatari = kwargs.pop('check_selfatari',True)
        if kwargs:
            raise TypeError('Unexpected **kwargs: %r' % kwargs)
        nuPasses = 0
        for _ in range(limit):
            color = board.current_player
            if random_simulation:
                move = GoBoardUtil.generate_random_move(board,color,False)
            else:
                move = PatternUtil.generate_move_with_filter(board,use_pattern,check_selfatari)
            if move == PASS:
                return GoBoardUtil.opponent(color)
            board.play_move(move, color)
        return board.current_player

    @staticmethod
    def pattern(state, move):
        #get legal moves
        """first_moves = GoBoardUtil.generate_legal_moves(state, state.current_player)
        moves =[]
        #convert points to formated
        for move in first_moves:
            #convert to coords
            temp = gtp.point_to_coord(move, state.size)
            #format version
            temp = gtp.format_point(temp)
            moves.append(temp)
        moves.sort()

        #reverse it
        new_moves =[]
        column_letters = "ABCDEFGHJKLMNOPQRSTUVWXYZ"
        #put format to point
        for move in moves:
            temp = str(column_letters.find(move[0])+1)
            temp = coord_to_point(int(move[1]),int(temp), state.size)
            new_moves.append((temp))

        moves = new_moves"""


        check = PatternUtil.neighborhood_33(state, move)
        tonum = check[0] + check[1] + check[2] + check[3] + check[5] + check[6] + check[7] + check[8]
        convertnum = 0
        count = 0
        #print(tonum)
        #tonum = tonum[::-1]
        ##print(tonum)
        #print((len(tonum)-1))
        """turn X,O,., into ints, multiply by 4, raise to power of index"""
        for y in range((len(tonum)-1), -1, -1):
            if state.current_player == WHITE:
                #print("white")
                if tonum[y] == ".":
                    convertnum = convertnum + 0*(4**count)
                elif tonum[y] == "x":
                    convertnum = convertnum + 1*(4**count)
                elif tonum[y] == "X":
                    convertnum = convertnum + 2*(4**count)
                else:
                    convertnum = convertnum + 3*(4**count)
            else:
                #print("black")
                if tonum[y] == ".":
                    convertnum = convertnum + 0*(4**count)
                elif tonum[y] == "X":
                    convertnum = convertnum + 1*(4**count)
                elif tonum[y] == "x":
                    convertnum = convertnum + 2*(4**count)
                else:
                    convertnum = convertnum + 3*(4**count)
            count = count + 1
            #print(count)
            #print(convertnum)
        w = linecache.getline('weights',convertnum+1).split()
        return float(w[1])
        """numlist.append(float(w[1]))
        #print(numlist)
        dem = sum(numlist)
        #print(dem)
        max = len(numlist)
        for x in range(0, max):
            numlist.append(round(numlist.pop(0)/float(dem), 3))
        #print(pmoves, numlist)
        return pmoves, numlist"""
