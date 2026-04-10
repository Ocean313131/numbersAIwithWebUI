// Select the form and input field
const form = document.getElementById('userForm'); // Ensure the id matches the form in HTML
const inputField = document.getElementById('input');

// Add an event listener for form submission
form.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission behavior

    // Get the value from the input field
    const userInput = inputField.value;

    // Save the value (e.g., in localStorage or a variable)
    console.log('User Input: ', userInput); // Log the input to the console
    localStorage.setItem('userInput', userInput); // Save to localStorage
    // Optionally, clear the input field
    inputField.value = '';

    vent.preventDefault();

    // Send the input to the Flask server
    fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ input: userInput })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Prediction:', data.prediction); // Log the prediction
        alert(`Prediction: ${data.prediction}`); // Optionally show the prediction
    })
    .catch(error => console.error('Error:', error));

    inputField.value = ''; // Clear the input field
});
