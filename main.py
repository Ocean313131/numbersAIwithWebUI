import torch


# Step 1: Generate Training Data
# Input: Numbers from 0 to 99, Output: Next number
X = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=torch.float32)  # No reshaping needed
y = torch.tensor([2, 3, 4, 5, 6, 7, 8, 9, 10, 11], dtype=torch.float32)  # No reshaping needed

# Step 2: Define the Model
class numbers(torch.nn.Module):
    def __init__(self):
        super(numbers, self).__init__()
        self.hidden = torch.nn.Linear(1, 10)  # Hidden layer with 10 neurons
        self.output = torch.nn.Linear(10, 1)  # Output layer

    def forward(self, x):
        x = x.unsqueeze(-1)  # Add a dimension to make it (batch_size, 1)
        x = torch.relu(self.hidden(x))  # Apply ReLU activation
        x = self.output(x)  # Output layer
        return x.squeeze(-1)  # Remove the added dimension for output

model = numbers()

# Step 3: Define Loss Function and Optimizer
criterion = torch.nn.MSELoss()  # Mean Squared Error Loss
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)  # Adam optimizer

# Step 4: Train the Model
epochs = 100
for epoch in range(epochs):
    model.train()
    optimizer.zero_grad()  # Clear gradients
    predictions = model(X)  # Forward pass
    loss = criterion(predictions, y)  # Compute loss
    loss.backward()  # Backward pass
    optimizer.step()  # Update weights

    print(f"Epoch {epoch + 1}/{epochs}, Loss: {loss.item()}")

# Step 5: Test the Model
model.eval()
with torch.no_grad():
    test_input = torch.tensor([11], dtype=torch.float32)  # Test input
    predicted_output = model(test_input)  # Get prediction
    print(f"Input: {test_input.item()}, Predicted Output: {predicted_output.item()}")

# Step 6: Save the Model
torch.save(model, 'numbers.pkl')  # Save the trained model to a file
print("Model saved as 'numbers.pkl'")