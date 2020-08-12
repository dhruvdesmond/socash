import random


class Game:
    def __init__(self):
        self.cardColors = ["spade", "hearts", "diamonds", "clubs"]

        self.cardNumbers = ["2", "3", "4", "5", "6", "7",
                            "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.cardNumbersValues = {
            "2": 2, "3": 3, "4": 4, "5": 5,
            "6": 6, "7": 7,
            "8": 8, "9": 9, "10": 10,
            "Jack": 11, "Queen": 12,
            "King": 13, "Ace": 1
        }

        self.deckOfCards = []
        self.playerCards = {}

    def createDeck(self):
        deckOfCards = []

        for color in self.cardColors:
            for number in self.cardNumbers:
                currCard = number + " of " + color
                deckOfCards.append(currCard)

        return deckOfCards

    def distributeRandomCardsToPlayers(self):

        player = 0
        playerCards = {}
        while player < 4:
            currCards = 0
            playerCards[player] = []
            while currCards < 3:
                randomIndex = random.randint(0, 51)
                if self.deckOfCards[randomIndex] != -1:
                    playerCards[player].append(self.deckOfCards[randomIndex])
                    self.deckOfCards[randomIndex] = -1
                    currCards += 1

            player += 1

        return playerCards

    def checkFirstCondition(self):
        currWinner = -1
        cardsWinner = []
        currNumberWinner = -1
        for onePlayerCards in self.playerCards:
            currList = []
            for card in self.playerCards[onePlayerCards]:
                currNumber = self.cardNumbersValues[card.split(" ")[0]]
                currList.append(currNumber)
            currList.sort()

            if currList[0] == currList[-1]:
                if currList[0] > currNumberWinner:
                    currNumberWinner = currList[0]
                    currWinner = onePlayerCards
                    cardsWinner = self.playerCards[onePlayerCards]
        if currWinner != -1:
            print("player ", currWinner, " won because three same number")
            print(cardsWinner)
            return True
        return False

    def checkSecondCondition(self):

        currWinner = []
        cardsWinner = []
        currNumberWinner = -1

        for onePlayerCards in self.playerCards:
            currList = []
            for card in self.playerCards[onePlayerCards]:
                currNumber = self.cardNumbersValues[card.split(" ")[0]]
                currList.append(currNumber)
            currList.sort()

            if currList[0]+1 == currList[1] and currList[1]+1 == currList[2]:

                if currList[2] > currNumberWinner:
                    currNumberWinner = currList[2]
                    currWinner = [onePlayerCards]
                    cardsWinner = [self.playerCards[onePlayerCards]]
                elif currList[2] == currNumberWinner:
                    currWinner.append(onePlayerCards)
                    cardsWinner.append(self.playerCards[onePlayerCards])

        if len(currWinner) == 1:
            print("player ", currWinner[0], " won because three numbers are in consecutive sequence")
            print(cardsWinner[0])
            return True

        elif len(currWinner) > 1:
            return self.FaceOff(currWinner)

        return False

    def checkThirdCondition(self):
        currWinner = []
        cardsWinner = []
        currNumberWinner = -1

        for onePlayerCards in self.playerCards:
            currList = []
            for card in self.playerCards[onePlayerCards]:
                currNumber = self.cardNumbersValues[card.split(" ")[0]]
                currList.append(currNumber)
            currList.sort()
            if currList[0] == currList[1] or currList[1] == currList[2]:
                if  currList[1] > currNumberWinner:
                    currWinner = [onePlayerCards]
                    cardsWinner = [self.playerCards[onePlayerCards]]
                    currNumberWinner =  currList[1]
                elif currList[1] == currNumberWinner:
                    currWinner.append(onePlayerCards)
                    cardsWinner.append(self.playerCards[onePlayerCards])
                    currNumberWinner =  currList[1]

        if len(currWinner) == 1:
            print("player ",currWinner[0]," won  because two cards of same number")
            print(cardsWinner[0])
            return True

        elif len(currWinner) > 1:
            return self.FaceOff(currWinner)

        return False


    def checkFourthCondition(self):
        currWinner = []
        cardsWinner = []
        currNumberWinner = -1
        for onePlayerCards in self.playerCards:
            currList = []
            for card in self.playerCards[onePlayerCards]:
                currNumber = self.cardNumbersValues[card.split(" ")[0]]
                currList.append(currNumber)
            currList.sort()


            
            if  currList[2] > currNumberWinner:
                currWinner = [onePlayerCards]
                cardsWinner = [self.playerCards[onePlayerCards]]
                currNumberWinner =  currList[2]
            elif currList[2] == currNumberWinner:
                currWinner.append(onePlayerCards)
                cardsWinner.append(self.playerCards[onePlayerCards])
                currNumberWinner =  currList[2]

        if len(currWinner) == 1:
            print("player ",currWinner[0]," won because card of highest level")
            print(cardsWinner[0])
            return True

        elif len(currWinner) > 1:
            return self.FaceOff(currWinner)

        return False

    def FaceOff(self,currWinner):
        print("Face off between = ",end=" ")
        for x in currWinner:
            print("Player ",x,end=" ")
        print()

        cardsDrawed = []

        currWinnerList = []
        cardsWinner = []
        currNumberWinner = -1

        self.cardNumbersValues["Ace"] = 13

        for player in currWinner:
            drawCard = 1
            while True:
                randomIndex = random.randint(0, 51)
                if self.deckOfCards[randomIndex] != -1:
                    drawCard = self.deckOfCards[randomIndex]
                    print("Player ",player," drew card ",drawCard)
                    self.deckOfCards[randomIndex] = -1
                    if self.cardNumbersValues[drawCard.split(" ")[0]] > currNumberWinner:
                        currNumberWinner = self.cardNumbersValues[drawCard.split(" ")[0]]
                        currWinnerList = [player]
                        cardsWinner = [drawCard]
                        break
                    elif self.cardNumbersValues[drawCard.split(" ")[0]] == currNumberWinner:
                        currNumberWinner = self.cardNumbersValues[drawCard.split(" ")[0]]
                        currWinnerList.append([player])
                        cardsWinner.append([drawCard])
                        break
        

        if len(currWinnerList) == 1:
            print("player ",currWinnerList[0]," won with")
            print(cardsWinner[0])
            return True

        
        return self.FaceOff(currWinnerList)
        





    def findWinner(self):

        if(self.checkFirstCondition() == True):
            return True

        elif(self.checkSecondCondition() == True):
            return True

        elif(self.checkThirdCondition() == True):
            return True

        elif (self.checkFourthCondition() == True):
            return True

        return  self.FaceOff([0,1,2,3])

    def startGame(self):
        self.deckOfCards = self.createDeck()
        self.playerCards = self.distributeRandomCardsToPlayers()
        for i in range(4):

            print("Player ",i+1," cards = ",self.playerCards[i])


        self.findWinner()







# while True:
#     print("\nMenu\n(1)Start Game\n(2)Exit\n")
#     choice = int(input())

#     if choice == 1:
#         print("Start Game")
        
#         game = Game()
#         game.startGame()

#     elif choice == 2:
#         print("Thank you for playing,")

#         break
#     else:
#         print("Invalid choice, please choose again\n")
