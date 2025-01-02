import pickle
import numpy as np
import streamlit as st

# Load the saved model
loaded_model = pickle.load(open("creditmodel.sav", "rb"))

# Function to make predictions
def credit_predict(input_data):
    input_array = np.asarray(input_data).reshape(1, -1)  # Reshape for a single sample
    prediction = loaded_model.predict(input_array)
    
    if prediction == [0]:
        return "TRANSACTION IS LEGIT"
    else:
        return "TRANSACTION IS FRAUD"

# Main function for the Streamlit app
def main():
    # Title of the web app
    st.title("CREDIT CARD FRAUD DETECTION WEB APP")

    # Input fields for the encoded values
    inputs = []
    for i in range(1, 31):  # Loop to create 30 input fields
        value = st.text_input(f"Enter encoded value for V{i}", key=str(i))
        inputs.append(value)

    # Prediction result
    result = ""

    # When the button is clicked, the prediction is made
    if st.button("ANALYSIS TEST RESULT"):
        try:
            # Convert input values to floats
            inputs_float = [float(i) for i in inputs]
            result = credit_predict(inputs_float)
        except ValueError:
            result = "Please enter valid numeric values for all fields."
    
    st.success(result)
    st.write("Thanks for your visit!")

if __name__ == '__main__':
    main()
