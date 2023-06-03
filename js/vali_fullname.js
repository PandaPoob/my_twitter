function fullNameCounter() {
  input = document.querySelector('input[name="user_full_name"]');
  document.getElementById("user_full_name_error_msg").style.display = "none";
  input.classList.remove("validate_error");
  const counter = document.querySelector(".full_name_no");
  counter.innerHTML = input.value.length;
}

function validateFullName() {
  //handle fullname
  input = document.querySelector('input[name="user_full_name"]');
  const min_val = parseInt(input.getAttribute("min-val"));

  if (input.value.length < min_val) {
    document.getElementById("user_full_name_error_msg").style.display = "block";
    input.classList.add("validate_error");
  } else {
    input = document.querySelector('input[name="user_full_name"]');
    document.getElementById("user_full_name_error_msg").style.display = "none";
  }
}
