import os
import csv

election_data = os.path.join("election_data.csv")
election_output = 'election_output.txt'

# A list to capture the names of candidates
total_votes = 0
candidates_name = []
each_vote = [] 
percent_vote = []


with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile)
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes= total_votes + 1 

  #find if candidate not in list or not then add to list -> if not just add    
        if row[2] not in candidates_name:
            candidates_name.append(row[2])
            index = candidates_name.index(row[2])
            each_vote.append(1)
        else:
            index = candidates_name.index(row[2])
            each_vote[index] = each_vote[index] + 1 
    
    # Add to percent_votes list 
    for votes in each_vote:
        percentage = (votes/total_votes)
        percentage = "{:.3%}".format(percentage)
        percent_vote.append(percentage)
        #print(percentage)
    
    # Find the winning candidate
    winner = max(each_vote)
    index = each_vote.index(winner)
    winning_candidate = candidates_name[index]
    

#Print results
print("Election Results")
print("--------------------------")
print("Total Votes: " + str(total_votes))
print("--------------------------")
for i in range(len(candidates_name)):
    print(candidates_name[i] + ": " + (str(percent_vote[i])) + " (" + (str(each_vote[i])) + ")")
print("--------------------------")
print("Winner: " + winning_candidate)
print("--------------------------")

#output 
with open (election_output, "w") as txt:
    txt.write ("Election Results")
    txt.write ("\n")
    txt.write ("----------------------------")
    txt.write ("\n")
    txt.write ("Total Votes: " + str(total_votes))
    txt.write ("\n")
    txt.write ("--------------------------")
    for i in range(len(candidates_name)):
        line = ((candidates_name[i] + ": " + (str(percent_vote[i])) + " (" + (str(each_vote[i])) + ")"))
        txt.write('{}\n'.format(line))
    txt.write ("--------------------------")
    txt.write ("\n")
    txt.write ("Winner: " + winning_candidate)
    txt.write ("\n")
    txt.write ("--------------------------")

#https://www.tutorialspoint.com/How-to-write-multiple-lines-in-text-file-using-Python