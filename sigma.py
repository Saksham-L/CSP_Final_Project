import pandas as pd
import matplotlib.pyplot as plt


df_lebron = pd.read_csv("lebron_career.csv")
df_jordan = pd.read_csv("jordan_career.csv")
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