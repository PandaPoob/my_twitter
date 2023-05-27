async function handleSubmitLogin() {
  //Disable btn and add loader
  const btn = event.target;
  btn.disabled = true;

  document.getElementById("form_default").style.display = "none";
  document.getElementById("form_loading").style.display = "block";

  const frm = event.target;

  const resp = await fetch("/api-login", {
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
    //Reset button state
    btn.disabled = false;

    document.getElementById("form_default").style.display = "block";
    document.getElementById("form_loading").style.display = "none";
    // Success go to home page
    location.href = "/";
  }
}

function checkForm() {
  validateUserName();
  validatePassword();

  const form = event.target;
  if (!form.querySelector(".validate_error")) {
    handleSubmitLogin();
  }
}
