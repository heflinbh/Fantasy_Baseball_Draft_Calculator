from CostCalculator import CostCalculator
import Constants as c

def main():

    my_cost_calculator = CostCalculator()

    for player in my_cost_calculator.player_value_dict:
        if c.PI in player.positions:

            name = player.name
            points = player.points
            price = my_cost_calculator.player_value_dict.get(player)

            print("NAME: " + str(name) + " POINTS: " + str(points) + " PRICE: " + str(price))

main()