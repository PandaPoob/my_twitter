let storedTweetImages = [];
let circumference = "";
const circle = document.getElementById("progress_circle");

window.onload = () => {
  //Set progress on circle val
  const radius = circle.r.baseVal.value;
  circumference = radius * 2 * Math.PI;
  circle.style.strokeDasharray = `${circumference} ${circumference}`;
  circle.style.strokeDashoffset = circumference;
};

function validateTextTweetInput() {
  const tweet = document.getElementById("tweet_field_text");
  const tweet_text = tweet.value;
  const max_length = parseInt(tweet.getAttribute("data-max"));

  //Text component validation
  circle.style.stroke = "#1d9bf0";
  if (tweet_text.length > max_length) {
    circle.style.stroke = "#f4212e";
    //set to red stop function
  } else {
    const percentage = (tweet_text.length / max_length) * 100;
    setProgress(percentage);
  }

  const tweet_btn = document.getElementById("submit_tweet_btn");
  //If text is bigger than max disable
  if (tweet_text.length > max_length) {
    tweet_btn.disabled = true;
    //If there is text enabled
  } else if (tweet_text.trim().length !== 0) {
    tweet_btn.disabled = false;
    //If there is not text or images disabled
  } else if (tweet_text.trim().length == 0 && storedTweetImages.length == 0) {
    tweet_btn.disabled = true;
  }

  //Get characters left and insert
  const char_left = max_length - tweet_text.length;
  const number_text = document.getElementById("max_length_number");

  number_text.innerHTML = char_left;
}

function setProgress(percent) {
  const offset = circumference - (percent / 100) * circumference;
  circle.style.strokeDashoffset = offset;
}

function handleTweetImages() {
  //Empty and reset array
  storedTweetImages = [];

  //Get image input
  const imageInput = document.getElementById("tweet_field_image");
  //Array to store current images

  //Get files
  const files = imageInput.files;

  //Store in array
  for (let i = 0; i < files.length; i++) {
    storedTweetImages.push(files[i]);
  }

  const max_imgs = parseInt(imageInput.getAttribute("data-max-imgs"));
  const max_img_size = parseInt(imageInput.getAttribute("data-max-img"));

  //VALIDATION//
  //Maximum of 4 images
  if (storedTweetImages.length > max_imgs) {
    displayNotifToaster("Please choose up to 4 images", (clear = true));
  } else {
    fullValidation();
  }
  function fullValidation() {
    storedTweetImages.forEach((img) => {
      //Size
      if (img.size > max_img_size) {
        displayNotifToaster(
          "One or more images exceed the size limit of 5MB",
          (clear = true)
        );
      }
      //Type
      else {
        validateImageMagicType(img)
          .then((imageType) => {
            if (!imageType.includes("jpeg") && !imageType.includes("png")) {
              displayNotifToaster(
                "One or more images are not the accepted filetype",
                (clear = true)
              );
            } else {
              //Show images if all validation passes
              prepareOutput();
            }
          })
          .catch((error) => {
            //If api fails return error message as notification
            displayNotifToaster(error.message, (clear = true));
          });
      }
    });
  }
}

