document.getElementById('calculate').addEventListener('click', function() {
    const num1 = document.getElementById('num1').value;
    const num2 = document.getElementById('num2').value;
    const operation = document.getElementById('operation').value;

    // Input validation
    if (!num1 || !num2) {
        document.getElementById('result').innerText = 'Error: Both numbers are required.';
        return;
    }

    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ num1, num2, operation })
    })
    .then(response => response.json())
    .then(data => {
        if (data.result !== undefined) {
            document.getElementById('result').innerText = 'Result: ' + data.result;
        } else {
            document.getElementById('result').innerText = 'Error: ' + data.error;
        }
    })
    .catch(error => {
        document.getElementById('result').innerText = 'Error: ' + error.message;
    });
});
