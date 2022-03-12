# Election-Analysis
Using Python Module 3

## Overview of Election Audit
The Colorado Board of Elections staff has given the following list of taks to complete an election audit for a recent local congressional election:

1. Calculate the number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Calculate the voter turnout for each county.
7. Calculate the percentage of votes from each county out of the total count.
8. Determine the county with the highest voter turnout.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code

## Election-Audit Results
The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 total votes.
  - Diana DeGette received 73.8% of the vote and 272,892 total votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 total votes.
- The winner of the election was:
  - Dianna Degette, who received 73.8% of the vote and 272,892 total votes. 
- The counties in the election were:
  - Jefferson
  - Denver
  - Arapahoe
- The results of each counties voter turnout were:
  - Jefferson county had 10.5% of the vote and 38,855 total votes.
  - Denver county had 82.8% of the vote and 306,055 total votes.
  - Arapahoe county had 6.7% of the vote and 24,801 total votes.
- The county with the highest voter turnout:
  - Denver county, which had 82.8% of the vote.

## Election-Audit Summary
While working on the code for this election-audit it was easy to see how it could be used for most other election types. The code is made to import any CSV file that can contain any number of counties or candidates without having to change the code. This makes the PyPoll code versatile and useful for others. Some modifications that could be applied to the script for future use are:
1. If another for loop is applied to the code, we could use it to see how many votes each candidate got in each county. This could help each candidate figure out where they need to campaign harder next round of elections.
2. The code could also be refactored for a CSV file that contained other types of political positions such as senators or county judges. 
