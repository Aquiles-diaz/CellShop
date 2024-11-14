document.addEventListener("DOMContentLoaded", function () {
  Toastify({
    text: "¡Bienvenido y Gracias por Contactarnos!",
    duration: 2200,
    destination: "../Pages/Contacto.html",
    newWindow: true,
    close: true,
    gravity: "top", // `top` or `bottom`
    position: "right", // `left`, `center` or `right`
    stopOnFocus: true, // Prevents dismissing of toast on hover
    style: {
      background: "linear-gradient(to right, #009,#009 ,  #0098d9 , #0098d9 )",
    },
    onClick: function () {}, // Callback after click
  }).showToast();

  // Agregando events a los campos de entrada
  document.getElementById("nombre").addEventListener("blur", validarNombre);
  document.getElementById("email").addEventListener("blur", validarEmail);
  document.getElementById("form").addEventListener("submit", validarFormulario);
});
function validarNombre() {
  const nombre = document.getElementById("nombre").value;
  const nombreRegex = /^[ A-Za-záéíóúÁÉÍÓÚÑñ ]+$/;

  if (nombre === "") {
    Swal.fire({
      icon: "error",
      title: "Oops...",
      text: "Por favor, completa el campo de nombre.",
      footer: '<a href="#">¿Por qué tengo este problema?</a>',
    });
  } else if (!nombreRegex.test(nombre)) {
    Swal.fire({
      icon: "error",
      title: "Oops...",
      text: "Por favor, ingrese un carácter válido para el nombre (solo letras).",
      footer: '<a href="#">¿Por qué tengo este problema?</a>',
    });
  }
}
function validarEmail() {
  const email = document.getElementById("email").value;
  if (email === "") {
    Swal.fire({
      icon: "error",
      title: "Oops...",
      text: "Por favor, completa el campo de email.",
      footer: '<a href="#">¿Por qué tengo este problema?</a>',
    });
  }
}
function validarFormulario() {
  // obtener los value
  const nombre = document.getElementById("nombre").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const confirmPassword = document.getElementById("confirm_password").value;

  // campos vacio
  if (
    nombre === "" ||
    email === "" ||
    password === "" ||
    confirmPassword === ""
  ) {
    Swal.fire({
      icon: "error",
      title: "Oops...",
      text: "Por favor, completa todos los campos.",
      footer: '<a href="#">¿Por qué tengo este problema?</a>',
    });
    return false;
  }
  // oincidencia de psw
  if (password !== confirmPassword) {
    Swal.fire({
      icon: "error",
      title: "Oops...",
      text: "Las contraseñas no coinciden. Por favor, verifica.",
      footer: '<a href="#">¿Por qué tengo este problema?</a>',
    });
    return false;
  }

  // Validate lenght the psw
  if (password.length < 6) {
    Swal.fire({
      icon: "error",
      title: "Oops...",
      text: "La contraseña debe tener al menos 6 caracteres.",
      footer: '<a href="#">¿Por qué tengo este problema?</a>',
    });
    return false;
  }
  return true; // si es correcto el formulario regresa true
}
