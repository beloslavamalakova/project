import pandas as pd


# Initialize men's and women's lists
man_list = ['a', 'b', 'c', 'd']
women_list = ['A', 'B', 'C', 'D']

# Women's preferences as DataFrame
women_df = pd.DataFrame({'A': [3, 4, 2, 1], 'B': [3, 1, 4, 2], 'C': [2, 3, 4, 1], 'D': [3, 2, 1, 4]})
women_df.index = man_list

# Men's preferences as DataFrame
man_df = pd.DataFrame({'A': [1, 1, 2, 4], 'B': [2, 4, 1, 2], 'C': [3, 3, 3, 3], 'D': [4, 2, 4, 1]})
man_df.index = man_list

