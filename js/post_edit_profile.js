const edit_profile_modal = document.getElementById("modal_bg");

function openEditModal() {
  //display modal
  edit_profile_modal.style.display = "block";

  //set all input fields length
  document.querySelectorAll(".val_no").forEach(function (element) {
    input_parent_name = element.getAttribute("for");
    parent = document.getElementById(input_parent_name);
    element.innerHTML = parent.value.length;
  });
}

function validateBio() {
  const input = document.querySelector('textarea[name="user_bio_text"]');
  const display = document.getElementById("counter_user_bio_text");
  counter(display, input);
}

function validateLocation() {
  const input = document.querySelector('input[name="user_bio_location"]');
  const display = document.getElementById("counter_user_bio_location");
  counter(display, input);
}

function countLink() {
  const input = document.querySelector('input[name="user_bio_link"]');
  const display = document.getElementById("counter_user_bio_link");
  counter(display, input);
}

function counter(display, input) {
  display.innerHTML = input.value.length;
}

function validateLink() {
  const input = document.querySelector('input[name="user_bio_link"]');

  //Check regex
  const regex = /^(http|https):\/\/[^\s/$.?#].[^\s]*$/;
  const error_display = document.getElementById("user_bio_link_error_msg");
  if (!regex.test(input.value) && input.value.length !== 0) {
    //display error
    error_display.style.display = "block";
    input.classList.add("validate_error");
  } else {
    error_display.style.display = "none";
    input.classList.remove("validate_error");
  }
}

function checkEditForm() {
  validateLink();
  const form = event.target;
  if (!form.querySelector(".validate_error")) {
    handleSubmitEditProfile();
  }
}

async function handleSubmitEditProfile() {
  //Disable btn and add loader
  const btn = event.target;
  btn.disabled = true;
  document.getElementById("form_default").style.display = "none";
  document.getElementById("form_loading").style.display = "block";

  const frm = event.target;

  const resp = await fetch("/api-edit-profile", {
    method: "POST",
    body: new FormData(frm),
  });

  if (!resp.ok) {
    const data = await resp.json();
    //Reset button state
    document.getElementById("form_default").style.display = "block";
    document.getElementById("form_loading").style.display = "none";

    //Show toaster

    return;
  } else if (resp.ok) {
    edit_profile_modal.style.display = "none";
    location.reload();
  }
}
