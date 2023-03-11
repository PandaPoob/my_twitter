function validate(callback) {
  const form = event.target;
  // const validate_error = "rgba(240, 130, 240, 0.2)"

  const validate_error = "white";
  form.querySelectorAll("[data-validate]").forEach(function (element) {
    element.classList.remove("validate_error");

    element.style.backgroundColor = "white";
    const id = element.getAttribute("id");
    document.getElementById(`${id}_error_msg`).style.display = "none";
  });
  form.querySelectorAll("[data-validate]").forEach(function (element) {
    switch (element.getAttribute("data-validate")) {
      case "str":
        const id = element.getAttribute("id");
        const errorMsgElement = document.getElementById(`${id}_error_msg`);
        //check if its empty
        if (element.value.length === 0) {
          //add error style
          element.classList.add("validate_error");
          //add error messsage
          errorMsgElement.style.display = "block";
          errorMsgElement.innerHTML =
            element.getAttribute("error-msg-required");

          //remove backend error
          const backendval = document.getElementById(`${id}_backend_error_msg`);
          if (backendval) {
            backendval.style.display = "none";
            backendval.innerHTML = "";
          }
        } else if (
          element.value.length < parseInt(element.getAttribute("data-min")) ||
          element.value.length > parseInt(element.getAttribute("data-max"))
        ) {
          element.classList.add("validate_error");

          errorMsgElement.style.display = "block";
          errorMsgElement.innerHTML = element.getAttribute("error-msg-len");

          //remove backend error
          const backendval = document.getElementById(`${id}_backend_error_msg`);
          if (backendval) {
            backendval.style.display = "none";
            backendval.innerHTML = "";
          }
        }
        break;
      case "int":
        if (
          !/^\d+$/.test(element.value) ||
          parseInt(element.value) <
            parseInt(element.getAttribute("data-min")) ||
          parseInt(element.value) > parseInt(element.getAttribute("data-max"))
        ) {
          element.classList.add("validate_error");
          element.style.backgroundColor = validate_error;
        }
        break;
      case "email":
        let re =
          /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        if (!re.test(element.value.toLowerCase())) {
          element.classList.add("validate_error");
          element.style.backgroundColor = validate_error;
        }
        break;
      case "regex":
        var regex = new RegExp(element.getAttribute("data-regex"));
        // var regex = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/
        if (!regex.test(element.value)) {
          console.log(element.value);
          console.log("regex error");
          element.classList.add("validate_error");
          element.style.backgroundColor = validate_error;
        }
        break;
      case "match":
        if (
          element.value !=
          form.querySelector(
            `[name='${element.getAttribute("data-match-name")}']`
          ).value
        ) {
          element.classList.add("validate_error");
          element.style.backgroundColor = validate_error;
        }
        break;
    }
  });
  if (!form.querySelector(".validate_error")) {
    callback();

    return;
  }
  form.querySelector(".validate_error").focus();
}

// ##############################
function clear_validate_error() {
  // event.target.classList.remove("validate_error")
  // event.target.value = ""
}
