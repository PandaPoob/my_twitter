const step_1 = document.getElementById("delete_step_1");
const step_2 = document.getElementById("delete_step_2");
const step_3 = document.getElementById("delete_step_3");

function displayDelete_2() {
  step_1.style.display = "none";
  step_2.style.display = "block";
}

function displayDelete_3() {
  step_2.style.display = "none";
  step_3.style.display = "block";
}

function checkDeleteForm() {
  validatePassword();

  const form = event.target;
  if (!form.querySelector(".validate_error")) {
    handleSubmitDelete();
  }
}

async function handleSubmitDelete() {
  const btn = event.target;
  btn.disabled = true;
  document.getElementById("form_default").style.display = "none";
  document.getElementById("form_loading").style.display = "block";

  const frm = event.target;

  const resp = await fetch("/api-delete-user", {
    method: "POST",
    body: new FormData(frm),
  });

  if (!resp.ok) {
    //Reset button state
    const data = await resp.json();
    document.getElementById("form_default").style.display = "block";
    document.getElementById("form_loading").style.display = "none";
    displayToasterTop(data.info);
    return;
  } else if (resp.ok) {
    //const data = await resp.json();
    window.location.reload();
  }
}
