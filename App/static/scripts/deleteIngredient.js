// Comentario: Lógica para agregar y eliminar ingredientes dinámicamente
document.addEventListener('DOMContentLoaded', function () {
    const addIngredientBtn = document.getElementById('addIngredientBtn');
    const ingredientInput = document.getElementById('ingredientInput');
    const ingredientTable = document.getElementById('ingredientTable').getElementsByTagName('tbody')[0];

    let ingredientCount = 0;

    // Función para agregar un ingrediente a la tabla
    function addIngredient() {
        const ingredient = ingredientInput.value.trim();

        if (ingredient) {
            ingredientCount++;

            // Crear una fila con el nuevo ingrediente
            const newRow = ingredientTable.insertRow();
            newRow.innerHTML = `
                        <tr>
                            <td>${ingredientCount}</td>
                            <td>${ingredient}</td>
                            <td><button class="ingredient-btn btn-danger btn-sm deleteBtn">Delete</button></td>
                        </tr>
                    `;

            // Limpiar el input después de agregar
            ingredientInput.value = '';

            // Agregar funcionalidad de eliminación al botón
            const deleteBtn = newRow.querySelector('.deleteBtn');
            deleteBtn.addEventListener('click', function () {
                ingredientTable.deleteRow(newRow.rowIndex - 1);
                ingredientCount--;
            });
        }
    }

    // Evento para el botón de agregar ingrediente
    addIngredientBtn.addEventListener('click', addIngredient);

    // Comentario: Permitir agregar el ingrediente con la tecla "Enter"
    ingredientInput.addEventListener('keydown', function (event) {
        if (event.key === 'Enter') {
            event.preventDefault(); // Evitar que el formulario se envíe
            addIngredient(); // Llamar a la función para agregar ingrediente
        }
    });
});