async function handleSubmitSms() {
  //Disable btn and add loader
  const btn = event.target;
  btn.disabled = true;
  document.getElementById("form_default").style.display = "none";
  document.getElementById("form_loading").style.display = "block";

  const frm = event.target;

  const resp = await fetch("/api-sms-gateway", {
    method: "POST",
    body: new FormData(frm),
  });

  if (!resp.ok) {
    //Reset button state
    document.getElementById("form_default").style.display = "block";
    document.getElementById("form_loading").style.display = "none";

    return;
  } else if (resp.ok) {
    const data = await resp.json();
    document.getElementById("gold_step_2").style.display = "none";
    //console.log(data);
    document.getElementById("user_phonenumber_2").value = data.user_phonenumber;
    document.getElementById("gold_step_3").style.display = "flex";
  }
}

function displayStep_2() {
  document.getElementById("gold_step_2").style.display = "flex";
  document.getElementById("gold_step_1").style.display = "none";
}

function validateNumber() {
  const regex = /^[0-9]+$/;
  input = document.querySelector('input[name="user_phonenumber"]');
  document.getElementById("user_phonenumber_error_msg").style.display = "none";
  input.classList.remove("validate_error");
  const max_val = parseInt(input.getAttribute("maxlength"));
  const min_val = parseInt(input.getAttribute("min-val"));

  if (
    !(input.value.length >= min_val && input.value.length <= max_val) ||
    !regex.test(input.value)
  ) {
    document.getElementById("user_phonenumber_error_msg").style.display =
      "block";
    input.classList.add("validate_error");
  } else {
    document.getElementById("user_phonenumber_error_msg").style.display =
      "none";
    input.classList.remove("validate_error");
  }
}

function checkSmsForm() {
  validateNumber();

  const form = event.target;
  if (!form.querySelector(".validate_error")) {
    handleSubmitSms();
  }
}

async function handleSubmitVerification() {
  //Disable btn and add loader
  const btn = event.target;
  btn.disabled = true;
  document.getElementById("form_default").style.display = "none";
  document.getElementById("form_loading").style.display = "block";

  const frm = event.target;

  const resp = await fetch("/api-verify-phone", {
    method: "POST",
    body: new FormData(frm),
  });

  if (!resp.ok) {
    //Reset button state
    document.getElementById("form_default").style.display = "block";
    document.getElementById("form_loading").style.display = "none";

    return;
  } else if (resp.ok) {
    //const data = await resp.json();
    window.location.reload();
  }
}
