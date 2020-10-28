pokemon = '''audino bagon baltoy banette bidoof braviary bronzor carracosta charmeleon cresselia croagunk darmanitan deino emboar emolga exeggcute gabite girafarig gulpin haxorus heatmor heatran ivysaur jellicent jumpluff kangaskhan kricketune landorus ledyba loudred lumineon lunatone machamp magnezone mamoswine nosepass petilil pidgeotto pikachu pinsir poliwrath poochyena porygon2 porygonz registeel relicanth remoraid rufflet sableye scolipede scrafty seaking sealeo silcoon simisear snivy snorlax spoink starly tirtouga trapinch treecko tyrogue vigoroth vulpix wailord wartortle whismur wingull yamask'''

# Split to list
pokemon_list = pokemon.split(" ")

# Put each of them inside dictionary
pokemon_dict = {}
for names in pokemon_list:
    if names[0] not in pokemon_dict:
        pokemon_dict[names[0]] = [names]
    else:
        pokemon_dict[names[0]].append(names)

# Variables
count = 0
longest_combi = []

# Main function
def longest_combination(combination):
    global count
    global longest_combi

    # Check the longest combination
    if len(combination) > count:
        count = len(combination)
        longest_combi = combination

    # The code snippet to find the next value in the chain
    if combination[-1][-1] in pokemon_dict:
        for name in pokemon_dict[combination[-1][-1]]:
            if name not in combination:
                longest_combination(combination + [name])
                
# Search all possible combinations
for names in pokemon_list:
    longest_combination([names])

# Print
print(longest_combi,"\n"+"The Length:",count)
