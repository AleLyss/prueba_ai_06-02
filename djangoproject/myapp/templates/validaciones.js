document.addEventListener('DOMContentLoaded', function () {
    // Acceder a los elementos del formulario
    const imagenInput = document.getElementById('imagen'); 
    const descripcionImagenInput = document.getElementById('descripcion');
    const nombreCategoriaImput = document.getElementById('nombre');


    imagenInput.addEventListener('change', function () {
        // Obtener el valor del campo de imagen
        const imagenValue = imagenInput.value;

        if (imagenValue.trim() === '') {
            alert('Por favor, selecciona una imagen.');
        }
    });

    descripcionImagenInput.addEventListener('change', function () {
        // Obtener el valor del campo de descripción
        const descripcionValue = descripcionImagenInput.value;

        if (descripcionValue.trim() === '') {
            alert('Por favor, ingresa una descripción.');
    
        }
    });

});
