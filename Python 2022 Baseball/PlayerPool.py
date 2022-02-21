from Player import Player
import pandas as pd
import Constants as c

class PlayerPool:

    def __init__(self):
        self.all_player_dict = {}

        self.catcher_list = []
        self.corner_list = []
        self.middle_list = []
        self.outfield_list = []
        self.dh_list = []
        self.pitcher_list = []

        self.parseDataFrames()
        self.sortPlayersByPosition()
        self.sortPositionLists()

        self.pos_list_dict = {c.CA:self.catcher_list, 
                              c.CI:self.corner_list, 
                              c.MI:self.middle_list, 
                              c.OF:self.outfield_list, 
                              c.DH:self.dh_list, 
                              c.PI:self.pitcher_list}

    def parseDataFrames(self):
        with pd.ExcelFile(c.EXCEL_SOURCE) as reader:
            catcher_df = pd.read_excel(reader, sheet_name=c.CA)[[c.NAME, c.POINTS]]
            corner_df = pd.read_excel(reader, sheet_name=c.CI)[[c.NAME, c.POINTS]]
            middle_df = pd.read_excel(reader, sheet_name=c.MI)[[c.NAME, c.POINTS]]
            outfield_df = pd.read_excel(reader, sheet_name=c.OF)[[c.NAME, c.POINTS]]
            dh_df = pd.read_excel(reader, sheet_name=c.DH)[[c.NAME, c.POINTS]]
            pitcher_df = pd.read_excel(reader, sheet_name=c.PI)[[c.NAME, c.POINTS]]

        df_dict = {c.CA:catcher_df, c.CI:corner_df, c.MI:middle_df, c.OF:outfield_df, c.DH:dh_df, c.PI:pitcher_df}
        position_list = df_dict.keys()
        
        for position in position_list:
            df = df_dict.get(position)
            for index, row in df.iterrows():
                self.addToList(row[c.NAME], float(row[c.POINTS]), position)


    def addToList(self, name, points, position):
        if name in self.all_player_dict:
            cur_player = self.all_player_dict.get(name)
            cur_player.addPosition(position)
            self.all_player_dict[name] = cur_player
        else:
            self.all_player_dict[name] = Player(name, points, position)

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
            if c.DH in player.positions:
                self.dh_list.append(player)
            if c.PI in player.positions:
                self.pitcher_list.append(player)
            

    def sortPositionLists(self):
        self.catcher_list.sort(key=lambda x: x.points, reverse=True)
        self.corner_list.sort(key=lambda x: x.points, reverse=True)
        self.middle_list.sort(key=lambda x: x.points, reverse=True)
        self.outfield_list.sort(key=lambda x: x.points, reverse=True)
        self.dh_list.sort(key=lambda x: x.points, reverse=True)
        self.pitcher_list.sort(key=lambda x: x.points, reverse=True)

            

           