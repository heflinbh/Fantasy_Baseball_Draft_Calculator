from PlayerPool import PlayerPool
import Constants as c

class CostCalculator:

    def __init__(self):

        self.player_pool = PlayerPool()
        self.benchmark_dict = self.getBenchmark()
        self.pos_cat_player_par_dict = self.getParPerPosition()
        self.par_all_player_dict, self.total_par_dict = self.getParAll()
        self.player_value_dict = self.getValue()


    def getBenchmark(self):

        benchmarks = {}

        for position in c.POSITION_LIST:
            curr_list = self.player_pool.pos_list_dict.get(position)
            worst_index = (c.NUM_POS_PER_TEAM.get(position) * (c.NUM_TEAMS - 1)) - 1

            if position == c.PI:
                for category in c.PITCHING_CATEGOTIES:
                    if category == c.WINS:
                        curr_list = self.sortByWins(curr_list)
                        wins_benchmark = curr_list[worst_index].wins

                    elif category == c.SO:
                        curr_list = self.sortByStrikeouts(curr_list)
                        strikeouts_benchmark = curr_list[worst_index].strikeouts

                    elif category == c.SAVES:
                        curr_list = self.sortBySaves(curr_list)
                        saves_benchmark = curr_list[worst_index].saves

                    elif category == c.ERA:
                        curr_list = self.sortByEra(curr_list)
                        era_benchmark = curr_list[worst_index].era_helper

                    elif category == c.WHIP:
                        curr_list = self.sortByWhip(curr_list)
                        whip_benchmark = curr_list[worst_index].whip_helper

                benchmarks[position] = {c.WINS:wins_benchmark, 
                                        c.SO:strikeouts_benchmark,
                                        c.SAVES:saves_benchmark,
                                        c.ERA:era_benchmark,
                                        c.WHIP:whip_benchmark}

            else:
                for category in c.BATTING_CATEGORIES:
                    if category == c.HR:
                        curr_list = self.sortByHomeRuns(curr_list)
                        home_run_benchmark = curr_list[worst_index].homeRuns

                    elif category == c.RBI:
                        curr_list = self.sortByRBI(curr_list)
                        rbi_benchmark = curr_list[worst_index].rbi

                    elif category == c.SB:
                        curr_list = self.sortByStolenBases(curr_list)
                        stolen_bases_benchmark = curr_list[worst_index].stolenBases

                    elif category == c.RUNS:
                        curr_list = self.sortByRuns(curr_list)
                        runs_benchmark = curr_list[worst_index].runs

                    elif category == c.AVG:
                        curr_list = self.sortByAverage(curr_list)
                        batting_average_benchmark = curr_list[worst_index].average_helper
                        return 0

                benchmarks[position] = {c.AVG:batting_average_benchmark, 
                                        c.HR:home_run_benchmark,
                                        c.RBI:rbi_benchmark,
                                        c.SB:stolen_bases_benchmark,
                                        c.RUNS:runs_benchmark}

        return benchmarks

    def getParPerPosition(self):

        pos_player_par_dict = {}
        for position in c.POSITION_LIST:

            curr_list = self.player_pool.pos_list_dict.get(position)
            pos_benchmark_dict = self.benchmark_dict.get(position)

            if position == c.PI:
                category_list = c.PITCHING_CATEGOTIES
            else:
                category_list = c.BATTING_CATEGORIES

            player_par_dict = {}
            for player in curr_list:
                category_dict = {}

                for category in category_list:
                    benchmark = pos_benchmark_dict.get(category)
                    category_par = self.getPAR(player, category, benchmark)

                    category_dict[category] = category_par
                player_par_dict[player] = category_dict
            pos_player_par_dict[position] = player_par_dict

        return pos_player_par_dict

    def getParAll(self):

        par_dict = {}
        total_par_per_category = {c.AVG:0, c.HR:0, c.RBI:0, c.SB:0, c.RUNS:0, c.ERA:0, c.WINS:0, c.WHIP:0, c.SO:0, c.SAVES:0}

        for position in self.pos_cat_player_par_dict:
            temp_dict = self.pos_cat_player_par_dict.get(position)

            for player in temp_dict:
                player_par_actual = {}
                for category in player:
                    new_cat_par = temp_dict.get(player).get(category)

                    if player not in par_dict:
                        if new_cat_par > 0:
                            total_par_per_category[category] = new_cat_par + total_par_per_category.get(category)
                        player_par_actual[category] = new_cat_par

                    elif par_dict.get(player).get(category) < new_cat_par:
                        if new_cat_par > 0:
                            total_par_per_category[category] = total_par_per_category.get(category) - par_dict.get(player).get(category) + new_cat_par
                        player_par_actual[category] = new_cat_par
                        
                par_dict[player] = player_par_actual

        return par_dict, total_par_per_category


    def getValue(self):

        total_money = (c.BUDGET_PER_TEAM - c.NUM_PLAYERS_PER_TEAM) * c.NUM_TEAMS
        dollars_per_category = float(total_money) / 10.0

        par_to_dollars = {}
        for category in self.total_par_dict:
            dollar_per_stat = float(dollars_per_category) / float(self.total_par_dict.get(category))
            par_to_dollars[category] = dollar_per_stat

        value_dict = {}
        for player in self.par_all_player_dict:
            cat_dict = {}
            for category in player:
                cat_dict[category] = player.get(category) * par_to_dollars.get(category)
            value_dict[player] = cat_dict
                    
        return value_dict


                
    def getPAR(self, player, category, benchmark):
        if category == c.AVG:
            stat = player.average_helper
        elif category == c.HR:
            stat = player.home_runs
        elif category == c.RBI:
            stat = player.rbi
        elif category == c.SB:
            stat = player.stolenBases
        elif category == c.RUNS:
            stat = player.runs

        elif category == c.ERA:
            stat = player.era_helper
        elif category == c.WINS:
            stat = player.wins
        elif category == c.WHIP:
            stat = player.whip_helper
        elif category == c.SO:
            stat = player.strikeouts
        elif stat == c.SAVES:
            stat = player.saves

        else:
            stat = float('-inf')

        return stat - benchmark

                    
    def sortByAverage(self, list):
        return list.sort(key=lambda x: x.average_helper, reverse=True)

    def sortByHomeRuns(self, list):
        return list.sort(key=lambda x: x.homeRuns, reverse=True)

    def sortByRBI(self, list):
        return list.sort(key=lambda x: x.rbi, reverse=True)

    def sortByStolenBases(self, list):
        return list.sort(key=lambda x: x.stolenBases, reverse=True)

    def sortByRuns(self, list):
        return list.sort(key=lambda x: x.runs, reverse=True)

    def sortByEra(self, list):
        return list.sort(key=lambda x: x.era_helper, reverse=True)

    def sortByWins(self, list):
        return list.sort(key=lambda x: x.wins, reverse=True)

    def sortByWhip(self, list):
        return list.sort(key=lambda x: x.whip_helper, reverse=True)

    def sortByStrikeouts(self, list):
        return list.sort(key=lambda x: x.strikeouts, reverse=True)

    def sortBySaves(self, list):
        return list.sort(key=lambda x: x.saves, reverse=True)

