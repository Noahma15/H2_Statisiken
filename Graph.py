import csv
import matplotlib.pyplot as plt

reader = csv.reader(open("stats_all.csv", "r"), delimiter=";")
stats_all = list(reader)

specific_stat = 3
specific_player = 17

######################  Correspondens table    ############################################################################
#                                                                                                                         #
#                                                                                                                         #
######################  Stats   ###########################################################################################
#                                                                                                                         #
# 0 = Attack Kills; 1 = Attack Errors ; 2 = Attack Attempts; 3 = Attack Atk%; 4 = Attack K/S; 5 = Attack ?; 6 = Serve Ace;#
# 7 = Serve Error; 8 = Serve Attempts; 9 = Serve Pct; 10 = Serve Eff; 11 = Serve Rtg.; 12 = Serve ?; 13 = Receive 3;      #
# 14 = Receive 2; 15 = Receive 1; 16 = Receive 0; 17 = Receive Attempts; 18 = Receive ?; 19 = Receive Pass%; 20 = Set Ast;#
# 21 = Set Attempts; 22 = Set Errors; 23 = Dig Succesful; 24 = Dig Error; 25 = Block Kill; 26 = Block Attempts;           #
# 27 = Block Error; 28 = Block B/S; 29 = Sets Played                                                                      #
#                                                                                                                         #
######################  Players   #########################################################################################
# 0 = Jens, 1 = Luiz, 2 = Alex, 3 = Elias, 4 = Chris, 5 = Sebi, 6 = Simon, 7 = Steffen, 8 = Lukas, 9 = Marcel,            #
# 10 = Marian, 11 = Noah, 12 = Flo, 13 = Basti, 14 = Martin, 15 = Joel, 16 = Dirk, 17 = Herrn 2, 18 = Gegner              #                                                                                                                         #
#                                                                                                                         #
###########################################################################################################################

#misc variables 
average_stat = 0
times_played = 0
stat_cumulative = 0
specific_player_iterate = specific_player
game_array = []
game_stats_array = []
list_playerNames = ['Jens','Luiz','Alex','Elias','Chris','Sebi','Simon','Steffen','Lukas','Marcel','Marian','Noah','Flo',
                    'Basti','Martin','Joel','Dirk','Herrn 2','Gegner']
list_opponents = ['Botnang - Hinspiel','Untersteinbach - Hinspiel','Kornwestheim - Hinspiel','Stromberg - Hinspiel','AlliH3 - Rückspiel',
                  'ASVBotnang - Rückspiel','Geißelhardt - Rückspiel','Stromberg - Rückspiel','Untersteinbach - Rückspiel',
                  'Willsbach - Rückspiel','Kornwestheim - Rückspiel']
list_of_stats = ['Attack Kills','Attack Errors','Attack Attempts','Attack Atk%','Attack K/S',' Attack ?','Serve Ace','Serve Error',
                'Serve Attempts','Serve Pct','Serve Eff','Serve Rtg.','Serve ?','Receive 3','Receive 2','Receive 1','Receive 0',
                'Receive Attempts','Receive ?','Receive Pass%','Set Ast','Set Attempts','Set Errors','Dig Succesful','Dig Error',
                'Block Kill','Block Attempts ','Block Error ','Block B/S ','Sets Played']

for i in range(11):
    stat = float(stats_all[specific_player_iterate][specific_stat])
    if stat == -100: #checks if person played
        stat_cumulative  +=0
        game_array.append(0)
        game_stats_array.append(0)
    else:
        stat_cumulative  +=stat
        times_played +=1
        game_array.append(1)
        game_stats_array.append(stat)

    specific_player_iterate += 19

average_stat = stat_cumulative/times_played

plt.plot(range(11),game_stats_array)
plt.title('Statiskik: '+ list_of_stats[specific_stat] +'; Spieler: '+ list_playerNames[specific_player]+ '; Durchscnitt: '+str(round(average_stat,3))) 
plt.grid(True)
plt.show()