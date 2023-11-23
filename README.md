# DM_Challenge_ICC_Mens_WC23_Winner
Data Mining Challenge , Predict winner of Cricket World Cup 2023

**Documentation for CP-03
By Group -16**

PROJECT PIPELINE

-> Understanding of Data (Problem Statement)

-> Data Preprocessing - checked null values, attribute types, duplicate values etc

-> Data Visualization - 
 --Distribution plots
 --Scatter Plots
 --Box Plots
 --Count Plots
 --Barplots
 --Heatmap

**Contributions :** 
Chinmaya (202218054) 
TASK 2.1 and 3 : Predicting Finalist and Winner (Multiclass Classification)/ whole ML prediction process,
Model deployment using FastAPI 

Riya (202218049) 
TASK 1 :  Preprocessing, EDA and Predicting cricketers likely to achieve the highest runs, wickets, and catches along with their respective countries.
Data Extraction through Kaggle

Swayista (202218035)
TASK 2.1 and 3 : Predicting Finalist and Winner (Regression)/ whole ML prediction process,
Dataset Generation for  points tabel, EDA and analysis of finalists performance 

Asish (202218022) 
 TASK 2.2: Predicting Playing 11 for Finalist,
 Dataset Generation for teams performance and fixtures

Kashish (202001425)
TASK 2 and 3 : Scrapping data for playing 11 and players stats, Extracting data for finalists and winner prediction from Kaggle, EDA and thorough analysis of semifinalist teams, Documentation


**DETAILED DESCRIPTION OF EACH TASK**
_**Task 1 : Creative problem prediction** _

_**FILE : Data_Mining(Scrapped)_CP_03_Riya.ipynb**_
_ML pipeline_
-> Feature selection using correlation analysis
-> Splitting of data
-> Scaling of data
-> Model Fitting 
               → Linear Regression
               → Decision tree
               → Random Forest Regression
               → ANN
-> Model Evaluation and Testing

_Problem Statement :_ 
**1)Predicting the batsman who will score most runs in the tournament.**
The data has been scraped from the provided link - https://www.espncricinfo.com/records/tournament/batting-most-runs-career/icc-cricket-world-cup-2023-24-15338
_Dataset Description for most runs :_ 
- Player: The name of the cricket player who took the wickets.

- Country: The country for which the player represents or plays international cricket.

- Span: The time period (range of years) during which the player's career spanned.

- Matches: The total number of matches the player participated in.

- Innings: The total number of bowling innings bowled by the player.

- Balls: The total number of balls bowled by the player.

- Overs: The total number of overs bowled by the player. An over consists of six legal deliveries.

- MDNS: The total number of maidens bowled by the player. A maiden over is an over in which no runs are scored.

- Runs: The total number of runs conceded by the player.

- Wickets: The total number of wickets taken by the player.

- BBI (Best Bowling in an Inning): The player's best bowling performance in a single inning, represented as the number of wickets taken for the fewest runs.

- AVE (Bowling Average): The average number of runs conceded per wicket taken by the player.

- Econ (Economy Rate): The average number of runs conceded per over bowled by the player.

- SR (Strike Rate): The average number of balls bowled per wicket taken by the player.

- Fours: The total number of times the player's deliveries were hit for four runs by the batsmen.

- Fives: The total number of times the player took five wickets in a single inning.

![1](https://github.com/Chinmaya54/DM_Challenge_WC_Winner/assets/75682006/9de7d024-dddc-419e-9cd6-5b401835fea9)



**2)Predicting the player who will  have the most catches in the tournament.**
The data has been scraped from the provided link - 
https://www.espncricinfo.com/records/tournament/fielding-most-catches-career/icc-cricket-world-cup-2023-24-15338

_Dataset Description for most catches :_ 
- Player: The name of the cricket player who took catches.

- Country: The country for which the player represents or plays international cricket.

- Span: The time period (range of years) during which the player's career spanned.

- Matches: The total number of matches the player participated in.

- Innings: The total number of fielding innings the player was involved in.

- CT (Catches): The total number of catches taken by the player.

- Max: The maximum number of catches taken by the player in a single match.

- Ct/Inns (Catches per Inning): The average number of catches taken by the player per fielding inning.

![ctinns](https://github.com/Chinmaya54/DM_Challenge_WC_Winner/assets/75682006/e0e34d47-f6cc-4ce6-88ab-4393c79aaed9)



**3)Predicting the bowler who will  have the most wickets in the tournament.**
The data has been scraped from the provided link - 
https://www.espncricinfo.com/records/tournament/bowling-most-wickets-career/icc-cricket-world-cup-2023-24-15338

_Dataset Description for most wickets :_
- Player: The name of the cricket player who took the wickets.

- Country: The country for which the player represents or plays international cricket.

- Span: The time period (range of years) during which the player's career spanned.

- Matches: The total number of matches the player participated in.

- Innings: The total number of bowling innings bowled by the player.

- Balls: The total number of balls bowled by the player.

- Overs: The total number of overs bowled by the player. An over consists of six legal deliveries.

- MDNS: The total number of maidens bowled by the player. A maiden over is an over in which no runs are scored.

- Runs: The total number of runs conceded by the player.

- Wickets: The total number of wickets taken by the player.

- BBI (Best Bowling in an Inning): The player's best bowling performance in a single inning, represented as the number of wickets taken for the fewest runs.

- AVE (Bowling Average): The average number of runs conceded per wicket taken by the player.

- Econ (Economy Rate): The average number of runs conceded per over bowled by the player.

