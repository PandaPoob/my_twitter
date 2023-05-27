function validatePassword() {
  const regex = /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])/;
  input = document.querySelector('input[name="user_password"]');
  document.getElementById("user_password_error_msg").style.display = "none";
  input.classList.remove("validate_error");
  const max_val = parseInt(input.getAttribute("maxlength"));
  const min_val = parseInt(input.getAttribute("min-val"));

  if (
    !(input.value.length >= min_val && input.value.length <= max_val) ||
    !regex.test(input.value)
  ) {
    document.getElementById("user_password_error_msg").style.display = "block";
    input.classList.add("validate_error");
  } else {
    document.getElementById("user_password_error_msg").style.display = "none";
    input.classList.remove("validate_error");
  }
}

function confirmPassword() {
  validatePassword();

  password = document.querySelector('input[name="user_password"]');
  input = document.querySelector('input[name="confirm_password"]');

  if (password.value !== input.value) {
    document.getElementById("confirm_password_error_msg").style.display =
      "block";
    input.classList.add("validate_error");
  } else {
    document.getElementById("confirm_password_error_msg").style.display =
      "none";
    input.classList.remove("validate_error");
  }
}
