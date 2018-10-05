# modified 
import unittest
from transition import Board

class TestBoardMethods(unittest.TestCase):

    def setUp(self):
        self.threeX3List = [['X','X','X'],
                            ['.','.','.'],
                            ['O','O', 'O'],
                            ]
        self.threeX3Board = Board(self.threeX3List, 'X')
    
    def tearDown(self):
        pass

    #@unittest.skip("False value already tested")
    def test_is_valid_false(self):
        pairs_false = [[(0,0),(0,0)], # False, src = dst
                        [(0,0),(0,2)],   # False, two units, same row
                        [(0,0),(-1,0)],  # False, out of index
                        [(0,0),(0,1)],   # False, same row
                        [(0,0),(1,-1)],   # False, out of index
                        [(0,0),(1,2)],   # False, moving two units
                        [(0,0),(2,0)],   # False, moving two units
                        [(0,0),(2,2)],   # False, moving two units
                        [(0,0),(11,11)]   # False, out of index
                        ]
        for pair in pairs_false:
            with self.subTest(pair=pair):
                self.assertIs(self.threeX3Board.is_valid(pair[0],pair[1]), False)

    #@unittest.skip("False value already tested")
    def test_is_valid_true(self):
        pairs_true = [[(0,0),(1,0)], # True, forward
                        [(0,0),(1,1)],   # True, diagonal left
                        [(0,1),(1,0)],  # True, diagonal left
                        [(0,1),(1,1)],   # True, forward
                        [(0,1),(1,2)],   # True, diagonal right
                        [(2,0),(1,0)],   # True, forward
                        [(2,0),(1,1)],   # True, diagonal right
                        [(2,2),(1,2)],   # False, forward
                        [(2,1),(1,0)]   # True, diagonal left
                        ]
        for pair in pairs_true:
            with self.subTest(pair=pair):
                self.assertTrue(self.threeX3Board.is_valid(pair[0],pair[1]))

    #@unittest.skip("False value already tested")
    def test_get_moves_returns_empty(self):
        # For point where the returned list will be empty
        dots = [(1,0),     # [], no player, column-0
                (1,1),     # [], no player, middle
                (1,2)      # [], no player, rightmost column
                    ] 

        for each in dots:
            with self.subTest(each=each):
                self.assertEqual(self.threeX3Board.get_moves(each), [])

    #@unittest.skip("False value already tested")
    def test_get_moves_for_playerO_at_positions(self):
        # For point where the returned list will be empty
        dots = [(2,0),     # [], playerO, column-0
                (2,1),     # [], playerO, middle
                (2,2)      # [], playerO, rightmost column
                    ] 
        self.assertEqual(self.threeX3Board.get_moves(dots[0]), [(1,0),(1,1)])
        self.assertEqual(self.threeX3Board.get_moves(dots[1]), [(1,0),(1,1),(1,2)])
        self.assertEqual(self.threeX3Board.get_moves(dots[2]), [(1,1),(1,2)])

    #@unittest.skip("False value already tested")
    def test_get_moves_for_playerX_at_positions(self):
        # For point where the returned list will be empty
        dots = [(0,0),     # [], playerX, column-0
                (0,1),     # [], playerX, middle
                (0,2)      # [], playerX, rightmost column
                    ] 
        self.assertEqual(self.threeX3Board.get_moves(dots[0]), [(1,0),(1,1)])
        self.assertEqual(self.threeX3Board.get_moves(dots[1]), [(1,0),(1,1),(1,2)])
        self.assertEqual(self.threeX3Board.get_moves(dots[2]), [(1,1),(1,2)])

    def test_all_moves_for_playerX(self):
        """Supposed to return a dictionary with (x,y):['L','F','R']"""
        self.assertCountEqual(self.threeX3Board.all_moves('X')[(0,0)], ['L', 'F'])        
        self.assertCountEqual(self.threeX3Board.all_moves('X')[(0,1)], ['L','F','R'])
        self.assertCountEqual(self.threeX3Board.all_moves('X')[(0,2)], ['F','R']) 
        # The syntax does not seem to be working
        # self.assertRaises(TypeError, self.threeX3Board.all_moves(), 'G')
    
    def test_move_forward(self):
        old_new_pairs = [[(0,0),(1,0)],
                         [(2,0),(1,0)],
                         [(0,1),(1,1)],
                         [(2,1),(1,1)],
                         [(0,2),(1,2)],
                         [(2,2),(1,2)]
                        ]

        for pair in old_new_pairs:
            with self.subTest(pair = pair):
                player = self.threeX3Board.get_sym(pair[0])
                self.threeX3Board.move(pair[0], 'F')
                self.assertIs(self.threeX3Board.get_sym((pair[0])), '.')    # emptied
                self.assertIs(self.threeX3Board.get_sym((pair[1])), player)    # newly occupied

    def test_move_dright_playerO(self):
        pass

    def test_move_dleft_for_playerO(self):
        pass


if __name__ == '__main__':
    unittest.main()
