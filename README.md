# DM_Challenge_WC_Winner
Data Mining Challenge , Predict winner of Cricket World Cup 2023





Documentation

for

CP-03


By Group -16










PROJECT PIPELINE

Understanding of Data (Problem Statement)

Data Preprocessing - checked null values, attribute types, duplicate values etc

Data Visualization - 
Distribution plots
Scatter Plots
Box Plots
Count Plots
Barplots
Heatmap

Contributions : 

Chinmaya (202218054) 
TASK 2 and 3 : Predicting Finalist and Winner (Multiclass Classification)


Riya (202218049) 
TASK 1 :  Preprocessing, EDA and Predicting cricketers likely to achieve the highest runs, wickets, and catches along with their respective countries.


Swayista (202218035)
TASK 2 and 3 : Predicting Finalist and Winner (Regression)


Asish (202218022) 
 TASK 2 and 3 : Predicting Playing 11 for Finalist


Kashish (202001425)
 TASK 2 and 3 : Scrapping, EDA, Documentation




















Task 1 :  
FILE : Data_Mining(Scrapped)_CP_03_Riya.ipynb
ML pipeline
Feature selection using correlation analysis
Splitting of data
Scaling of data
Model Fitting 
               → Linear Regression
               → Decision tree
               → Random Forest Regression
               → ANN
Model Evaluation and Testing


Problem Statement :

Predicting the batsman who will score most runs in the tournament.

The data has been scraped from the provided link - https://www.espncricinfo.com/records/tournament/batting-most-runs-career/icc-cricket-world-cup-2023-24-15338

Dataset Description for most runs : 

Player: The name of the cricket player who took the wickets.

Country: The country for which the player represents or plays international cricket.

Span: The time period (range of years) during which the player's career spanned.

Matches: The total number of matches the player participated in.

Innings: The total number of bowling innings bowled by the player.

Balls: The total number of balls bowled by the player.

Overs: The total number of overs bowled by the player. An over consists of six legal deliveries.

MDNS: The total number of maidens bowled by the player. A maiden over is an over in which no runs are scored.

Runs: The total number of runs conceded by the player.

Wickets: The total number of wickets taken by the player.

BBI (Best Bowling in an Inning): The player's best bowling performance in a single inning, represented as the number of wickets taken for the fewest runs.

AVE (Bowling Average): The average number of runs conceded per wicket taken by the player.

Econ (Economy Rate): The average number of runs conceded per over bowled by the player.

SR (Strike Rate): The average number of balls bowled per wicket taken by the player.

Fours: The total number of times the player's deliveries were hit for four runs by the batsmen.

Fives: The total number of times the player took five wickets in a single inning.

