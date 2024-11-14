const fieldName = document.getElementById("nombre");
const fieldEmail = document.getElementById("email");
const fieldPassword = document.getElementById("password");
const fieldConfirmPassword = document.getElementById("confirm_password");

function validateName(e) {
  const htmlTarget = e ? e.target : tag; // Verifica si hay un evento, de lo contrario usa una referencia global (tag)
  const fieldValue = htmlTarget.value; // Obtiene el valor ingresado en el campo

  const errorDiv = e.target.nextElementSibling; // Accede al elemento que sigue al campo (normalmente un div para mensajes de error)

  // Validaciones
  if (fieldValue.trim().length === 0) {
    // Si el campo está vacío
    errorDiv.textContent = "No has escrito todavia el nombre del producto"; // Muestra mensaje de error
    errorDiv.classList.add("error-message"); // Añade una clase CSS para resaltar el error
    disabled = true; // Desactiva el botón de confirmación
  } else if (fieldValue.trim().length < 3) {
    // Si el nombre del producto es muy corto
    errorDiv.textContent = "El nombre del producto es muy corto";
    errorDiv.classList.add("error-message");
    disabled = true;
  } else {
    // Si la validación es exitosa
    errorDiv.textContent = ""; // Limpia el mensaje de error
    errorDiv.classList.remove("error-message"); // Quita la clase de error
    disabled = false; // Habilita el botón de confirmación
  }
}

function validateEmail(e) {
  const htmlTarget = e ? e.target : tag; // Verifica si hay un evento, de lo contrario usa una referencia global (tag)
  const fieldValue = htmlTarget.value.trim(); // Obtiene el valor ingresado en el campo y quita espacios
  const errorDiv = htmlTarget.nextElementSibling; // Accede al elemento que sigue al campo (normalmente un div para mensajes de error)

  // Expresión regular para verificar el formato de email
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  // Validaciones
  if (fieldValue.length === 0) {
    // Si el campo está vacío
    errorDiv.textContent = "No has escrito tu email aún";
    errorDiv.classList.add("error-message"); // Añade una clase CSS para resaltar el error
    disabled = true; // Desactiva el botón de confirmación
  } else if (!emailRegex.test(fieldValue)) {
    // Si el formato del email es inválido
    errorDiv.textContent = "Formato de email no válido";
    errorDiv.classList.add("error-message");
    disabled = true;
  } else {
    // Si la validación es exitosa
    errorDiv.textContent = ""; // Limpia el mensaje de error
    errorDiv.classList.remove("error-message"); // Quita la clase de error
    disabled = false; // Habilita el botón de confirmación
  }
}

function validatPassword(e) {
  const htmlTarget = e ? e.target : tag; // Verifica si hay un evento, de lo contrario usa una referencia global (tag)
  const fieldValue = htmlTarget.value; // Obtiene el valor ingresado en el campo

  const errorDiv = e.target.nextElementSibling; // Accede al elemento que sigue al campo (normalmente un div para mensajes de error)

  // Validaciones
  if (fieldValue.trim().length === 0) {
    // Si el campo está vacío
    errorDiv.textContent = "No has escrito tu contraseña aun"; // Muestra mensaje de error
    errorDiv.classList.add("error-message"); // Añade una clase CSS para resaltar el error
    disabled = true; // Desactiva el botón de confirmación
  } else if (fieldValue.trim().length < 3) {
    // Si el nombre del producto es muy corto
    errorDiv.textContent = "El nombre de tu contraseña es muy corto";
    errorDiv.classList.add("error-message");
    disabled = true;
  } else {
    // Si la validación es exitosa
    errorDiv.textContent = ""; // Limpia el mensaje de error
    errorDiv.classList.remove("error-message"); // Quita la clase de error
    disabled = false; // Habilita el botón de confirmación
  }
}

function validateConfirmPassword(e) {
  const htmlTarget = e ? e.target : tag; // Verifica si hay un evento, de lo contrario usa una referencia global (tag)
  const confirmPasswordValue = htmlTarget.value.trim(); // Obtiene el valor ingresado en el campo de confirmación
  const errorDiv = htmlTarget.nextElementSibling; // Accede al elemento que sigue al campo (normalmente un div para mensajes de error)

  // Obtiene el valor de la contraseña original
  const passwordField = document.getElementById("password"); // Asegúrate de que este sea el ID del campo de contraseña
  const passwordValue = passwordField.value.trim();

  // Validaciones
  if (confirmPasswordValue.length === 0) {
    // Si el campo está vacío
    errorDiv.textContent = "No has confirmado tu contraseña aún";
    errorDiv.classList.add("error-message"); // Añade una clase CSS para resaltar el error
    disabled = true; // Desactiva el botón de confirmación
  } else if (confirmPasswordValue !== passwordValue) {
    // Si las contraseñas no coinciden
    errorDiv.textContent = "Las contraseñas no coinciden";
    errorDiv.classList.add("error-message");
    disabled = true;
  } else {
    // Si la validación es exitosa
    errorDiv.textContent = ""; // Limpia el mensaje de error
    errorDiv.classList.remove("error-message"); // Quita la clase de error
    disabled = false; // Habilita el botón de confirmación
  }
}

fieldName?.addEventListener("blur", validateName);
fieldEmail?.addEventListener("blur", validateEmail);
fieldPassword?.addEventListener("blur", validatPassword);
fieldConfirmPassword?.addEventListener("blur", validateConfirmPassword);

fieldEmail?.addEventListener("input", validateEmail);
