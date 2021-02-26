# https://adventofcode.com/2020/day/21

from copy import deepcopy as deep

debug = False
printit = False
part2 = False

def p(text = "", override = False): #prints as string 
    if debug or printit or override:
        print(text, flush=True)
def pp(subject, name = "", override = False): #prints anything with a name as string 
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        #   print()
        print(name, ": ", subject)
def ppp(subject, name = "", override = False, isDictionary=False): #prints list entries
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        print()
        print(name, ": ")
        for item in subject:
            if isDictionary:
                print(item, ":", end="")
                print(subject[item])
            else:
                print(item)
def pppp(subject, name = "", override = False, isDictionary=False): #prints list's list entries
    if debug or printit or override:
        #print("\n", name, ": ", subject)
        print()
        print(name, ": ")
        for item in subject:
            if isDictionary:
                print(item, ":", end="")
                print(subject[item])
            else:
                for tile in item:
                    print()
                    for line in tile: 
                        print(line)

print("\n----------------------------------")   # reading file

DATA = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""

if not debug:
    file = "advent_2020_ludwig/AOC20/DATA_aoc20_21.txt"
    with open(file) as f:
        DATA = f.read()

DATA = [s[:-1].split(" (contains ") for s in DATA.split("\n")]
ppp(DATA)
_FOODS, _FOODNAMES, _INGREDIENTS, _ALLERGENS  = {}, {}, {}, {}
for index, line in enumerate(DATA):
    _FOODS[index] = [line[0].split(), line[1].split(", ")]
    _FOODNAMES[index] = line[0]

ppp(_FOODS, "foods dict", False, True)
ppp(_FOODNAMES, "food names dict", False, True)

for food in _FOODS:
    for ingredient in _FOODS[food][0]:
        _INGREDIENTS[ingredient] = None
    for allergen in _FOODS[food][1]:
        _ALLERGENS[allergen] = None
ppp(_INGREDIENTS, "ingredients dict", False, True)
ppp(_ALLERGENS, "allergens dict", False, True)

_ALLERGENS_FOUND = 0
def solve_allergen(allergen):
    pp(allergen, "checking")
    foods_containing = []
    ingredient_register = {}
    matches = 0
    match = ""

    if _ALLERGENS[allergen] is not None:
        return _ALLERGENS[allergen]

    for f in _FOODS:
        food = _FOODS[f]
        pp(food, "food to check")
        for contained_allergen in food[1]:
            if contained_allergen == allergen:
                pp(contained_allergen, "matching allergen")
                if f not in foods_containing:
                    foods_containing.append(f)
    pp(foods_containing, "indices of foods containing the allergen")
    for f in foods_containing:
        pp(_FOODS[f][0], "food to check")
        for ingredient in _FOODS[f][0]:
            if _INGREDIENTS[ingredient] is None:
                if ingredient not in ingredient_register:
                    pp(ingredient, "not in register, adding")
                    ingredient_register[ingredient] = 1
                else:
                    pp(ingredient, "already in register")
                    ingredient_register[ingredient] += 1
                    pp(ingredient_register[ingredient], "increasing count to")
            else:
                pass

    for ing in ingredient_register:
        if ingredient_register[ing] == len(foods_containing):
            pp(ing, "found ingredient that is in all foods containing the allergen")
            match = ing
            matches += 1

    if matches == 1:
        pp(match, "the only ingredient that is in all those, returning")
        return match
    else:
        return False
    
done = False
loop = 0

while not done:
    loop += 1
    p(loop, True)
    for a in _ALLERGENS:
        pp(a)
        solved = solve_allergen(a)
        if solved:
            if _ALLERGENS[a] is None:
                _ALLERGENS[a] = solved
                _INGREDIENTS[solved] = a
                #ppp(_INGREDIENTS, "", True, True)
                ppp(_ALLERGENS, "", True, True)
                _ALLERGENS_FOUND += 1
                done = _ALLERGENS_FOUND == len(_ALLERGENS)
            else:
                pass
        if done:
            break
    #ppp(_ALLERGENS, "", False, True)
    

safe_ingredients = {}
amount = 0
if done:
    for i in _INGREDIENTS:
        if _INGREDIENTS[i] is None:
            safe_ingredients[i] = 0
            for food in _FOODS:
                food = _FOODS[food]
                for x in food[0]:
                    if x == i:
                        amount += 1
                        safe_ingredients[i] += 1

pp(safe_ingredients, "safe ingredients", True)
pp(amount, "total occurences of them", True)

allsorted = sorted(_ALLERGENS)

canonical_dangerous_ingredient_list = []
for i in allsorted:
    canonical_dangerous_ingredient_list.append(_ALLERGENS[i])
pp(",".join(canonical_dangerous_ingredient_list), "", True)

'''
graveyard of failed attempts..


def check_food(food):
    ingredients = food[0]
    allergens = food[1]
    ing_leftovers = len(ingredients)
    alg_leftovers = len(allergens)

    for ing in ingredients:
        if _INGREDIENTS[ing] is not None:
            ing_leftovers -= 1
        else:
            ing_leftover = ing

    for alg in allergens:
        if _ALLERGENS[alg] is not None:
            alg_leftovers -= 1
        else:
            alg_leftover = alg

    if ing_leftovers == alg_leftovers == 1:
        return [ing_leftover, alg_leftover]
    else:
        return False
    

def compare_foods(food_a, food_b):
    ingredients_a = food_a[0]
    ingredients_b = food_b[0]
    allergens_a = food_a[1]
    allergens_b = food_b[1]
    ing_candidate, alg_candidate = "", ""
    allergen_matches, ingredient_matches = 0, 0
    
    precheck = check_food(food_a)
    if precheck:
        return precheck
    precheck = check_food(food_b)
    if precheck:
        return precheck
    
    for ing_a in ingredients_a:
        for ing_b in ingredients_b:
            if ing_a == ing_b:
                if _INGREDIENTS[ing_a] is None:
                    ingredient_matches += 1
                    ing_candidate = ing_a

    if ingredient_matches == 1:
        for alg_a in allergens_a:
            for alg_b in allergens_b:
                if alg_a == alg_b:
                    if _ALLERGENS[alg_a] is None:
                        allergen_matches += 1
                        alg_candidate = alg_a
    
    if allergen_matches == 1:
        return [ing_candidate, alg_candidate]
    else:
        False


def comptest(a, b):
    global _ALLERGENS_FOUND, _ALLERGENS, _INGREDIENTS
    comp0 = compare_foods(_FOODS[a], _FOODS[b])
    if comp0:
        _ALLERGENS[comp0[1]] = comp0[0]
        _INGREDIENTS[comp0[0]] = comp0[1]
        ppp(_INGREDIENTS, "", False, True)
        ppp(_ALLERGENS, "", False, True)
        _ALLERGENS_FOUND += 1
    else:
        #p("\nno exact match")
        pass

while not done:
   for food in _FOODS:
        for food_b in _FOODS:

            if food != food_b:
                comptest(food, food_b)
                done = _ALLERGENS_FOUND == len(_ALLERGENS)

            if done:
                break
        if done:
            break

'''
