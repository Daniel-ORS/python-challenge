
electionData="election_data.csv"
import csv
import collections
import os


with open(electionData, "r",encoding="UTF-8",newline="\n") as electionData:
    csvreader=csv.reader(electionData,delimiter=",")
    #print(csvreader)
    #csv_header=next(csvreader)
    csv_header=next(csvreader)
 
numVotes=0
candidateVotes=[]
candidates={}

for row in csvreader:
    numVotes+=1
    candidateName=row[2]
    if candidateName in candidates:
        candidates[candidateName]+=1
    else:
        candidates[candidateName]=1

voteCount='\n'
for key in candidates.keys():
        percent=(candidates[key]/numVotes)*100
        percent=round(percent,2)
        voteCount+= f'{key}:{percent}%, ({candidates[key]})'
        candidateVotes.append(candidates[key])

maxVotes=max(candidateVotes)
maxIndex=candidateVotes.index(maxVotes)
Names=list(candidates.keys())
pollWinner=Names[maxIndex]

result=f'''
    Election Results
    -------------------------
    Total Votes: {numVotes}
    -------------------------
    {voteCount}
    -------------------------
    Winner: {pollWinner}
    -------------------------
    '''
print(result)