function prepareOutput() {
  tweet_text = document.getElementById("tweet_field_text").value;
  const max_length = parseInt(
    document.getElementById("tweet_field_text").getAttribute("data-max")
  );

  if (
    (storedTweetImages.length == 0 && tweet_text.trim().length == 0) ||
    tweet_text.length > max_length
  ) {
    document.getElementById("submit_tweet_btn").disabled = true;
  } else if (storedTweetImages.length !== 0) {
    document.getElementById("submit_tweet_btn").disabled = false;
  }
  //HTML array
  let images = "";

  //Populate array HTML
  storedTweetImages.forEach((image, index) => {
    if (storedTweetImages.length == 3 && index == 0) {
      images += `<div class="relative" style="grid-row:1/3;">
            <img 
              src="${URL.createObjectURL(image)}" 
              alt="image" 
              class="relative rounded-xl w-full h-full object-cover"/>
              <button type="button" style="background-color:rgba(0, 0, 0, 0.8); left: 0.25rem;" class="absolute top-0 mt-1 w-6 h-6 rounded-full flex justify-center items-center text-white hover:bg-opacity-50" onclick="removeImage(${index})">
                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24"><path fill="currentColor" d="M19 6.41L17.59 5L12 10.59L6.41 5L5 6.41L10.59 12L5 17.59L6.41 19L12 13.41L17.59 19L19 17.59L13.41 12L19 6.41Z"/></svg>
              </button>
          </div>`;
    } else {
      images += `<div class="relative">
            <img 
              src="${URL.createObjectURL(image)}" 
              alt="image" 
              class="relative rounded-xl w-full h-full object-cover"/>
              <button type="button" style="background-color:rgba(0, 0, 0, 0.5); left: 0.25rem;" class="absolute top-0 mt-1 w-6 h-6 rounded-full flex justify-center items-center text-white hover:bg-opacity-50" onclick="removeImage(${index})">
                <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24"><path fill="currentColor" d="M19 6.41L17.59 5L12 10.59L6.41 5L5 6.41L10.59 12L5 17.59L6.41 19L12 13.41L17.59 19L19 17.59L13.41 12L19 6.41Z"/></svg>
              </button>
          </div>`;
    }
  });
  displayOutputImages(images);
}

function removeImage(index) {
  storedTweetImages.splice(index, 1);
  prepareOutput();
}

function displayOutputImages(images) {
  const output = document.querySelector("output");

  //Clear layout on output
  output.className = "";

  //Set style on image amount
  if (storedTweetImages.length == 2) {
    output.classList.add("output_images_2");
  } else if (storedTweetImages.length >= 3) {
    output.classList.add("output_images");
  }

  //Push images into output
  output.innerHTML = images;
}

async function handleSubmitTweet() {
  const frm = event.target;

  const resp = await fetch("/tweet", {
    method: "POST",
    body: new FormData(frm),
  });

  if (!resp.ok) {
    const data = await resp.json();
    console.log(data.info);
    return;
  } else {
    const data = await resp.json();
    frm.reset();
    document.querySelector("output").innerHTML = "";
    document.querySelector("output").className = "";
    document.getElementById("submit_tweet_btn").disabled = true;
    renderTweet(data);
  }
}

