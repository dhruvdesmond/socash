import unittest
from socash import Game

class TestSocash(unittest.TestCase):


    def test_createDeck(self):

        game = Game()
        cardsDeck = game.createDeck()

        self.assertEqual(len(cardsDeck),52)



    def test_checkFirstCondition(self):
        game = Game()
        game.deckOfCards = game.createDeck()
        game.playerCards = game.distributeRandomCardsToPlayers()
        game.playerCards[0] = ['3 of spade', '3 of hearts', '3 of diamonds']
        game.playerCards[1] = ['5 of spade', '6 of diamonds', 'King of hearts']
        game.playerCards[2] = ['King of clubs', '3 of spade', 'Queen of diamonds']
        game.playerCards[3] = ['5 of hearts', '5 of diamonds', '5 of spade']
        res = game.checkFirstCondition()

        self.assertEqual(res,True)

    def test_checkSecondCondition(self):
        game = Game()
        game.deckOfCards = game.createDeck()
        game.playerCards = game.distributeRandomCardsToPlayers()
        game.playerCards[0] = ['3 of spade', '3 of hearts', '3 of diamonds']
        game.playerCards[1] = ['5 of spade', '6 of diamonds', 'King of hearts']
        game.playerCards[2] = ['King of clubs', '5 of spade', 'Queen of diamonds']
        game.playerCards[3] = ['5 of hearts', '6 of diamonds', '7 of spade']
        res = game.checkSecondCondition()

        self.assertEqual(res,True)


    def test_checkThirdCondition(self):
        game = Game()
        game.deckOfCards = game.createDeck()
        game.playerCards = game.distributeRandomCardsToPlayers()
        game.playerCards[0] = ['4 of spade', '2 of hearts', '3 of diamonds']
        game.playerCards[1] = ['5 of spade', '6 of diamonds', 'King of hearts']
        game.playerCards[2] = ['King of clubs', 'Queen of spade', 'Queen of diamonds']
        game.playerCards[3] = ['5 of hearts', '2 of diamonds', '7 of spade']
        res = game.checkThirdCondition()

        self.assertEqual(res,True)



    def test_checkFourthCondition(self):
        game = Game()
        game.deckOfCards = game.createDeck()
        game.playerCards = game.distributeRandomCardsToPlayers()
        game.playerCards[0] = ['4 of spade', '6 of hearts', '3 of diamonds']
        game.playerCards[1] = ['5 of spade', '2 of diamonds', 'King of hearts']
        game.playerCards[2] = ['King of clubs', '5 of spade', '8 of diamonds']
        game.playerCards[3] = ['5 of hearts', '2 of diamonds', '7 of spade']
        res = game.checkFourthCondition()

        self.assertEqual(res,True)



if __name__ == '__main__':
    unittest.main()

