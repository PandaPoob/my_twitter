function displayTip(data) {
  document.getElementById("toast_error_msg_signup").style.display = "flex";
  document.getElementById("toast_error_text").innerHTML = data.info;
  setTimeout(function () {
    document.getElementById("toast_error_msg_signup").style.display = "none";
    //document.querySelector(`[data-tip-id='${tip_id}']`).remove();
  }, 4000);
}

async function handleSubmitSignup() {
  const btn = event.target;
  btn.disabled = true;

  //document.getElementById("form_default").style.display = "none";
  //document.getElementById("form_loading").style.display = "block";

  const frm = event.target;

  const resp = await fetch("/api-signup", {
    method: "POST",
    body: new FormData(frm),
  });
  btn.disabled = false;

  //document.getElementById("form_default").style.display = "block";
  //document.getElementById("form_loading").style.display = "none";

  if (!resp.ok) {
    console.log("Cannot signup");
    const data = await resp.json();
    displayTip(data);
    return;
  }
  const data = await resp.json();

  // Success go to profile page
  location.href = `/${data.user_name}`;
}
