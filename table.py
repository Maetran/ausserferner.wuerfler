###table

###game table style
def tableStyle(choise):
    if choise == "1":
        table = {"down" : {1 : "", 2 : "", 3 : "", 4 : "",
                5 : "", 6 : "", "min" : "", "max" : "",
                "kent" : "", "full" : "", "poker" : "",
                "sixty": ""},
                "free" : {1 : "", 2 : "", 3 : "", 4 : "",
                5 : "", 6 : "", "min" : "", "max" : "",
                "kent" : "", "full" : "", "poker" : "",
                "sixty": ""},
                "up" : {1 : "", 2 : "", 3 : "", 4 : "",
                5 : "", 6 : "", "min" : "", "max" : "",
                "kent" : "", "full" : "", "poker" : "",
                "sixty": ""},
                "said" : {1 : "", 2 : "", 3 : "", 4 : "",
                5 : "", 6 : "", "min" : "", "max" : "",
                "kent" : "", "full" : "", "poker" : "",
                "sixty": ""}}
        return(table)

    if choise == "2":
        table = {"free" : {1 : "", 2 : "", 3 : "", 4 : "",
                5 : "", 6 : "", "min" : "", "max" : "",
                "kent" : "", "full" : "", "poker" : "",
                "sixty": ""}}
        return(table)

    if choise == "3":
        table = {"said" : {1 : "", 2 : "", 3 : "", 4 : "",
                5 : "", 6 : "", "min" : "", "max" : "",
                "kent" : "", "full" : "", "poker" : "",
                "sixty": ""}}
        return(table)
#
# def momPoints(table):
#     print(table)
#     for x in 1, 2, 3, 4, 5, 6, "min", "max", "kent", "full", "poker", "sixty":
#         print(f"{x:04d}{said[x]:>12}")
