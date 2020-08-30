
# PyPoll Script

# Dependecies
import pandas as pd

# Get dataset
data_file = 'Resources.PyP/election_data.csv'

# Use pandas library to read data set
data_file_df = pd.read_csv(data_file)

# Check to make sure pandas is reading csv file
print(data_file_df.head())

# Getting the different unique candidate names
unique_can = data_file_df['Candidate'].unique()
print(unique_can)

# Getting the total for each candidates votes + Turning results into a new data frame
count_df = data_file_df['Candidate'].value_counts().rename_axis('Cand_Name').reset_index(name='Votes_Rec')
print(count_df)

# Getting total vote count
total_votes = count_df['Votes_Rec'].sum()
print(total_votes)

#Adding Percent of votes to count_df data frame
per_of_votes = (count_df['Votes_Rec']/total_votes) * 100
count_df['per_of_votes'] = per_of_votes
print(count_df)

# Rounding percent column
count_df = count_df.round({'Votes_Rec': 1, 'per_of_votes':0})


#Getting the value of the candidate with the most votes
max_vote = count_df['Votes_Rec'].max()

# Getting a new data frame with just the winning candidate
WC_df = count_df[count_df['Votes_Rec'] == max_vote]
print(WC_df)

# Getting Winning Candidate INFO
WCN = WC_df.iloc[0,0]
WCPV = WC_df.iloc[0,2]
WVR = WC_df.iloc[0,1]

# Printing DataFrame to CSV file
count_df.to_csv("Analysis.PyP/Final_Election_Results", index=False, header=True)


# Removing the winning candidate from the df
count_df = count_df.drop([0])

# Formatting df before print(Failed)
# count_df.style.format({'Votes_Rec': "({:.2f})", 'per_of_votes': "{:.2%}", 'Cand_Name': '{:.2f}:'})

# count_df['Cand_Name'] = count_df['Cand_Name'].map('{:.2f}:'.format)
# count_df['Votes_Rec'] = count_df['Votes_Rec'].map("({:.2f})".format)
# count_df['per_of_votes'] = count_df['per_of_votes'].map("{:.2%}".format)


# Variables doe correy
co_name = count_df.iloc[0,0]
co_vote_per = count_df.iloc[0,2]
co_vote_count = count_df.iloc[0,1]

# Variables doe li
li_name = count_df.iloc[1,0]
li_vote_per = count_df.iloc[1,2]
li_vote_count = count_df.iloc[1,1]

# Variables doe o'tooley
ot_name = count_df.iloc[2,0]
ot_vote_per = count_df.iloc[2,2]
ot_vote_count = count_df.iloc[2,1]

#Before creating the above variables to hold the info for the candidates I was trying to loop through the latest df to
# print the information but I could not get the syntax right below is the line of code feel free to correct me thanks :-(

# for x in count_df['Cand_Name']: print(f"{count_df.loc[ ,'Cand_Name']} {count_df.loc[ ,'per_of_votes']}"
#                                       f"{count_df.loc[ ,'Votes_Rec']}")


# Election Results

print('Election Results')
print('-----------------------')
print(f'Total Votes: {total_votes}')
print('-----------------------')
print(f'{WCN}: {WCPV}% ({WVR})')
print(f'{co_name}: {co_vote_per}% ({co_vote_count})')
print(f'{li_name}: {li_vote_per}% ({li_vote_count})')
print(f'{ot_name}: {ot_vote_per}% ({ot_vote_count})')
print('-----------------------')
print(f'Winner: {WCN}')
print('-----------------------')






