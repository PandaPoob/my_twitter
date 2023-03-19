function getAge(date) {
  var today = new Date();
  var birthDate = new Date(date);
  var age = today.getFullYear() - birthDate.getFullYear();
  var m = today.getMonth() - birthDate.getMonth();
  if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
    age--;
  }
  return age;
}

function validate(callback) {
  const form = event.target;
  // const validate_error = "rgba(240, 130, 240, 0.2)"

  const validate_error = "white";
  form.querySelectorAll("[data-validate]").forEach(function (element) {
    element.classList.remove("validate_error");

    //element.style.backgroundColor = "white";

    const id = element.getAttribute("id");
    const errorMsgElement = document.getElementById(`${id}_error_msg`);
    if (errorMsgElement) {
      errorMsgElement.style.display = "none";
    }
  });
  form.querySelectorAll("[data-validate]").forEach(function (element) {
    const id = element.getAttribute("id");
    const errorMsgElement = document.getElementById(`${id}_error_msg`);
    switch (element.getAttribute("data-validate")) {
      case "str":
        //check if its empty

        if (element.value.length === 0) {
          //add error style
          element.classList.add("validate_error");
          //add error messsage
          if (errorMsgElement) {
            errorMsgElement.style.display = "block";
            errorMsgElement.innerHTML =
              element.getAttribute("error-msg-required");
          }
        } else if (
          element.value.length < parseInt(element.getAttribute("data-min")) ||
          element.value.length > parseInt(element.getAttribute("data-max"))
        ) {
          element.classList.add("validate_error");
          if (errorMsgElement) {
            errorMsgElement.style.display = "block";
            errorMsgElement.innerHTML = element.getAttribute("error-msg-len");
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
        if (element.value.length === 0) {
          //add error style
          element.classList.add("validate_error");
          //add error messsage
          if (errorMsgElement) {
            errorMsgElement.style.display = "block";
            errorMsgElement.innerHTML =
              element.getAttribute("error-msg-required");
          }
        } else if (!re.test(element.value.toLowerCase())) {
          element.classList.add("validate_error");
          console.log(errorMsgElement);
          if (errorMsgElement) {
            errorMsgElement.style.display = "block";
            errorMsgElement.innerHTML = element.getAttribute("error-msg-len");
          }
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
        if (element.value.length === 0) {
          //add error style
          element.classList.add("validate_error");
          //add error messsage
          if (errorMsgElement) {
            errorMsgElement.style.display = "block";
            errorMsgElement.innerHTML =
              element.getAttribute("error-msg-required");
          }
        } else if (
          element.value !=
          form.querySelector(
            `[name='${element.getAttribute("data-match-name")}']`
          ).value
        ) {
          element.classList.add("validate_error");
          if (errorMsgElement) {
            errorMsgElement.style.display = "block";
            errorMsgElement.innerHTML = element.getAttribute("error-msg-len");
          }
        }

        break;
      case "birthday":
        age = getAge(element.value.replaceAll("-", "/"));

        if (element.value.length === 0) {
          //add error style
          element.classList.add("validate_error");
          //add error messsage
          if (errorMsgElement) {
            errorMsgElement.style.display = "block";
            errorMsgElement.innerHTML =
              element.getAttribute("error-msg-required");
          }
        } else if (age < 13) {
          element.classList.add("validate_error");
          //add error messsage
          if (errorMsgElement) {
            errorMsgElement.style.display = "block";
            errorMsgElement.innerHTML = element.getAttribute("error-msg-len");
          }
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
