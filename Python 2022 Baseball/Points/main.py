from CostCalculator import CostCalculator
import pandas as pd
import Constants as c

def main():

    my_cost_calculator = CostCalculator()
    my_df = pd.DataFrame()

    for player in my_cost_calculator.player_value_dict:

        name = player.name
        points = player.points
        price = my_cost_calculator.player_value_dict.get(player)

        d = {c.NAME:name, c.POINTS:points, c.PRICE:price}
        new_df = pd.DataFrame(data=d, index=[""])

        my_df = pd.concat([my_df, new_df])

    my_df.to_excel(c.EXCEL_OUTPUT)
    print("HERE")

    print(my_df)


main()