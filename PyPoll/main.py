# Creating the path file 
import os
import csv
filepath = os.path.join('.', 'Resources', 'election_data.csv')

with open(filepath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    candidatelist = [candidate[2] for candidate in csvreader]
    
# Calculating the number of total votes
totalvotes = len(candidatelist)

# Creating a unique list of the candidates 
canditatesinfo = [[candidate,candidatelist.count(candidate)] for candidate in set(candidatelist)]

# Sorting the list so that the first candidate becomes the winner 
canditatesinfo = sorted(canditatesinfo, key=lambda x: x[1], reverse=True)

# Printing the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {totalvotes}")
print("-------------------------")

for candidate in canditatesinfo:
    percent_votes = (candidate[1] / totalvotes) * 100
    print(f'{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})')

print("-------------------------")
print(f"Winner: {canditatesinfo[0][0]}")
print("-------------------------")


#  Printing the  election results to text file 
filepath = os.path.join('.', 'analysis', 'PyPoll_Results.txt')
with open(filepath, "w") as text_file:
    print("Election Results", file=text_file)
    print("-------------------------", file=text_file)
    print(f"Total Votes: {totalvotes}", file=text_file)
    print("-------------------------", file=text_file)

    for candidate in canditatesinfo:
        percent_votes = (candidate[1] / totalvotes) * 100
        print(f'{candidate[0]}: {percent_votes:6.3f}% ({candidate[1]})', file=text_file)

    print("-------------------------", file=text_file)
    print(f"Winner: {canditatesinfo[0][0]}", file=text_file)
    print("-------------------------", file=text_file)