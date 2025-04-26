import pandas as pd

username = input('Instagram username: @')

followers = set(user for user in pd.read_csv(f"IGExport_Followers_{username}.csv")["userName"])
following = set(user for user in pd.read_csv(f"IGExport_Following_{username}.csv")["userName"])

print('Not following me back: ')
print(following - followers) #* not following me back
print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

print('I\'m not following back: ')
print(followers - following) #* i don't follow back