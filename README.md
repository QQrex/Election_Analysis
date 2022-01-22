# **Election_Analysis**

## **Purpose**
A Colorado Board of Elections employee has given you the following task to complete the election audit of a recent local congressional election.

## **Project Overview**
1. Calculate the total number of votes cast.
2. Get a complete list of candidates/counties that received votes.
3. Calculate the total number of votes each candidate/county received.
4. Determine the county with the most votes.
5. Calculate the percentage of votes each candidate won.
6. Determine the winner of the election based on popular vote.

## **Analysis**

Our first step is to create a path to open the election_results.csv to read and a path for election_analysis.txt to save our analysis results.

![import and path](https://github.com/QQrex/Election_Analysis/blob/main/Resources/import%20and%20paths.PNG)
>Line 5 - Importing csv module so we can pull data from our election_results.csv and perform operations on that data.
>
>Line 6 - Importing os module to open files when direct path is unknown.
>
>Line 9,11 - Creating the path for our "file_to_load" and "file_to_save".

It is not ideal to use a direct path in this code because if someone else needs to run this script, the direct path will not work for them. We import the "os" module to create an indirect path to the file we are reading or writing by using code os.path.join("folder","file") in our script.


Now that we have a path to read our election result file and a path to write into our analysis file. We need to create our variables for our operations, list and dictionaries.

![variables](https://github.com/QQrex/Election_Analysis/blob/main/Resources/counter%20list%20dic.PNG)

The next step will be to open our election_results.csv file and declare the headers in the file.

![open and headers](https://github.com/QQrex/Election_Analysis/blob/main/Resources/With%20open%20and%20headers.PNG)
>Line 35 - Using "with open" to open file_to_load as election_data.
>
>Line 36 - Using csv.reader(file) to read the file to load as variable reader.
>
>Line 39 - Declaring headers as first row in file.

Now that our file is open, we will write a for loop to loop through all the rows in our file to figure out total votes, votes each candidate received and total votes cast in each county.

![for loop row](https://github.com/QQrex/Election_Analysis/blob/main/Resources/for%20row%20in%20reader.PNG)
>Line 42 - Start for loop to loop through all rows in csv file.
>
>Line 45 - Starting from 0 votes, adding 1 vote per row to get total votes.

Before we calculate tho votes cast for each candidate and in each county, we need to specify which row each data is in.

![nameofrow](https://github.com/QQrex/Election_Analysis/blob/main/Resources/name%20of%20rows.PNG)
>line 48 - row 3 as candidate's name
>
>line 51 - row 2 as county name

Next, we need to figure out how many candidates and counties are is in the csv file by using two if statement with the same logic. Our logic would be, "If name is not in list, then add to list". Once we have figure out all the names and counties, we can tally up all the votes for each corresponding name or county. Remember, because we are still in the "for row in reader:" loop, we are able tally up votes based on names/counties list by creating a dictionary with names/counties as keys and votes as values.
![if can](https://github.com/QQrex/Election_Analysis/blob/main/Resources/if%20for%20can.PNG)
>Line 55 - If statement to ask if name is not already in candidate_options list.
>
>Line 58 - Add name to candidate_options list.
>
>Line 61 - Create dictionary with name as key, votes as value and set vote value to 0.
>
>Line 64 - Tally votes to dictionary based on name.
>

![if cou](https://github.com/QQrex/Election_Analysis/blob/main/Resources/if%20for%20cou.PNG)
>Line 69 - If statement to ask if county is not already in county list.
>
>Line 72 - Add county to county list.
>
>Line 76 - Create dictionary with county as key, votes as value and set vote value to 0.
>
>Line 80 - Tally votes to dictionary based on county.

Now that we have dictionaries of names/counties:votes we can begin to write our analysis into our election_analysis text file. Similar to how we opened election_results.csv, we can use with open() as:, but we need to add "w" inside open() to declare we are writing into the text file. We will write our election results into the text file and print into the terminal to check our work.
![WithopenWrite](https://github.com/QQrex/Election_Analysis/blob/main/Resources/With%20open%20write%20and%20print%20election.PNG)
>Line 84 - Open election_analysis.txt to write.
>
>Line 87 - Create f string election result summary with formatting as variable election_results.
>
>Line 94 - Print election results in terminal.
>
>Line 96 - Write election result summary to text file.


Moving forward, our next step would be calculating each county's voting percentages and then determine which county had the most votes. We will utilize a for loop to loop through our count_votes dictionary to accomplish this and will print or findings into our terminal to check our work before saving it to our election_analysis.txt.

![forcou](https://github.com/QQrex/Election_Analysis/blob/main/Resources/For%20county.PNG)
>Line 99 - For loop to loop county_votes dictionary with county_name as keys.
>
>Line 102 - Using get() to retrieve vote count as variable cVotes.
>
>Line 104 - Calculate county percentages with float() by cVotes/total_votes * 100.
>
>Line 105 - Create county_result summary variable with f string.
>
>Line 107 - Print county_result summary to terminal.
>
>Line 109 - Write county_results in to election_analysis.txt.
>
>Line 111 - Asking if statement "if cVote is greater than largest_county".
>
>Line 112 - If if statement is true then largest_count = cVotes.
>
>Line 113 - If if statement is true then largest_county = county_name.
>>
>>The if statement to find county with the largest vote count only works because the script is still in the for loop in line 99. We set the largest_count = 0 in our variables at the start of this script and as the for loop continues to loop through our county_votes dictionary, it is replacing the largest_count variable with largest cVote. At the end of the for loop it should have the largest county vote paired with county name.
>
>Line 115 to 118 - Create largest_county_summary variable with formatted f string results.
>
>Line 119 - Print largest_county_summary variable to terminal.
>
>Line 121 - Write largest_county_summary variable to election_analysis.txt.
>

Finally, we will calculate candidate percentages and winning candidate of the election. We will use a for loop again but instead loop through candidate_votes dictionary using candidate_name as keys and then printing to terminal / saving to election_analysis.txt.

![forcan](https://github.com/QQrex/Election_Analysis/blob/main/Resources/for%20can.PNG)
>Line 124 - For loop to loop through candidate_votes dictionary usi.ng candidate_name list as keys
>
>Line 127 - Using get() to retrieve votes counts as variable votes.
>
>Line 128 - Calculate candidate percentages with float() by votes/total_votes * 100.
>
>Line 129 to 130 - Create candidate_results summary variable with f string
>
>Line 134 - Print candidate_results summary to terminal.
>
>Line 135 - Write candidate_results summary to election_analysis.txt.
>
>Line 139 - Asking if statement "if votes is greater than winning_count and vote_percentage is great than winning_percentage.
>
>Line 140 - If if statement is true then winning_count = votes.
>
>Line 141 - If if statement is true then winning_candidate = candidate_name.
>
>Line 142 - If if statement is true then winning_percentage = vote_percentage.
>
>>The logic behind this loop is the same as the logic we used to figure out county with largest vote count. However, we are replacing the variables to match candidates rather than counties.
>
>Line 139 to 142 - Create winning_candidate_summary variable with formatted f string results.
>
>Line 151 - Print winning_candidate_summary to terminal.
>
>Line 154 - Write winning_candidate_summary to election_analysis.txt.
>

## Summary and Results

[Results]

![results](https://github.com/QQrex/Election_Analysis/blob/main/Resources/Terminal%20results.PNG)

[Summary]

The script outline for this analysis could serve as a foundation to be utilized for any state election. However, there are a few things to keep in mind. First, the pathing needs to be edited to ensure the file we want to read or write to can be accessed by the script. Also, if the data file we are reading is not a CSV file, we would need to edit the script to read whatever data file is provided. Lastly, if there are any new variables you would like to explore, we could easily add the variables to the list and use existing for loops to loop over data to perform an analysis.
    
## **Resources**
-Data Source: election_results.csv
-Software: Python 3.7.6, Visual Studio Code, 1.63.2
