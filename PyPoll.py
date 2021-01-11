#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular votes.

#Open the election results and read the file.
#Assign a variable for the file to load and the path.
# import csv
# import os

# file_to_load='Resources/election_results.csv'

# election_results=open(file_to_load,'r')

# file_to_load=open('Resources/election_results.csv')
# file_to_load=os.path("Resources","election_results.csv")

# open(file_to_load,'w')
#Open the election results and read the file.
# with open(file_to_load) as election_data:
#     #To do: perform analysis.
#     print(election_data)

#Create a filename variable toa direct or indirect path to the file.
# election_data=open(r'C:\Users\Joey\Documents\Election_Analysis\Resources\election_results.csv',"r")

#Assign a variable for the file to load and the path.
#file_to_load=('C:\Users\Joey\Documents\Election_Analysis\Resources\election_results.csv')

# election_data=open(file_to_load,'r')
# #Open the election results and read the file.
# with open(file_to_load) as election_data:

# #     #To do: perform analysis.
#     print(election_data)

#INDIECT PATH METHOD
import csv
import os

#Assign a variable to load a file from a path.
file_to_load=os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path.
file_to_save=os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file.
with open(file_to_load) as election_data:
    #To do: read and analyze the data here.
    file_reader=csv.reader(election_data)
    # #Write some data to the file.
    # #txt_file.write("Hello World")
    #Print the header row.
    headers=next(file_reader)
    print(headers)