function renderTweet(data) {
  const { image_amount, tweet, images, author } = data.content;

  //Conditional components that make up tweet
  let icon = getAccountStatus(author.twitter_status);
  let text = getTextContent(tweet.tweet_field_text);
  let imageGrid = getImageLayout(image_amount, images);

  //Tweet template
  const template = `<div
    class="relative w-full height-auto flex pt-3 px-4 bg-black border-b border-zinc-700 hover:bg-white hover:bg-opacity-[3%]">
    <a href="/${author.user_name}/status/${tweet.tweet_slug}"
      class="absolute top-0 left-0 right-0 bottom-0"
    > </a>
      <!-- left -->
      <div class="pl-4" style="padding-right: 1rem">
        <a href="/${author.user_name}" class="relative z-20">
          <img
            src="/images/avatar_imgs/${author.img_avatar}"
            alt="${author.user_name} profile image"
            class="relative rounded-full w-14 z-0"
          />
        </a>
      </div>
      <!-- right -->
      <div class="w-full flex flex-col pr-4">

        <!-- user -->
        <div class="relative flex items-center text-base mr-auto">
          <a
            href="/${author.user_name}"
            class="flex items-center gap-0.5 font-bold group"
          >
            <span class="group-hover:underline"
              >${author.full_name}</span
            >
            ${icon}
            <span class="text-zinc-500 font-normal">
              @${author.user_name}</span
            >
          </a>

          <svg
            class="mt-1 text-zinc-500"
            xmlns="http://www.w3.org/2000/svg"
            width="12"
            height="12"
            viewBox="0 0 24 24"
          >
          <path fill="currentColor" d="M12 14a2 2 0 1 1 0-4a2 2 0 0 1 0 4Z" />
          </svg>

          <a href="/${author.user_name}/status/${tweet.tweet_slug}" class="text-zinc-500 hover:underline">Now</a>
          
        </div>
                 <button
            style="cursor:default;"
            class="absolute top-1.5 right-2 rounded-full p-1.5 z-30 group hover:bg-opacity-10 hover:bg-twitterblue"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="w-5 h-5 stroke-zinc-500 group-hover:stroke-twitterblue"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M6.75 12a.75.75 0 11-1.5 0 .75.75 0 011.5 0zM12.75 12a.75.75 0 11-1.5 0 .75.75 0 011.5 0zM18.75 12a.75.75 0 11-1.5 0 .75.75 0 011.5 0z"
              />
            </svg>
          </button>

        <!-- tweet content -->
        <div>
          <!-- tweet text display-->
          ${text}
          <!-- tweet image display-->
          ${imageGrid}
    
        </div>
        <!-- tweet icons -->
        <div
          class="flex justify-between sm:gap-6 sm:justify-start lg:gap-8 text-zinc-500 text-sm py-1.5 -ml-2"
        >
          <button style="cursor:default;" class="relative z-20 group flex items-center gap-1 hover:text-twitterblue">
            <div
              class="rounded-full p-2 group-hover:bg-twitterblue group-hover:bg-opacity-10"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="18"
                height="18"
                viewBox="0 0 24 24"
              >
                <path
                  fill="currentColor"
                  d="M12 2A10 10 0 0 0 2 12a9.89 9.89 0 0 0 2.26 6.33l-2 2a1 1 0 0 0-.21 1.09A1 1 0 0 0 3 22h9a10 10 0 0 0 0-20Zm0 18H5.41l.93-.93a1 1 0 0 0 0-1.41A8 8 0 1 1 12 20Z"
                />
              </svg>
            </div>
          </button>

          <button style="cursor:default;" class="relative z-20 group flex items-center gap-1 hover:text-green-500">
            <div
              class="rounded-full p-2 group-hover:bg-green-500 group-hover:bg-opacity-10"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="18"
                height="18"
                viewBox="0 0 1024 1024"
              >
                <path
                  fill="currentColor"
                  d="M136 552h63.6c4.4 0 8-3.6 8-8V288.7h528.6v72.6c0 1.9.6 3.7 1.8 5.2a8.3 8.3 0 0 0 11.7 1.4L893 255.4c4.3-5 3.6-10.3 0-13.2L749.7 129.8a8.22 8.22 0 0 0-5.2-1.8c-4.6 0-8.4 3.8-8.4 8.4V209H199.7c-39.5 0-71.7 32.2-71.7 71.8V544c0 4.4 3.6 8 8 8zm752-80h-63.6c-4.4 0-8 3.6-8 8v255.3H287.8v-72.6c0-1.9-.6-3.7-1.8-5.2a8.3 8.3 0 0 0-11.7-1.4L131 768.6c-4.3 5-3.6 10.3 0 13.2l143.3 112.4c1.5 1.2 3.3 1.8 5.2 1.8c4.6 0 8.4-3.8 8.4-8.4V815h536.6c39.5 0 71.7-32.2 71.7-71.8V480c-.2-4.4-3.8-8-8.2-8z"
                />
              </svg>
            </div>
        
          </button>

          <button style="cursor:default;" class="relative z-20 group flex items-center gap-1 hover:text-pink-500">
            <div
              class="rounded-full p-2 group-hover:bg-pink-500 group-hover:bg-opacity-10"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke-width="1.5"
                stroke="currentColor"
                class="w-5 h-5"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z"
                />
              </svg>
            </div>
           
          </button>

          <button
            style="cursor:default;"
            class="relative z-20 group hidden lg:flex items-center gap-1 hover:text-twitterblue"
          >
            <div
              class="rounded-full p-2 group-hover:bg-twitterblue group-hover:bg-opacity-10"
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="18"
                height="18"
                viewBox="0 0 24 24"
              >
                <path
                  fill="currentColor"
                  d="M3 22V8h4v14H3m7 0V2h4v20h-4m7 0v-8h4v8h-4Z"
                />
              </svg>
            </div>
      
          </button>

          <button
            style="cursor:default;"
            class="relative z-20 rounded-full p-2 hover:text-twitterblue hover:bg-twitterblue hover:bg-opacity-10"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="18"
              height="18"
              viewBox="0 0 256 256"
            >
              <path
                fill="currentColor"
                d="M80.3 87.6a8 8 0 0 1 0-11.3l42-42a8.1 8.1 0 0 1 11.4 0l42 42a8 8 0 0 1 0 11.3a8 8 0 0 1-11.4 0L136 59.3V152a8 8 0 0 1-16 0V59.3L91.7 87.6a8 8 0 0 1-11.4 0ZM216 144a8 8 0 0 0-8 8v56H48v-56a8 8 0 0 0-16 0v56a16 16 0 0 0 16 16h160a16 16 0 0 0 16-16v-56a8 8 0 0 0-8-8Z"
              />
            </svg>
          </button>
        </div>
      </div>
   
  </div>`;

  document.querySelector("#tweets").insertAdjacentHTML("afterbegin", template);
}

