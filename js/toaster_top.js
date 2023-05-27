function displayToasterTop(text) {
  document.getElementById("toast_error_msg_signup").style.display = "flex";
  document.getElementById("toast_error_text").innerHTML = text;
  setTimeout(function () {
    document.getElementById("toast_error_msg_signup").style.display = "none";
    document.getElementById("toast_error_text").innerHTML = "";
  }, 6000);
}
