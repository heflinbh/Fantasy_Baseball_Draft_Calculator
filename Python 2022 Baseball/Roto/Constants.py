EXCEL_SOURCE = "/Users/benjaminheflin/Desktop/Baseball/Baseball 2021.xlsx"

NUM_TEAMS = 8
BUDGET_PER_TEAM = 273
NUM_PLAYERS_PER_TEAM = 27

CA = "C"
CI = "1B3B"
MI = "2BSS"
OF = "OF"
DH = "DH"
PI = "P"

POSITION_LIST = [CA, CI, MI, OF, DH, PI]

CA_PER_TEAM = 1
CI_PER_TEAM = 3
MI_PER_TEAM = 3
OF_PER_TEAM = 5
DH_PER_TEAM = 1
PI_PER_TEAM = 9

NUM_POS_PER_TEAM = {
            CA:CA_PER_TEAM,
            CI:CI_PER_TEAM,
            MI:MI_PER_TEAM,
            OF:OF_PER_TEAM,
            DH:DH_PER_TEAM,
            PI:PI_PER_TEAM
        }

NAME = "Name"
HITS = "Hits"
AB = "AtBats"
HR = "HR"
RBI = "RBI"
SB = "SB"
RUNS = "Runs"
IP = "Innings Pitched"
WINS = "Wins"
BB = "Walks"
SO = "Strikeouts"
SAVES = "Saves"

AVG = "Average"
ERA = "ERA"
WHIP = "WHIP"

BATTING_CATEGORIES = [AVG, HR, RBI, SB, RUNS]
PITCHING_CATEGOTIES = [ERA, WINS, WHIP, SO, SAVES]


