import pandas as pd

data_csv= pd.read_csv('pokemon_data.csv')
data_xls= pd.read_excel('pokemon_data.xlsx')
data_txt= pd.read_csv('pokemon_data.txt', delimiter='\t')      #For text use same csv functon.


# Print Operations !!
'''
#print(f"printing .csv file \n {data_csv.head(3)}")
#print(data_csv.tail(3))
#print(data_csv)
#print(f"printing excel file \n{data_xls.head(3)}")
#print (f"Printing .txt file \n {data_txt.head(3)}")

#print(f"Printing column information\n {data_csv.columns}\n")
#print(f"Printing single column \n {data_csv['Name']}")
#print(f"Printing single column with top 5 entries\n {data_csv['Name'][0:5]}")
#print(f"Printing multiple columns \n {data_csv[['Name', 'Type 1', 'HP']]}")
#print(f"Printing 2nd row form the file using iloc function\n {data_csv.iloc[1]}")
#print(f"Printing from 2nd row until 4th row \n {data_csv.iloc[1:4]}")
#print(f"Printing specific location, 2nd row, 1st column \n {data_csv.iloc[2,1]}")

#print(f"Printing all fields containing Fire  from column Type 1  using .loc function \n {data_csv.loc[data_csv['Type 1'] == 'Fire']}")

#print(data_csv.sort_values('Name'))   #Sorting values by alfaphetically
#print(data_csv.sort_values('Name', ascending=False))  #reverse
print(data_csv.sort_values(['Type 1', 'HP']))   #sorting multiple values

#For loop

#for all rows
#for index, row in data_csv.iterrows():
#    print(index, row)

#for specific column

#for index, row in data_csv.iterrows():
#    print(index, row['Name'])
'''

# Change Data  !!
'''
#print(data_csv.columns)

#Adding values from column HP until Speed and creating new column "Total" but it will not save the vaule in actual file.
data_csv['Total'] = data_csv['HP'] + data_csv['Attack'] + data_csv['Defense'] + data_csv['Sp. Atk'] + data_csv['Sp. Def'] + data_csv['Speed']

#To save the modified file.
#data_csv.to_csv('modified.csv')
#data_csv.to_csv('modified.csv', index=False)   #remove index

#new_data=pd.read_csv('modified.csv')
#print(new_data.head(5))

'''

# Filtering Data !!
'''''
#print(data_csv.loc[data_csv['Type 1'] == 'Fire'])  #filtering Type 1 == Fire
#print(data_csv.loc[ (data_csv['Type 1'] == 'Fire')  &  (data_csv['Type 2'] == 'Poison') ])  # two filter with '&'> and
#print(data_csv.loc[(data_csv['Type 1'] == 'Grass') | (data_csv['Type 2'] == 'Poison')])  # Filtering with "|" OR logic

#print(data_csv.loc[data_csv['Name'].str.contains('Mega')])    #Show all names with "Mega" string in it in column Name

#print(data_csv.loc[~data_csv['Name'].str.contains('Mega')])    #Show all name which DO NOT have Mega in column Name
'''''

# Conditional Changes !!
''''
#data_csv.loc[data_csv['Type 1'] == 'Flamer', 'Type 1'] = 'Fire'    #change all 'Fire' field from column 'Type 1' to 'Flamer'
#print(data_csv.loc[data_csv['Type 1'] == 'Fire'])      #Print

'''

# Aggregate statistics by groupby()


# Average skill stats of all Type 1 pockemon
#print(data_csv.groupby(['Type 1']).mean())

#Further sort ascending by attack 
#print(data_csv.groupby(['Type 1']).mean().sort_values('Attack', ascending=False))

#Sum

#print(data_csv.groupby(['Type 1']).sum())

#count
print(data_csv.groupby(['Type 1']).count())
