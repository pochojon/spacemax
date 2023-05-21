const form = document.getElementById('formcontacto');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const nameInput = document.getElementById('name');
  const emailInput = document.getElementById('email');
  const messageInput = document.getElementById('message');

  console.log(nameInput.value);
  console.log(emailInput.value);
  console.log(messageInput.value);

  resetErrors();

  if (nameInput.value.trim() === '') {
    showError(nameInput, 'Por favor ingrese su nombre', 'name-error');
  }

  if (emailInput.value.trim() === '') {
    showError(emailInput, 'Por favor ingrese su direccion de email', 'email-error');
  } else if (!isValidEmail(emailInput.value)) {
    showError(emailInput, 'El mail ingresado no parece válido. Reintente', 'email-error');
  }

  if (messageInput.value.trim() === '') {
    showError(messageInput, 'Por favor dejanos un comentario de lo que necesites', 'message-error');
  }

  if (!hasErrors()) {
    console.log("todo bien")
    alert('Gracias por tu contacto nos estaremos comunicando a la brevedad');
  }
});

function showError(input, message, errorId) {
  const errorDiv = document.getElementById(errorId);
  errorDiv.innerText = message;
  input.classList.add('error-input');
}

function resetErrors() {
  const errorMessages = document.querySelectorAll('.error-message');
  errorMessages.forEach((errorMessage) => {
    errorMessage.innerText = '';
  });

  const errorInputs = document.querySelectorAll('.error-input');
  errorInputs.forEach((errorInput) => {
    errorInput.classList.remove('error-input');
  });
}

function hasErrors() {
  return document.querySelectorAll('.error-message:not(:empty)').length > 0;
}

function isValidEmail(email) {
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailPattern.test(email);
}