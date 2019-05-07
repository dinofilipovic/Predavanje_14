from prettytable import PrettyTable

table = PrettyTable({"animal", "ferocity"})

table.add_row(["wolverine", 100])
table.add_row(["grizly", 87])
table.add_row(["cat",-1])
table.add_row(["doplhin", 63])

print(table)

exit()