import pandas as pd
import matplotlib.pyplot as plt


df_lebron = pd.read_csv("lebron_career.csv")
df_jordan = pd.read_csv("jordan_career.csv")
print(df_lebron.head)

print(df_jordan.head)
total_pts_lebron = df_lebron["pts"].sum()
total_pts_jordan = df_jordan["pts"].sum()
print(f"Total Points - LeBron James: {total_pts_lebron}")
print(f"Total Points - Michael Jordan: {total_pts_jordan}")
total_tov_lebron = df_lebron["tov"].sum()
total_tov_jordan = df_jordan["tov"].sum()
print(f"Total Turnovers - LeBron James: {total_tov_lebron}")
print(f"Total Turnovers - Michael Jordan: {total_tov_jordan}")
def MakeAGraph(value, bins, name):
    B = int(bins)
    plt.figure(figsize=(10, 6))
    plt.hist(df_lebron[value], bins=B, alpha=0.5, label="LeBron James")
    plt.hist(df_jordan[value], bins=B, alpha=0.5, label="Michael Jordan")
    plt.xlabel(f"{name} Per Game")
    plt.ylabel("Frequency")
    plt.legend()
    plt.savefig(f"LeBron_vs_Jordan_Histogram_{value}.png")
    plt.show()
    plt.close
MakeAGraph("pts",10, "Points")
MakeAGraph("trb", 10, "Rebounds")
MakeAGraph("stl", 8, "Steals")
MakeAGraph("ast", 10, "Assists")
MakeAGraph("blk", 5, "Blocks")
MakeAGraph("tov", 6, "Turnovers")
MakeAGraph("mp", 10, "Minutes Played")