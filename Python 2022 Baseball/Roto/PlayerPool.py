from Batter import Batter
from Pitcher import Pitcher
import pandas as pd
import Constants as c

class PlayerPool:

    def __init__(self):
        self.all_player_dict = {}

        self.catcher_list = []
        self.corner_list = []
        self.middle_list = []
        self.outfield_list = []
        self.pitcher_list = []

        self.parseDataFrames()
        self.sortPlayersByPosition()

        self.pos_list_dict = {c.CA:self.catcher_list, 
                              c.CI:self.corner_list, 
                              c.MI:self.middle_list, 
                              c.OF:self.outfield_list,  
                              c.PI:self.pitcher_list}

    def parseDataFrames(self):
        with pd.ExcelFile(c.EXCEL_SOURCE) as reader:
            catcher_df = pd.read_excel(reader, sheet_name=c.CA)[[c.NAME, c.HITS, c.AB, c.HR, c.RBI, c.SB, c.RUNS]]
            corner_df = pd.read_excel(reader, sheet_name=c.CI)[[c.NAME, c.HITS, c.AB, c.HR, c.RBI, c.SB, c.RUNS]]
            middle_df = pd.read_excel(reader, sheet_name=c.MI)[[c.NAME, c.HITS, c.AB, c.HR, c.RBI, c.SB, c.RUNS]]
            outfield_df = pd.read_excel(reader, sheet_name=c.OF)[[c.NAME, c.HITS, c.AB, c.HR, c.RBI, c.SB, c.RUNS]]
            pitcher_df = pd.read_excel(reader, sheet_name=c.PI)[[c.NAME, c.RUNS, c.IP, c.WINS, c.HITS, c.BB, c.SO, c.SAVES]]

        df_dict = {c.CA:catcher_df, c.CI:corner_df, c.MI:middle_df, c.OF:outfield_df, c.PI:pitcher_df}
        position_list = df_dict.keys()
        
        for position in position_list:
            df = df_dict.get(position)
            for index, row in df.iterrows():
                if position == c.PI:
                    self.addToList(row[c.NAME], 
                                float(row[c.RUNS]), 
                                float(row[c.IP]), 
                                float(row[c.WINS]), 
                                float(row[c.HITS]),
                                float(row[c.BB]),
                                float(row[c.SO]),
                                float(row[c.SAVES]),
                                position)
                else:
                    self.addToList(row[c.NAME], 
                                float(row[c.HITS]), 
                                float(row[c.AB]), 
                                float(row[c.HR]), 
                                float(row[c.RBI]),
                                float(row[c.SB]),
                                float(row[c.RUNS]),
                                position)

    # For Pitchers
    def addToList(self, name, runs, inningsPitched, wins, hits, walks, strikeouts, saves, position):
        if name in self.all_player_dict:
            cur_player = self.all_player_dict.get(name)
            cur_player.addPosition(position)
            self.all_player_dict[name] = cur_player
        else:
            self.all_player_dict[name] = Pitcher(name, position, runs, inningsPitched, wins, hits, walks, strikeouts, saves)

    # For Batters
    def addToList(self, name, hits, atBats, homeRuns, rbi, stolenBases, runs, position):
        if name in self.all_player_dict:
            cur_player = self.all_player_dict.get(name)
            cur_player.addPosition(position)
            self.all_player_dict[name] = cur_player
        else:
            self.all_player_dict[name] = Batter(name, position, hits, atBats, homeRuns, rbi, stolenBases, runs)

    def sortPlayersByPosition(self):
        for player in self.all_player_dict.values():

            if c.CA in player.positions:
                self.catcher_list.append(player)
            if c.CI in player.positions:
                self.corner_list.append(player)
            if c.MI in player.positions:
                self.middle_list.append(player)
            if c.OF in player.positions:
                self.outfield_list.append(player)
            if c.PI in player.positions:
                self.pitcher_list.append(player)
            

           