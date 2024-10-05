function sendDataToBackend() {
    const tableRows = document.querySelectorAll('table tbody tr');
    let ingredientList = [];

    tableRows.forEach((row) => {
        let ingredient = row.querySelector('td:nth-child(2)').innerText; // Obtener el valor de la columna de ingredientes
        ingredientList.push(ingredient);
    });

    // Mostramos la lista en consola y limpiamos la tabla
    console.log('Lista de ingredientes:', ingredientList);
    document.querySelector('table tbody').innerHTML = '';

    // Enviar los datos al backend con fetch
    fetch('/groceries/process-ingredients/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')  // Incluye el CSRF token para seguridad
        },
        body: JSON.stringify({ ingredients: ingredientList })
    })
        .then(response => response.json())
        .then(data => console.log(data)) // Ver el resultado en la consola
        .catch(error => console.error('Error:', error));
}

// Esta función es necesaria para obtener el CSRF token (proteger el envío de datos)
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
// Event listener para el botón
document.getElementById('go-button').addEventListener('click', sendDataToBackend);