async function handleSubmitSignup() {
  //Disable btn and add loader
  const btn = event.target;
  btn.disabled = true;
  document.getElementById("form_default").style.display = "none";
  document.getElementById("form_loading").style.display = "block";

  const frm = event.target;

  const resp = await fetch("/api-signup", {
    method: "POST",
    body: new FormData(frm),
  });

  if (!resp.ok) {
    const data = await resp.json();
    //Reset button state
    document.getElementById("form_default").style.display = "block";
    document.getElementById("form_loading").style.display = "none";
    //Show toaster
    displayToasterTop(data.info);
    return;
  } else if (resp.ok) {
    document.getElementById(`signup_form_container`).style.display = "none";
    document.getElementById(`heading`).style.display = "none";
    document.getElementById(`signup_success_container`).style.display = "block";
  }
}

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

function getAge(date) {
  let today = new Date();
  let birthDate = new Date(date);
  let age = today.getFullYear() - birthDate.getFullYear();
  let m = today.getMonth() - birthDate.getMonth();
  if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
    age--;
  }
  return age;
}

function validateBirthday() {
  input = document.querySelector('input[name="user_birthday"]');
  document.getElementById("user_birthday_error_msg").style.display = "none";
  input.classList.remove("validate_error");
  let age = getAge(input.value.replaceAll("-", "/"));

  if (input.value.length === 0 || age < 13) {
    document.getElementById("user_birthday_error_msg").style.display = "block";
    input.classList.add("validate_error");
  } else {
    document.getElementById("user_birthday_error_msg").style.display = "none";
    input.classList.remove("validate_error");
  }
}

function userNamecounter() {
  input = document.querySelector('input[name="user_name"]');
  document.getElementById("user_name_error_msg").style.display = "none";
  input.classList.remove("validate_error");

  const counter = document.querySelector(".user_name_no");
  counter.innerHTML = input.value.length;
}

function checkSignupForm() {
  validateFullName();
  validateEmail();
  validateBirthday();
  validateUserName();
  validatePassword();
  confirmPassword();

  const form = event.target;
  if (!form.querySelector(".validate_error")) {
    handleSubmitSignup();
  }
}
