import pandas as pd
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_squared_error, r2_score
df = pd.read_csv(r'C:\Users\kalpa\Desktop\Hackathon\student.csv')
df.columns = df.columns.str.strip()
label_encoder = LabelEncoder()
if 'Student Name' in df.columns:
    df['Student Name'] = label_encoder.fit_transform(df['Student Name'])
df['Initial Performance Score'] = sum(df[column] * weight for column, weight in weights.items())
df['Rank'] = df['Initial Performance Score'].rank(ascending=False)
weights = {
    'CGPA': 0.25,  # 25% weight  # 8% weight
    'Local Hackathons Participated': 0.07,
    'Local Hackathons Won': 0.08,# 7% weight
    'Paper Presentations': 0.08,  # 8% weight
    'Paper Presentations': 0.07,  # 7% weight
    'National Level Hackathons Won': 0.12,  # 12% weight
    'Certifications': 0.1,  # 10% weight
    'R&D Work Rating': 0.08,  # 8% weight
    'Social Interactions': 0.05,  # 5% weight
    'Paper Publications': 0.1   # 10% weight
}
df['Initial Performance Score'] = sum(df[column] * weight for column, weight in weights.items())
df['Rank'] = df['Initial Performance Score'].rank(ascending=False)

# Display the top 3 students based on the initial score
top_students_initial = df.nlargest(3, 'Initial Performance Score')
features = df.drop(columns=['ID Number', 'Year', 'Initial Performance Score', 'Rank','Department'])
target = df['Initial Performance Score']
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"\nModel Evaluation:")
print(f"Mean Squared Error: {mse:.4f}")
print(f"R² Score: {r2:.4f}")
year_input = int(input("Enter the year to get the top 3 students using ML predictions: "))

year_data = df[df['Year'] == year_input]
if year_data.empty:
    print(f"No data found for the year {year_input}.")
else:
    year_data['Predicted Performance Score'] = model.predict(year_data.drop(columns=['ID Number', 'Year', 'Initial Performance Score', 'Rank','Department']))

    top_students_ml = year_data[['ID Number', 'Student Name', 'Predicted Performance Score','Department']].nlargest(3, 'Predicted Performance Score')

    print(f"\nTop 3 Students for the year {year_input} using ML predictions:")
    print(top_students_ml)