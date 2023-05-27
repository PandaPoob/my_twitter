function validateUserName() {
  const regex = /^[a-zA-Z0-9_]*$/;
  input = document.querySelector('input[name="user_name"]');
  const max_val = parseInt(input.getAttribute("maxlength"));
  const min_val = parseInt(input.getAttribute("min-val"));

  if (
    !(input.value.length >= min_val && input.value.length <= max_val) ||
    !regex.test(input.value)
  ) {
    document.getElementById("user_name_error_msg").style.display = "block";
    input.classList.add("validate_error");
  } else {
    document.getElementById("user_name_error_msg").style.display = "none";
    input.classList.remove("validate_error");
  }
}
