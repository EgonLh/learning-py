players = ['egon','loth','florence','elly']
print(players[:3])
print(players[2:3])
print(players[1:])
print(players[:])
print(players[3:])
print("\n From Back..... \n")
print(players)
print(players[-3:])
print(players[:-2])
# start from -1 position to start
print(players[:-1])
# start end to -1
print(players[-1:])


for player in players[:2]:
    print("Name: "+player.title()) # title() to capitalize the first letter of each word