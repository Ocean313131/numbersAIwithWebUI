from flask import Flask, request, jsonify
import torch
import numpy as np

class numbers(torch.nn.Module):
    def __init__(self):
        super(numbers, self).__init__()
        self.linear = torch.nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)


app = Flask(__name__)

# Load your trained AI model
model = torch.load('numbers.pkl', weights_only=False)  # Replace with your model file

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Get JSON data from the request
    user_input = data.get('input')  # Extract the 'input' field

    # Preprocess the input if necessary
    # Example: Convert to numpy array or reshape
    input_array = np.array([float(user_input)])  # Adjust based on your model's input format

    # Make prediction
    prediction = model.predict(input_array)

    # Return the prediction as JSON
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)