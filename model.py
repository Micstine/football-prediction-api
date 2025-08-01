import pandas as pd
import random

def load_matches():
    df = pd.read_csv("sample_matches.csv")
    predictions = []

    for _, row in df.iterrows():
        # Sample rule-based prediction
        combined_goals = row['home_goals_avg'] + row['away_goals_avg']
        if combined_goals > 3.0:
            prediction = "Over 2.5 Goals"
            confidence = random.randint(80, 95)
            reason = f"Both teams average high goals per game ({combined_goals:.1f})."
        else:
            prediction = "Under 2.5 Goals"
            confidence = random.randint(65, 80)
            reason = f"Low scoring tendency ({combined_goals:.1f})."

        predictions.append({
            "sport": "Football",
            "match": f"{row['home_team']} vs {row['away_team']}",
            "prediction": prediction,
            "confidence": confidence,
            "reason": reason,
            "h2h": row['last_5_h2h'].split(',')
        })
    return predictions
