import os
import csv

election__csv = os.path.join(r"C:\Users\Sarah\OneDrive\Desktop\BCamp\homeworks\python-challenge\PyPoll\Resources","election_data.csv")

with open(election__csv, encoding ="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_reader)
    
    totalVotes = 0
    candidates = []
    candiVotes = {}

    for row in csv_reader:
        cName = row[2]
        totalVotes = totalVotes + 1
        

        if cName not in candidates:
            candidates.append(cName)
            candiVotes[cName] = 0
        else:    
            candiVotes[cName] = candiVotes[cName] + 1

    #def of a function to do percentage of votes each candidate won
    def percent(name):
        total = candiVotes[name]
        return round((total/totalVotes)*100, 3)
    
    #def of a function total votes for each, maybe for print out
    def amount(name):
        total = candiVotes[name]
        return total
    
    #def print out all the candidates info
    #results = [
    #        f"{votes}: {percent(votes)}% ({amount(votes)})\n" 
    #        for votes in candiVotes]
    
    def printout(list):
        work = ""
        for each in list:
            #print(f'{each}: {percent(each)}% ({amount(each)})')
            work = work + str(each) + ": " + str(percent(each)) + "% ("+ str(amount(each)) + ")\n" 
        return work
    #winner of election
    def chickendinner(list):
        winner = 0
        winName = ""
        for name in list:
            if list[name] > winner:
                winner = list[name]
                winName = name
        return winName





    election_file = os.path.join(r'C:\Users\Sarah\OneDrive\Desktop\BCamp\homeworks\python-challenge\PyPoll\analysis', "election_results.txt")
    el_out = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {totalVotes}\n"
        f"-------------------------\n"
        f'{printout(candiVotes)}'
        f"-------------------------\n"
        f"Winner: {chickendinner(candiVotes)}\n"
        f"-------------------------\n"

    )
    print(el_out)
    with open(election_file, "w") as txt_file:
        txt_file.write(el_out)