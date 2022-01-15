# **Election_Analysis**

## **Project Overview**
A Colorado Board of Elections employee has given you the following task to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates/counties that received votes.
3. Calculate the total number of votes each candidate/county received.
4. Determine the county with the most votes.
5. Calculate the precentage of votes each candidate won.
6. Determine the winner of the election based on popluar vote.

## **Analysis and Results**

Our first step is to create a path to open the election_results.csv to read and create an election_analysis.txt to save our analysis results.

![import and path](https://github.com/QQrex/Election_Analysis/blob/main/Resources/import%20and%20paths.PNG)
>line 5 - Importing csv module to pull data from our election_results.csv and performation operations on that data.
>
>line 6 - Importing os module to open files when direct path is unknown.
>
>line 9,11 - Creating the path for our "file_to_load" and "file_to_save".

It is not ideal to use a direct path in this code because if someone else needs to run this script, the direct path will not work for them. We import the "os" module to create an indirect path to the file we are reading or writing to when the code os.path.join("folder","file") in our script.


Now that we have a path to read our election result file and a path to write into our analysis file. We need to create our variables for our operations, list and dictionaries.

![variables](https://github.com/QQrex/Election_Analysis/blob/main/Resources/counter%20list%20dic.PNG)

The next step will be to open our election_results.csv file and declare the headers in the file.

![open and headers](https://github.com/QQrex/Election_Analysis/blob/main/Resources/With%20open%20and%20headers.PNG)
>line 35 - Using "with open" to open file_to_load as election_data.
>
>line 36 - Using csv.reader(file) to read the file to load as variable reader.
>
>line 39 - Declaring headers as first row in file.

Now that our file is open, we will write a for loop to loop through all the rows in our file to figure out total votes, votes each candidate received and total votes cast in each county.

![for loop row](https://github.com/QQrex/Election_Analysis/blob/main/Resources/for%20row%20in%20reader.PNG)
>line 42 - Start for loop to loop through all rows in csv file.
>
>Line 45 - Starting from 0 votes, adding 1 vote per row to get total votes.

Before we calculate tho votes cast for each candidate and in each county, we need to specify which row each data is in.

![nameofrow](https://github.com/QQrex/Election_Analysis/blob/main/Resources/name%20of%20rows.PNG)
>line 48 - row 3 as candidate's name
>
>line 51 - row 2 as county name

Next we need to figure out how many candidates and counties are is in the csv file by using an if statement. If candidate's name or county is not in candidate_options list or county list, then add to list. Once we have firgure out all the names and counties we can tally up all the votes for each corrisponding name or county. Remember, because we are still in the "for row in reader:" loop, we are able tally up votes based on names/counties list by creating a dictionary with names/counties as keys and votes as values.
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

Now that we have dictionaries of names/counties:votes we can begin to write our analysis into our election_analysis text file. Simliar to how we opened the election_results.csv, we are going to use an open








## Summary
The analysis of the election shows that:
-There were "x"votes cast in the election.
-The candidates were:
    -Candidate 1
    -Candidate 2
    -Candidate 3
-The Candidate results were:
    -Candidate 1 received "x%" of the vote and "y" number of votes.
    -Candidate 2 received "x%" of the vote and "y" number of votes.
    -Candidate 3 received "x%" of the vote and "y" number of votes.
-The winner of the election was:
    -Candidate (1,2, or 3), who received "x%" of the vote and "y" number of votes.
    
## **Resources**
-Data Source: election_results.csv
-Software: Python 3.7.6, Visual Studio Code, 1.63.2
