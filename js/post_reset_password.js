async function handleResetPassword() {
  //Disable btn and add loader
  const btn = event.target;
  btn.disabled = true;
  document.getElementById("form_default").style.display = "none";
  document.getElementById("form_loading").style.display = "block";

  const frm = event.target;
  const resp = await fetch("/api-reset-password", {
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
    //Succesful reset
    document.getElementById(`password_reset_container`).style.display = "none";
    document.getElementById(`heading`).style.display = "none";
    document.getElementById(`password_success_container`).style.display =
      "block";
    const body = document.querySelector("body");
    body.style.flexDirection = "column";
    body.style.alignItems = "center";
    body.style.justifyContent = "flex-start";
  }
}
function checkResetPwForm() {
  validatePassword();
  confirmPassword();
  const form = event.target;
  if (!form.querySelector(".validate_error")) {
    handleResetPassword();
  }
}
