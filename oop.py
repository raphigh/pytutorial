from SoccerPlayer import Player
player1 = Player('messi',32,'barcelona',False)
player2 = Player('ostad asadi',55,'zob ahan',True)
print(player1.name)
print(player2.name)
print(player1.get_status())
player2.injured = False
print(player2.get_status())