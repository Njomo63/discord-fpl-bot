import unittest
from fpl import get_player_hist_data, get_player_data

class TestBot(unittest.TestCase):
    
    def test_player_data1(self):
        self.assertEqual(get_player_data("salahs"), "Incorrect entry.", "Should be incorect entry")

    def test_player_data2(self):
        res = (
            "Goals Scored: 23, "
            "Assists: 14, "
            "Yellow Cards: 1, "
            "Red Cards: 0, "
            "Points per game: 7.6"
        )
        self.assertEqual(get_player_data("salah"), res, f"Should be {res}")
    
    def test_palyer_hist1(self):
        res = "Player not present in that season"
        self.assertEqual(get_player_hist_data("hickey", 2), res, f"Should be {res}")

    def test_palyer_hist2(self):
        res = "Season Name: 2020/21, Goals: 22, Assists: 6, Total Points: 231"
        self.assertEqual(get_player_hist_data("salah", 2), res, f"Should be {res}")
    

if __name__ == '__main__':
    unittest.main()