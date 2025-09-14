import pandas as pd
from collections import Counter

# Initialize men's and women's lists
man_list = ['a', 'b', 'c', 'd']
women_list = ['A', 'B', 'C', 'D']

# Women's preferences as DataFrame
women_df = pd.DataFrame({'A': [3, 4, 2, 1], 'B': [3, 1, 4, 2], 'C': [2, 3, 4, 1], 'D': [3, 2, 1, 4]})
women_df.index = man_list

# Men's preferences as DataFrame
man_df = pd.DataFrame({'A': [1, 1, 2, 4], 'B': [2, 4, 1, 2], 'C': [3, 3, 3, 3], 'D': [4, 2, 4, 1]})
man_df.index = man_list

# Initialize each man's proposal list
women_available = {man: women_list.copy() for man in man_list}
waiting_list = []
proposals = {}
count = 0

while len(waiting_list) < len(man_list):
    # Men make proposals to their highest-ranked available women
    for man in man_list:
        if man not in waiting_list:
            # Propose to the top available woman
            best_choice = min(women_available[man], key=lambda w: man_df.loc[man][w])
            proposals[(man, best_choice)] = (man_df.loc[man][best_choice], women_df.loc[man][best_choice])

    # Check for women with multiple proposals
    overlays = Counter([pair[1] for pair in proposals.keys()])
    for woman in overlays.keys():
        if overlays[woman] > 1:
            # Woman chooses the best proposal, others are rejected
            pairs_for_woman = {pair: proposals[pair] for pair in proposals if pair[1] == woman}
            best_pair = min(pairs_for_woman.items(), key=lambda x: x[1][1])[0]
            pairs_to_drop = [p for p in pairs_for_woman if p != best_pair]

            # Remove rejected proposals
            for p in pairs_to_drop:
                del proposals[p]
                women_available[p[0]].remove(p[1])  # Update man's preference list

    # Men who successfully paired are added to the waiting list
    waiting_list = [pair[0] for pair in proposals.keys()]
    count += 1

print("Final stable pairs:", proposals)