![1](https://github.com/Chinmaya54/DM_Challenge_WC_Winner/assets/75682006/9de7d024-dddc-419e-9cd6-5b401835fea9)






Predicting the player who will  have the most catches in the tournament.

The data has been scraped from the provided link - 
https://www.espncricinfo.com/records/tournament/fielding-most-catches-career/icc-cricket-world-cup-2023-24-15338


Dataset Description for most catches : 

Player: The name of the cricket player who took catches.

Country: The country for which the player represents or plays international cricket.

Span: The time period (range of years) during which the player's career spanned.
Matches: The total number of matches the player participated in.

Innings: The total number of fielding innings the player was involved in.

CT (Catches): The total number of catches taken by the player.

Max: The maximum number of catches taken by the player in a single match.

Ct/Inns (Catches per Inning): The average number of catches taken by the player per fielding inning.

![ctinns](https://github.com/Chinmaya54/DM_Challenge_WC_Winner/assets/75682006/e0e34d47-f6cc-4ce6-88ab-4393c79aaed9)







Predicting the bowler who will  have the most wickets in the tournament.

The data has been scraped from the provided link - https://www.espncricinfo.com/records/tournament/bowling-most-wickets-career/icc-cricket-world-cup-2023-24-15338


Dataset Description for most wickets :

Player: The name of the cricket player who took the wickets.

Country: The country for which the player represents or plays international cricket.

Span: The time period (range of years) during which the player's career spanned.

Matches: The total number of matches the player participated in.

Innings: The total number of bowling innings bowled by the player.

Balls: The total number of balls bowled by the player.

Overs: The total number of overs bowled by the player. An over consists of six legal deliveries.

MDNS: The total number of maidens bowled by the player. A maiden over is an over in which no runs are scored.

Runs: The total number of runs conceded by the player.

Wickets: The total number of wickets taken by the player.

BBI (Best Bowling in an Inning): The player's best bowling performance in a single inning, represented as the number of wickets taken for the fewest runs.

AVE (Bowling Average): The average number of runs conceded per wicket taken by the player.

Econ (Economy Rate): The average number of runs conceded per over bowled by the player.

SR (Strike Rate): The average number of balls bowled per wicket taken by the player.

Fours: The total number of times the player's deliveries were hit for four runs by the batsmen.

Fives: The total number of times the player took five wickets in a single inning.
![8](https://github.com/Chinmaya54/DM_Challenge_WC_Winner/assets/75682006/d16acbae-175f-48ba-8895-8bf4db00a083)


Task 2.1 and 3 : Predicting the Finalist Teams and Winner 


You are required to predict the two finalist teams in the ICC Cricket World Cup 2023

DATASET DESCRIPTION
1. ICC CWC 23 Points Table (Scrapped)
Dataset Link : Web_Scrapping_DM_Challenge.ipynb

Source: The dataset was collected through web scraping from Cricbuzz, a prominent sports platform. It contains cricket performance details for various countries, including the number of matches played, matches won and lost, points earned, and net run rate. The use of web scraping allows for a comprehensive and up-to-date overview of cricket statistics, providing valuable insights into the performances of different teams in specific matches.
Purpose: Comprehensive overview of cricket performances by different nations.

2. ODI Men's Cricket Match Data (2002-2023)
Dataset Link : https://www.kaggle.com/datasets/utkarshtomar736/odi-mens-cricket-match-data-2002-2023

Description : This dataset provides comprehensive information about ODI cricket matches, making it suitable for analysis and research in the field of cricket statistics and performance evaluation.

ML pipeline

Extracting semifinalist teams from scrapped points table
Feature selection using correlation analysis
Splitting of data
Scaling of data
Model Training on historic data
               → Logistic Regression 
               → Decision tree Classifier
               → Random Forest Classifier
               → ANN
Model Evaluation and Testing
Prediction for finalist 
Prediction For Winner



We have used two approaches: 
Considering the problem statement as Multiclass Classification task
File : Final_ICC_WC23_predictions.ipynb 
Prediction : 
Finalists :

<img width="265" alt="2" src="https://github.com/Chinmaya54/DM_Challenge_WC_Winner/assets/75682006/e56479a6-5195-4ecd-8603-60e97424b212">

Choosing ANN Model Predicted finalists
Based on the finalists 
Winner :

Considering the problem statement as Regression task
Prediction : 
![4](https://github.com/Chinmaya54/DM_Challenge_WC_Winner/assets/75682006/ff0669e2-0532-4027-b0ac-444354dcd1ef)
![5](https://github.com/Chinmaya54/DM_Challenge_WC_Winner/assets/75682006/f38f9dc5-dc01-454f-8ba4-bc539804cb9a)

Task 2.2: Predicting the finalist teams 

Batting Dataset Link: : https://drive.google.com/file/d/1v6YTvUfGlPnohr0DtIcBQ2vQmAAtt-jY/view?usp=sharing
Bowling Dataset Link: https://drive.google.com/file/d/1hs5pvLrj-vpCWEfRPSnFgK58ZOdiS1Nr/view?usp=sharing
Source:The dataset presented here was obtained through the process of web scraping from ESPNcricinfo, a prominent and reliable source for comprehensive cricket-related information. Web scraping is a technique that automates the extraction of data from web pages, allowing us to compile a detailed dataset on various aspects of cricket matches. ESPNcricinfo, being a renowned platform, provides up-to-date and in-depth statistics, including the number of matches played, matches won and lost, points earned, and net run rate for each country. Through this web scraping process, we aim to deliver accurate and timely insights into the performance of cricket-playing nations, enabling a thorough analysis of team dynamics and tournament standings."


Prediction:

Prediction of playing eleven for Team India:-
![6](https://github.com/Chinmaya54/DM_Challenge_WC_Winner/assets/75682006/d09b55af-3ced-4c7d-a27f-b507f1f844a8)
Prediction of playing eleven for Team Australia:-
![7](https://github.com/Chinmaya54/DM_Challenge_WC_Winner/assets/75682006/3daf0551-87fa-48e9-ab83-a26942733926)