- SR (Strike Rate): The average number of balls bowled per wicket taken by the player.

- Fours: The total number of times the player's deliveries were hit for four runs by the batsmen.

- Fives: The total number of times the player took five wickets in a single inning.
![8](https://github.com/Chinmaya54/DM_Challenge_WC_Winner/assets/75682006/d16acbae-175f-48ba-8895-8bf4db00a083)


**_Task 2.1 and 3 : Predicting the Finalist Teams and Winner of the ICC Cricket World Cup 2023_**

_DATASET DESCRIPTION_
**1. ICC CWC 23 Points Table (Scrapped)**
_Dataset Link_ : Web_Scrapping_DM_Challenge.ipynb
_Description_: The dataset was collected through web scraping from Cricbuzz, a prominent sports platform. It contains cricket performance details for various countries, including the number of matches played, matches won and lost, points earned, and net run rate. The use of web scraping allows for a comprehensive and up-to-date overview of cricket statistics, providing valuable insights into the performances of different teams in specific matches.
**Note**: Attributes description in provided in the respective ipynb file
_Purpose_: Comprehensive overview of cricket performances by different nations.

**2. ODI Men's Cricket Match Data (2002-2023)**
_Dataset Link_ : https://www.kaggle.com/datasets/utkarshtomar736/odi-mens-cricket-match-data-2002-2023
_Description_ : This dataset provides comprehensive information about ODI cricket matches, making it suitable for analysis and research in the field of cricket statistics and performance evaluation.
**Note**: Attributes description in provided in the respective ipynb file

**ML pipeline**

-> Extracting semifinalist teams from scrapped points table
-> Feature selection using correlation analysis
-> Splitting of data
-> Scaling of data
-> Model Training on historic data
               → Logistic Regression 
               → Decision tree Classifier
               → Random Forest Classifier
               → ANN
-> Model Evaluation and Testing
-> Prediction for finalist 
-> Prediction For Winner

We have used two approaches: 
**1)Considering the problem statement as Multiclass Classification task**
_**File : Final_ICC_WC23_predictions.ipynb**_
Prediction : 
-->**Finalists** :

<img width="265" alt="2" src="https://github.com/Chinmaya54/DM_Challenge_WC_Winner/assets/75682006/e56479a6-5195-4ecd-8603-60e97424b212">

Choosing _ANN Model_ 
Predicted finalists: 
**_India and Australia_**

Based on the finalists 
_**Winner :**_
<img width="249" alt="image" src="https://github.com/Chinmaya54/DM_Challenge_WC_Winner/assets/137144018/3eca8e39-6c7e-45d4-9ead-77340fa04db9">

_**AUSTRALIA :(**_


**2)Considering the problem statement as Regression task**
_**File: Final_Regression_TaskDM_3.ipynb**_ 
Predictions : 
![4](https://github.com/Chinmaya54/DM_Challenge_WC_Winner/assets/75682006/ff0669e2-0532-4027-b0ac-444354dcd1ef)
![5](https://github.com/Chinmaya54/DM_Challenge_WC_Winner/assets/75682006/f38f9dc5-dc01-454f-8ba4-bc539804cb9a)

**Task 2.2: Predicting the finalist teams/Playing 11**
**_File: Prediction_of_Playing_11_DATA_MINING_.ipynb**
DATASET DESCRIPTION
_Batting Dataset Link:_ : https://drive.google.com/file/d/1v6YTvUfGlPnohr0DtIcBQ2vQmAAtt-jY/view?usp=sharing
_Bowling Dataset Link:_ https://drive.google.com/file/d/1hs5pvLrj-vpCWEfRPSnFgK58ZOdiS1Nr/view?usp=sharing

_Description:_ The dataset presented here was obtained through the process of web scraping from ESPNcricinfo, a prominent and reliable source for comprehensive cricket-related information. Web scraping is a technique that automates the extraction of data from web pages, allowing us to compile a detailed dataset on various aspects of cricket matches. ESPNcricinfo, being a renowned platform, provides up-to-date and in-depth statistics, including the number of matches played, matches won and lost, points earned, and net run rate for each country. Through this web scraping process, we aim to deliver accurate and timely insights into the performance of cricket-playing nations, enabling a thorough analysis of team dynamics and tournament standings.

**Prediction of playing eleven for Team India:-**

![final1](https://github.com/Chinmaya54/DM_Challenge_WC_Winner/assets/75682006/ed9a6fcf-198b-4e0c-8f72-3a8ce47d379b)

**Prediction of playing eleven for Team Australia:-**

![final2](https://github.com/Chinmaya54/DM_Challenge_WC_Winner/assets/75682006/4df1ebb8-9146-4df7-b270-598f9724dde0)


_**Task : Design, develop, and deploy an ML RESTful API**_ 
Choosen API : FastAPI
_**File: FastAPI.zip**_
Best ANN model is deployed using the FastAPI
**STEPS:**
Step 1: Install FastAPI and Uvicorn
Step 2: Create a FastAPI object
Step 3: Design Your API, **file : main.py**
Step 4: Define an ML Endpoint
Step 5: Run the FastAPI Application Locally
Step 6: Integrate ANN Model , **file: modelInference.py**
For this we have created an additional API endpoint /predict_winner that uses the loaded ANN model(pkl file) to predict the winner of a match based on the provided input data (team1, team2, venue).
Step 7: Test the Endpoint using Thunder Client
URL- [http://127.0.0.1:8000/predict_winner](http://127.0.0.1:8000/winnerpredict)http://127.0.0.1:8000/winnerpredict

**RESPONSES:**
