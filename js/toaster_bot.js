let notifTimer;
function displayNotifToaster(errorMsg, clear) {
  //Get elements in html

  const container = document.getElementById("notif_container");
  const content = container.querySelector("p");

  //Reset image display
  if (clear) {
    const output = document.querySelector("output");
    output.className = "";
    output.innerHTML = "";
  }

  //Reset notification
  if (notifTimer) {
    clearTimeout(notifTimer);
    container.style.display = "none";
    content.innerHTML = "";
  }
  //Display
  container.style.display = "flex";
  content.innerHTML = errorMsg;

  notifTimer = setTimeout(function () {
    container.style.display = "none";
    content.innerHTML = errorMsg;
  }, 5000);
}
