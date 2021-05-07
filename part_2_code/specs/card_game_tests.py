import unittest
from src.card import Card
from src.card_game import check_for_ace 
from src.card_game import highest_card
from src.card_game import cards_total

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card_1 = Card('Hearts', 1)
        self.card_2 = Card("Hearts", 2)
        self.card_3 = Card("Diamonds", 5)
        self.card_4 = Card("Diamonds", 4)
        self.card_5 = Card('Hearts', 4)


        self.cards = [self.card_1, self.card_2, self.card_3, self.card_3, self.card_4]
        self.cards_1 = [self.card_1]

    def test_check_for_ace(self):
        self.assertEqual(True, check_for_ace(self.card_1))

    def test_check_no_ace(self):
        self.assertEqual(False, check_for_ace(self.card_2))

    def test_check_highest_card_position_1(self):
        self.assertEqual(self.card_2, highest_card(self.card_2, self.card_1))

    def test_check_highest_card_comes_out_draw(self):
        self.assertEqual('its a draw', highest_card(self.card_4, self.card_5))

    def test_check_highest_card_position_2(self):
        self.assertEqual(self.card_3, highest_card(self.card_4, self.card_3))
    

    def test_cards_total(self):
        self.assertEqual("You have a total of 1", cards_total(self.cards_1))

    def test_cards_total_more_than_one(self):
        self.assertEqual("You have a total of 5", cards_total(self.cards))
