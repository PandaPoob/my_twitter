const edit_profile_modal = document.getElementById("modal_bg");

function openEditModal() {
  //display modal
  edit_profile_modal.style.display = "flex";

  //Set input fields length
  document.querySelectorAll(".val_no").forEach(function (element) {
    input_parent_name = element.getAttribute("for");
    parent = document.getElementById(input_parent_name);
    element.innerHTML = parent.value.length;
  });
}

function handleImgCover() {
  //validate type
  const coverInput = document.getElementById("user_img_cover");
  const cover = coverInput.files[0];

  const max_img_size = parseInt(coverInput.getAttribute("data-max-img"));

  validateImage(cover, max_img_size, (isCover = true));
}

function displayCoverImg(cover) {
  //display here
  document.getElementById("current_cover_img").style.filter = "brightness(0%)";

  const previewImage = document.getElementById("preview_cover");

  const image = `
          <img
              src="${URL.createObjectURL(cover)}" 
              alt="Preview Image"
             class="absolute top-0 left-0 w-full h-full object-cover z-[101]"/>
           `;
  previewImage.innerHTML = "";
  previewImage.insertAdjacentHTML("afterbegin", image);
}

function handleImgAvatar() {
  //validate type
  const avatarInput = document.getElementById("user_img_avatar");
  const avatar = avatarInput.files[0];

  const max_img_size = parseInt(avatarInput.getAttribute("data-max-img"));

  validateImage(avatar, max_img_size);
}

function displayAvatarImg(avatar) {
  //display here
  document.getElementById("current_avatar_img").style.filter = "brightness(0%)";

  const previewImage = document.getElementById("preview_avatar");

  const image = `
          <img
              src="${URL.createObjectURL(avatar)}" 
              alt="Preview Image"
             class="absolute top-0 left-0 w-full h-full object-cover z-[101] rounded-full p-0.5 bg-black"/>
           `;
  previewImage.innerHTML = "";
  previewImage.insertAdjacentHTML("afterbegin", image);
}

function validateImage(img, max, isCover) {
  if (img.size > max) {
    displayNotifToaster("Image exceed the size limit of 2MB");
  } else {
    validateImageMagicType(img)
      .then((imageType) => {
        if (!imageType.includes("jpeg") && !imageType.includes("png")) {
          displayNotifToaster("The image is not the accepted filetype");
        } else {
          //Show images if all validation passes
          if (isCover) {
            displayCoverImg(img);
          } else {
            displayAvatarImg(img);
          }
        }
      })
      .catch((error) => {
        //If api fails return error message as notification
        displayNotifToaster(error.message);
      });
  }
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
    console.log(data, resp);
    document.getElementById("form_default").style.display = "block";
    document.getElementById("form_loading").style.display = "none";

    return;
  } else if (resp.ok) {
    edit_profile_modal.style.display = "none";
    window.location.reload();
  }
}
