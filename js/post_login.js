function displayTip() {
  /*   const tip_id = Math.random();
  let tip = `
    <div data-tip-id="${tip_id}" class="flex justify-center w-full lg:w-1/3 mx-auto py-4 text-white bg-purple-500 rounded-md">
      Invalid credentials. Try again
    </div>
    `; */
  document.getElementById("toast_error_msg").style.display = "flex";

  setTimeout(function () {
    document.getElementById("toast_error_msg").style.display = "none";
    //document.querySelector(`[data-tip-id='${tip_id}']`).remove();
  }, 4000);
}

async function handleSubmitLogin() {
  const btn = event.target;
  btn.disabled = true;

  document.getElementById("form_default").style.display = "none";
  document.getElementById("form_loading").style.display = "block";

  const frm = event.target;

  const resp = await fetch("/api-login", {
    method: "POST",
    body: new FormData(frm),
  });
  btn.disabled = false;

  document.getElementById("form_default").style.display = "block";
  document.getElementById("form_loading").style.display = "none";

  if (!resp.ok) {
    console.log("Cannot login");
    displayTip();
    return;
  }
  const data = await resp.json();
  // Success go to home page
  location.href = "/";
}
