import unittest
from unittest.mock import patch

from ahorcado import Ahorcado


class TestAhoracado(unittest.TestCase):
#    @patch('ahorcado.choice', return_value='PERRO')
    def test_init(self):
        game = Ahorcado('PERRO')
        self.assertEqual(game.secret_word, 'PERRO')
        self.assertEqual(game.used_letters, [])
#
#    @patch('ahorcado.choice', return_value='PERRO')
    def test_play_missing_letter(self):
        game = Ahorcado('PERRO')
        game.play('A')
        self.assertEqual(game.used_letters, ['A'])
#
#    @patch('ahorcado.choice', return_value='PERRO')
    def test_play_missing_letter_twice(self):
        game = Ahorcado('PERRO')
        game.play('A')
        game.play('A')
        self.assertEqual(game.used_letters, ['A'])
#
#    @patch('ahorcado.choice', return_value='PERRO')
    def test_board_initial(self):
        game = Ahorcado('PERRO')
        self.assertEqual(game.board, '_ _ _ _ _')
#
#    @patch('ahorcado.choice', return_value='PERRO')
    def test_board_play_wrong(self):
        game = Ahorcado('PERRO')
        game.play('A')
        self.assertEqual(game.board, '_ _ _ _ _')
#
#    @patch('ahorcado.choice', return_value='PERRO')
    def test_board_play_well(self):
        game = Ahorcado('PERRO')
        game.play('E')
        self.assertEqual(game.board, '_ E _ _ _')
        self.assertEqual(game.used_letters, ['E'])
#
#    @patch('ahorcado.choice', return_value='PERRO')
    def test_board_play_well_tweice(self):
        game = Ahorcado('PERRO')
        game.play('E')
        game.play('R')
        self.assertEqual(game.used_letters, ['E', 'R'])
        self.assertEqual(game.board, '_ E R R _')
#
#    @patch('ahorcado.choice', return_value='PERRO')
    def test_lifes_left(self):
        game = Ahorcado('PERRO')
        self.assertEqual(game.lifes_left, 6)
        game.play('E')
        game.play('R')
        self.assertEqual(game.lifes_left, 6)
        game.play('A')
        self.assertEqual(game.lifes_left, 5)
        game.play('A')
        self.assertEqual(game.lifes_left, 5)
        game.play('L')
        self.assertEqual(game.lifes_left, 4)
        game.play('S')
        self.assertEqual(game.lifes_left, 3)
        game.play('Q')
        self.assertEqual(game.lifes_left, 2)
        game.play('I')
        self.assertEqual(game.lifes_left, 1)
        game.play('K')
        self.assertEqual(game.lifes_left, 0)
        game.play('N')
        self.assertEqual(game.lifes_left, 0)
#
#    @patch('ahorcado.choice', return_value='PERRO')
    def test_game_over(self):
        game = Ahorcado('PERRO')
        self.assertEqual(game.lifes_left, 6)
        self.assertFalse(game.is_over)
        game.play('E')
        game.play('R')
        self.assertEqual(game.lifes_left, 6)
        self.assertFalse(game.is_over)
        game.play('A')
        self.assertEqual(game.lifes_left, 5)
        self.assertFalse(game.is_over)
        game.play('A')
        self.assertEqual(game.lifes_left, 5)
        self.assertFalse(game.is_over)
        game.play('L')
        self.assertEqual(game.lifes_left, 4)
        self.assertFalse(game.is_over)
        game.play('S')
        self.assertEqual(game.lifes_left, 3)
        self.assertFalse(game.is_over)
        game.play('Q')
        self.assertEqual(game.lifes_left, 2)
        self.assertFalse(game.is_over)
        game.play('I')
        self.assertEqual(game.lifes_left, 1)
        self.assertFalse(game.is_over)
        game.play('K')
        self.assertEqual(game.lifes_left, 0)
        self.assertTrue(game.is_over)
        game.play('N')
        self.assertEqual(game.lifes_left, 0)
        self.assertTrue(game.is_over)
#
#    @patch('ahorcado.choice', return_value='PERRO')
    def test_game_win(self):
        game = Ahorcado('PERRO')
        self.assertFalse(game.win)
        game.play('P')
        self.assertFalse(game.win)
        game.play('E')
        self.assertFalse(game.win)
        game.play('R')
        self.assertFalse(game.win)
        game.play('O')
        self.assertTrue(game.win)
#
if __name__ == '__main__':
    unittest.main()