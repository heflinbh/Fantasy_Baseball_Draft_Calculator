from PlayerPool import PlayerPool
import Constants as c

class CostCalculator:

    def __init__(self):

        self.player_pool = PlayerPool()
        self.benchmark_dict = self.getBenchmark()
        self.pos_player_par_dict = self.getParPerPosition()
        self.par_all_player_dict, self.total_par = self.getParAll()
        self.player_value_dict = self.getValue()


    def getBenchmark(self):

        benchmarks = {}

        for position in c.POSITION_LIST:
            curr_list = self.player_pool.pos_list_dict.get(position)
            worst_index = (c.NUM_POS_PER_TEAM.get(position) * (c.NUM_TEAMS - 1)) - 1
            point_benchmark = curr_list[worst_index].points

            benchmarks[position] = point_benchmark

        return benchmarks


    def getParPerPosition(self):
        
        pos_par_dict = {}
        for position in c.POSITION_LIST:
            par_dict = {}
            curr_list = self.player_pool.pos_list_dict.get(position)
            benchmark = self.benchmark_dict.get(position)

            for player in curr_list:
                par = player.points - benchmark
                par_dict[player] = par

            pos_par_dict[position] = par_dict

        return pos_par_dict

    
    def getParAll(self):
        par_dict = {}
        sum_par = 0

        for pos in self.pos_player_par_dict:
            temp_dict = self.pos_player_par_dict.get(pos)

            for player in temp_dict:
                new_par = temp_dict.get(player)

                if player not in par_dict:
                    if new_par > 0:
                        sum_par += new_par
                    par_dict[player] = new_par

                elif par_dict.get(player) < new_par:
                    if new_par > 0:
                        sum_par += new_par - par_dict.get(player)
                    par_dict[player] = new_par

        return par_dict, sum_par



    def getValue(self):

        total_money = (c.BUDGET_PER_TEAM - c.NUM_PLAYERS_PER_TEAM) * c.NUM_TEAMS
        par_to_dollars = float(total_money) / float(self.total_par)

        value_dict = {}

        for player in self.par_all_player_dict:
            value_dict[player] = self.par_all_player_dict.get(player) * par_to_dollars
                    
        return value_dict





