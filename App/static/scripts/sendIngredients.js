function sendDataToBackend() {
    const tableRows = document.querySelectorAll('table tbody tr');
    let ingredientList = [];

    tableRows.forEach((row) => {
        let ingredient = row.querySelector('td:nth-child(2)').innerText; // Obtener el valor de la columna de ingredientes
        ingredientList.push(ingredient);
    });

    if (ingredientList.length === 0) {
        alert("Please add at least one ingredient!");
        return;  // Si no hay ingredientes, no envíes la solicitud
    }

    // Mostrar los ingredientes en consola y limpiar la tabla
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
    .then(data => {
        const recipesContainer = document.getElementById('recipesContainer');
        
        // Limpiar la tabla antes de agregar nuevas filas
        const tbody = recipesContainer.querySelector('tbody');
        tbody.innerHTML = '';
    
        // Verificar si hay datos en recipe_links
        if (data.recipe_links && data.recipe_links.length > 0) {
            data.recipe_links.forEach(recipe => {
                // Crear una nueva fila
                const row = document.createElement('tr');
    
                // Celda para el ingrediente
                const tdIngredient = document.createElement('td');
                tdIngredient.textContent = recipe.ingredient;
                tdIngredient.classList.add('ingredient-cell');
                row.appendChild(tdIngredient);
    
                // Celda para el enlace de la receta
                const tdRecipe = document.createElement('td');
                const link = document.createElement('a');
                link.href = recipe.url;
                link.target = '_blank';
                link.textContent = 'View Recipe';
                link.classList.add('recipe-link'); // Clase para estilos
                tdRecipe.appendChild(link);
                row.appendChild(tdRecipe);
    
                // Agregar la fila al cuerpo de la tabla
                tbody.appendChild(row);
            });
        } else {
            // Mostrar mensaje si no hay recetas
            const row = document.createElement('tr');
            const tdMessage = document.createElement('td');
            tdMessage.colSpan = 2; // Hacer que ocupe ambas columnas
            tdMessage.textContent = 'No recipes found for the ingredients.';
            tdMessage.classList.add('no-recipes-message'); // Clase para estilos
            row.appendChild(tdMessage);
            tbody.appendChild(row);
        }
    })  
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