import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
# Unique teams present in our dattaset
unique_teams = ['Bermuda', 'Nepal', 'Sri Lanka', 'Zimbabwe', 'South Africa', 'Ireland', 'West Indies', 'Australia', 'New Zealand', 'India', 'Canada', 'United States of America', 'Afghanistan', 'Scotland', 'England', 'ICC World XI', 'Hong Kong', 'Netherlands', 'Pakistan', 'Bangladesh', 'Namibia', 'Kenya', 'United Arab Emirates']

reverse_label_mapping = {0: 'Afghanistan', 1: 'Australia', 2: 'Bangladesh', 3: 'Bermuda', 4: 'Canada',
                         5: 'England', 6: 'Hong Kong', 7: 'ICC World XI', 8: 'India', 9: 'Ireland',
                         10: 'Kenya', 11: 'Namibia', 12: 'Nepal', 13: 'Netherlands', 14: 'New Zealand',
                         15: 'Pakistan', 16: 'Scotland', 17: 'South Africa', 18: 'Sri Lanka',
                         19: 'United Arab Emirates', 20: 'United States of America', 21: 'West Indies',
                         22: 'Zimbabwe'}
# loading pickel file of trained best ann model
with open('data/ann_model.pkl', 'rb') as predictive_model:
    loaded_ann_model = pickle.load(predictive_model)

#Function for predicting winner for semifinal matches / finalists prediction 
def predict_winner(team1, team2, venue):
    # input data
    input_data = pd.DataFrame({'team1': [team1], 'team2': [team2], 'venue': [venue], 'toss_winner_encoded': [0], 'toss_decision_encoded': [0]})

    # Encoding all columns
    label_encoder = LabelEncoder()
    label_encoder.fit(unique_teams)
    input_data['team1_encoded'] = label_encoder.transform(input_data['team1'])
    input_data['team2_encoded'] = label_encoder.transform(input_data['team2'])
    input_data['venue_encoded'] = label_encoder.fit_transform(input_data['venue'])

    # Using the trained model to predict the winner
    winner_encoded = loaded_ann_model.predict(input_data[['team1_encoded', 'team2_encoded',
     'venue_encoded', 'toss_winner_encoded', 'toss_decision_encoded']])
    winner_encoded = winner_encoded[0] 

    # Reverse label encoding for predicted winner name
    winner_name = reverse_label_mapping[winner_encoded]

    return winner_name
# function for final match winner / Winner of ICC Men's WC23
def fine_winner(team1: str, team2: str, venue: str) -> str:
    winner = predict_winner(team1, team2, venue)
    return winner