//Get component for tweet images
function getImageLayout(image_amount, images) {
  if (image_amount == 0) {
    return ``;
  } else {
    switch (image_amount) {
      case 1:
        return `<div class="mt-4">
            <img
              class="rounded-xl w-full h-full object-cover"
              alt="tweet image"
              src="/images/tweet_imgs/${images[0]}"
            />
          </div>`;
      case 2:
        return `<div class="mt-4 grid grid-cols-2 gap-0.5">
            <img
              class="rounded-xl w-full h-full object-cover"
              alt="tweet image 1"
              src="/images/tweet_imgs/${images[0]}"
            />
            <img
              class="rounded-xl w-full h-full object-cover"
              alt="tweet image 2"
              src="/images/tweet_imgs/${images[1]}"
            />
          </div>`;
      case 3:
        return `<div class="mt-4 grid grid-cols-2 grid-rows-2 gap-0.5 [&>*:nth-child(1)]:row-span-2">
            <img
              class="rounded-xl w-full h-full object-cover"
              alt="tweet image 1"
              src="/images/tweet_imgs/${images[0]}"
            />
            <img
              class="rounded-xl w-full h-full object-cover"
              alt="tweet image 2"
              src="/images/tweet_imgs/${images[1]}"
            />
            <img
              class="rounded-xl w-full h-full object-cover"
              alt="tweet image 3"
              src="/images/tweet_imgs/${images[2]}"
            />
          </div>`;
      case 4:
        return `<div class="mt-4 grid grid-cols-2 grid-rows-2 gap-0.5 aspect-square">
            <img
              class="rounded-xl w-full h-full object-cover max-h-52"
              alt="tweet image 1"
              src="/images/tweet_imgs/${images[0]}"
            />
            <img
              class="rounded-xl w-full h-full object-cover max-h-52"
              alt="tweet image 2"
              src="/images/tweet_imgs/${images[1]}"
            />
            <img
              class="rounded-xl w-full h-full object-cover max-h-52"
              alt="tweet image 3"
              src="/images/tweet_imgs/${images[2]}"
            />
              <img
              class="rounded-xl w-full h-full object-cover max-h-52"
              alt="tweet image 4"
              src="/images/tweet_imgs/${images[3]}"
            />
          </div>`;
    }
  }
}
