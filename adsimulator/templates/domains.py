FUNCTIONAL_LEVEL_LIST = ["2008"] * 4 + ["2008 R2"] * 5 + ["2012"] * 10 + \
            ["2012 R2"] * 30 + ["2016"] * 50 + ["Unknown"] * 1

TLD_LIST = [
    ".LOCAL",
    ".COM",
    ".PRV",
    ".CORP",
    ".IT",
    ".NET",
    ".ORG"
]


def get_functional_level_list(prob):
    sum = 0
    for key in prob.keys():
        sum += prob[key]
    if sum != 100:
        return FUNCTIONAL_LEVEL_LIST
    try:
        return ["2008"] * prob["2008"] +\
            ["2008 R2"] * prob["2008 R2"] +\
            ["2012"] * prob["2012"] +\
            ["2012 R2"] * prob["2012 R2"] +\
            ["2016"] * prob["2016"] +\
            ["Unknown"] * prob["Unknown"]
    except:
        return FUNCTIONAL_LEVEL_LIST
