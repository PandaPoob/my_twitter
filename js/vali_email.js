function resetEmailVal() {
  input = document.querySelector('input[name="user_email"]');
  document.getElementById("user_email_error_msg").style.display = "none";
  input.classList.remove("validate_error");
}

function validateEmail() {
  input = document.querySelector('input[name="user_email"]');
  const regex =
    /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-ZæøåÆØÅ\-0-9]+\.)+[a-zA-ZæøåÆØÅ]{2,}))$/;

  const max_val = parseInt(input.getAttribute("max-val"));
  const min_val = parseInt(input.getAttribute("min-val"));
  if (
    !(input.value.length >= min_val && input.value.length <= max_val) ||
    !regex.test(input.value)
  ) {
    document.getElementById("user_email_error_msg").style.display = "block";
    input.classList.add("validate_error");
    console.log("HERE");
  } else {
    document.getElementById("user_email_error_msg").style.display = "none";
    input.classList.remove("validate_error");
  }
}
