import random
import pandas as pd

#this should pull the entire excel sheet into Python
df = pd.read_excel('VideoGameReferences.xlsx') 
#sheet_name is sheets. Starts with the first sheet being 0, second sheet is 1, so on and so forth
Steam = pd.read_excel('VideoGameReferences.xlsx', sheet_name=0)
Epic = pd.read_excel('VideoGameReferences.xlsx', sheet_name=1)
EAGames = pd.read_excel('VideoGameReferences.xlsx', sheet_name=2)
Xbox = pd.read_excel('VideoGameReferences.xlsx',sheet_name=3)
#r,c = shape, df.shape gives you the number of rows and columns, df.index gives you the same
a = count_row = Steam.shape[0]
print('You have', a+1, 'games on Steam. You should play:')
g = random.randint(0,a-1) 
cell_value = Steam.iloc[g,0]
print(cell_value)

b = count_row = Epic.shape[0]
print('You have', b+1, 'games on Epic. You should play:')
g = random.randint(0,b-1)
cell_value = Epic.iloc[g,0]
print(cell_value)

c = count_row = EAGames.shape[0]
print('You have', c+1, 'games on EA Games. You should play:')
g = random.randint(0,c-1)
cell_value = EAGames.iloc[g,0]
print(cell_value)

d = count_row = Xbox.shape[0]
print('You have', d+1,'games on Xbox PC Game pass. You shold play:')
g = random.randint(0,d-1)
cell_value = Xbox.iloc[g,0]
print(cell_value)

print("And if these still aren't the right game, go read a book, or do some homework.")

#^Code above was written 27-Sep-2023

#The following is the OG Code, written 26-Sep-2023, uses purely RNG to pick games, spits out numbers
#print("Game Options!\nOnly accounts for games installed by 26-Sep-2023.\nSteam-no Oculus:")
#print ("\t",random.randint(1,17));
#the \n creates a new line, \t creates an indent. Commas can be used to put funcitons (like random.randint) into things like a print
#print("Steam, All Games:")
#print ("\t",random.randint(1,36));

#print("Epic Games:")
#print ("\t",random.randint(1,5));

#print("EA Games:")
#print("\t", random.randint(1,2))

#print("Xbox Game Pass:")
#print("\t", random.randint(1,34))
