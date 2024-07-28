import csv
import pandas as pd

df = pd.read_csv("followers.csv")

username = input('Instagram username: @')

followers = set(user for user in pd.read_csv(f"IGExport_Followers_{username}.csv")["userName"])
following = set(user for user in pd.read_csv(f"IGExport_Following_{username}.csv")["userName"])
print(following - followers) #* not following me back
# print(followers - following) #* i don't follow back