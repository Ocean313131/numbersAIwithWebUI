from flask import Flask, request, jsonify
from flask_cors import CORS
import torch
import numpy as np

class numbers(torch.nn.Module):
    def __init__(self):
        super(numbers, self).__init__()
        self.hidden = torch.nn.Linear(1, 10)
        self.output = torch.nn.Linear(10, 1)

    def forward(self, x):
        x = x.unsqueeze(-1)
        x = torch.relu(self.hidden(x))
        x = self.output(x)
        return x.squeeze(-1)


app = Flask(__name__)
CORS(app)  # Erlaubt Anfragen vom Browser (wichtig für lokale Entwicklung)

model = torch.load('numbers.pkl', weights_only=False)
model.eval()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    user_input = data.get('input')

    # Input als PyTorch Tensor vorbereiten
    input_tensor = torch.tensor([float(user_input)], dtype=torch.float32)

    # Prediction mit dem Modell (KEIN .predict() – PyTorch nutzt direkten Aufruf)
    with torch.no_grad():
        prediction = model(input_tensor)

    return jsonify({'prediction': round(prediction.item(), 4)})

if __name__ == '__main__':
    app.run(debug=True)