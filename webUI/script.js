const form = document.getElementById('userForm');
const inputField = document.getElementById('input');
const outputEl = document.getElementById('modelOutput');

form.addEventListener('submit', function(event) {
    event.preventDefault(); // Tippfehler "vent" war hier der Bug – jetzt korrekt

    const userInput = inputField.value.trim();
    if (!userInput) return;

    outputEl.textContent = 'Lädt...';

    fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ input: userInput })
    })
    .then(response => response.json())
    .then(data => {
        outputEl.textContent = data.prediction; // Output direkt in der UI anzeigen
    })
    .catch(error => {
        console.error('Error:', error);
        outputEl.textContent = 'Fehler – läuft der Flask-Server?';
    });

    inputField.value = '';
});