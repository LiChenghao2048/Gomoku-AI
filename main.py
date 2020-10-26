from Rules import *
from Strategy import *
from GameMode import *

#multiPlayers(9)
#singlePlayer(15, 0)
#battleAI(15, 2, 0)


blackSide = []
whiteSide = []
for i in range(20):
    blackSide.append(battleAI(15, 0, 2))
    whiteSide.append(battleAI(15, 2, 0))
    print(matchHistory)



# ['X', 'X', 'O', 'O', 'X', 'O', 'X', 'O', 'X', 'X', 'O', 'O', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'O'] 55%
# ['X', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'] 90%


# ['X', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'] 85%   (0, 2)
# ['O', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'] 90%   (2, 0)

# ['X', 'O', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X'] 85%   (2, 1)
# ['X', 'X', 'X', 'O', 'X', 'X', 'X', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X', 'O'] 60%   (1, 2)

# ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'O', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'] 95%   (0, 1)
# ['X', 'O', 'X', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'O', 'X', 'O', 'O', 'O', 'X', 'O', 'O', 'X', 'O'] 70%   (1, 0)

# ['X', 'O', 'X', 'O', 'X', 'X', 'O', 'O', 'X', 'X', 'X', 'O', 'O', 'X', 'O', 'O', 'O', 'X', 'O', 'O']   (1, 1)