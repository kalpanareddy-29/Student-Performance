from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load initial model and data
model = joblib.load('model.pkl')
students_df = pd.read_csv('data.csv')

@app.route('/')
def index():
    return render_template(r'C:\Users\kalpa\Desktop\Hackathon\Templates\home.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the year from the form
    year = request.form.get('year')
    
    # Filter students based on the year
    filtered_students = students_df[students_df['year'] == year]
    
    if filtered_students.empty:
        return jsonify({'error': 'No students found for the specified year.'})
    
    # Prepare features for prediction
    X = filtered_students[['percentage', 'local_hackathons_participated', 'local_hackathons_won', 
                           'paper_presentations', 'national_hackathons_participated',
                           'national_hackathons_won', 'certifications', 'rnd_work_rating', 
                           'social_interactions', 'paper_publications']]

    # Predict using the loaded model
    predictions = model.predict(X)

    # Add predictions to the DataFrame
    filtered_students['predicted_score'] = predictions

    # Get the top 3 students based on predicted scores
    top_students = filtered_students.nlargest(3, 'predicted_score')

    # Prepare the response data
    top_students_info = top_students[['id', 'student_name', 'predicted_score']].to_dict(orient='records')
    
    return jsonify(top_students_info)

@app.route('/update_model', methods=['GET', 'POST'])
def update_model():
    if request.method == 'POST':
        model_file = request.form.get('model_file')
        
        if model_file and model_file.endswith('.pkl'):
            try:
                global model
                model = joblib.load(model_file)  # Load the new model
                return jsonify({'success': 'Model updated successfully!'})
            except Exception as e:
                return jsonify({'error': f'Error loading model: {str(e)}'})
        else:
            return jsonify({'error': 'Invalid model file. Please ensure it ends with .pkl'})

    return render_template('update_model.html')

if __name__ == '__main__':
    app.run(debug=True)
 
    
