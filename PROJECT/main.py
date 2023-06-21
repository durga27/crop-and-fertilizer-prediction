import streamlit as st
import joblib

# Load the trained model
model = joblib.load('classifier.pkl')
fertilizer_labels = {
    0: '10-26-26',
    1: '14-35-14',
    2: '17-17-17',
    3: '20-20',
    4: '28-28',
    5: 'DAP',
    6: 'Urea',
    # Add more labels as needed
}
soil_type_labels = {
    0: 'Black',
    1: 'Clayey',
    2: 'Loamy',
    3: 'Red',
    4: 'Sandy'
}

# Define a dictionary to map numerical crop values to string labels
crop_labels = {
    0: 'Barley',
    1: 'Cotton',
    2: 'Ground Nuts',
    3: 'Maize',
    4: 'Millets',
    5: 'Oil seeds',
    6: 'Paddy',
    7: 'Pulses',
    8: 'Sugarcane',
    9: 'Tobacco',
    10: 'Wheat',
    # Add more labels as needed
}

def predict_fertilizer(temperature, humidity, moisture, soil_type, crop, nitrogen, potassium, phosphorous):
    # Perform any required preprocessing on the input data
    # (e.g., encoding categorical variables, feature scaling)

    # Create a feature vector with the input values
    features = [temperature, humidity, moisture, soil_type, crop, nitrogen, potassium, phosphorous]

    # Make the fertilizer prediction using the trained model
    fertilizer_prediction = model.predict([features])[0]

    return fertilizer_prediction

def main():
    # Set the app title
    st.title('Fertilizer Prediction')

    # Add input fields for the user to enter the attribute



def predict_fertilizer(temperature, humidity, moisture, soil_type, crop, nitrogen, potassium, phosphorous):
    # Perform any required preprocessing on the input data
    # (e.g., encoding categorical variables, feature scaling)

    # Create a feature vector with the input values
    features = [temperature, humidity, moisture, soil_type, crop, nitrogen, potassium, phosphorous]

    # Make the fertilizer prediction using the trained model
    fertilizer_prediction = model.predict([features])[0]

    return fertilizer_prediction



def main():
    # Set the app title
    st.title('Fertilizer Prediction')

    # Add input fields for the user to enter the attribute values
    temperature = st.number_input('Temperature', 25,38)
    humidity = st.number_input('Humidity', 50,72)
    moisture = st.number_input('Moisture',25,65)
    soil_type = st.selectbox('Soil Type', list(soil_type_labels.keys()), format_func=lambda x: soil_type_labels.get(x, 'Unknown'))
    crop = st.selectbox('Crop', list(crop_labels.keys()), format_func=lambda x: crop_labels.get(x, 'Unknown'))
    nitrogen = st.number_input('Nitrogen',4,42)
    potassium = st.number_input('Potassium',0,19 )
    phosphorous = st.number_input('Phosphorous',0,42)

    # Make the fertilizer prediction when the user clicks the 'Predict' button
    if st.button('Predict'):
        fertilizer_prediction = predict_fertilizer(temperature, humidity, moisture, soil_type, crop, nitrogen, potassium, phosphorous)

        # Convert the numerical prediction to string format using the fertilizer_labels dictionary
        fertilizer_prediction_str = fertilizer_labels.get(fertilizer_prediction, 'Unknown Fertilizer')
        st.success(f'Predicted Fertilizer: {fertilizer_prediction_str}')

if __name__ == '__main__':
    main()