function showSearchResults() {
  document
    .getElementById(`search_results_container`)
    .classList.remove("hidden");
}

function hideSearchResults() {
  setTimeout(function () {
    document.getElementById(`search_results_container`).classList.add("hidden");
  }, 1000);
}

let the_timer;
function search() {
  clearTimeout(the_timer);
  the_timer = setTimeout(async function () {
    const frm = document.querySelector("#search_form");
    const input = document.querySelector('input[name="search_query"]').value;

    const link = document.getElementById("search_link");
    const help = document.getElementById(`search_help`);
    const container = document.getElementById("search_results");

    //Set the link
    if (input.length != 0) {
      link.querySelector("span").innerHTML = input;
      link.href = `/search?query=${input}`;
      link.style.display = "flex";
      help.style.display = "none";

      const res = await fetch("/api-search", {
        method: "POST",
        body: new FormData(frm),
      });
      const data = await res.json();

      if (res.ok && data.results.length >= 1) {
        container.innerHTML = "";
        let articles = "";

        function getIcon(status) {
          if (status == "blue") {
            return `<svg
                width="18"
                height="18"
                viewBox="0 0 24 24"
                class="text-twitterblue"
              >
                <path
                  fill="currentColor"
                  d="m8.6 22.5l-1.9-3.2l-3.6-.8l.35-3.7L1 12l2.45-2.8l-.35-3.7l3.6-.8l1.9-3.2L12 2.95l3.4-1.45l1.9 3.2l3.6.8l-.35 3.7L23 12l-2.45 2.8l.35 3.7l-3.6.8l-1.9 3.2l-3.4-1.45Zm2.35-6.95L16.6 9.9l-1.4-1.45l-4.25 4.25l-2.15-2.1L7.4 12Z"
                />
              </svg>`;
          } else {
            return "";
          }
        }

        //Populate array HTML
        data.results.forEach((result) => {
          articles += `<li>
        <a
          href="/${result.user_name}"
          style="padding-inline: 20px;"
          class="flex items-center gap-4 py-4 hover:bg-white hover:bg-opacity-10"
        >
          <img
            style="max-width: 56px;"
            class="rounded-full"
            src="/images/avatar_imgs/${result.user_img_avatar}"
            alt=""
          />
          <span class="flex flex-col">
            <span class="flex items-center gap-1">
              <span class="font-bold max-w-[80%] text-ellipsis whitespace-nowrap overflow-hidden break-words">
              ${result.user_full_name}</span>
              ${getIcon(result.user_twitter_status)}
          
            </span>
            <span class="text-twittergray-500 text-base">@${
              result.user_name
            }</span>
          </span>
        </a>
      </li>`;
        });

        container.insertAdjacentHTML("afterbegin", articles);
      }
    } else if (input.length == 0) {
      help.style.display = "block";
      link.style.display = "none";
      container.innerHTML = "";
    }
  }, 500);
}

function handleSearch() {
  const searchQuery = document.querySelector(
    'input[name="search_query"]'
  ).value;
  if (searchQuery) {
    window.location.href = `/search?query=${searchQuery}`;
  }
}

//Get component for twitter status
function getAccountStatus(user_twitter_status) {
  switch (user_twitter_status) {
    case "basic":
      return "";
    case "blue":
      return `<svg
              width="18"
              height="18"
              viewBox="0 0 24 24"
              class="text-twitterblue"
            >
              <path
                fill="currentColor"
                d="m8.6 22.5l-1.9-3.2l-3.6-.8l.35-3.7L1 12l2.45-2.8l-.35-3.7l3.6-.8l1.9-3.2L12 2.95l3.4-1.45l1.9 3.2l3.6.8l-.35 3.7L23 12l-2.45 2.8l.35 3.7l-3.6.8l-1.9 3.2l-3.4-1.45Zm2.35-6.95L16.6 9.9l-1.4-1.45l-4.25 4.25l-2.15-2.1L7.4 12Z"
              />
            </svg>`;
    case "gold":
      return `<svg
              width="18"
              height="18"
              viewBox="0 0 24 24"
              class="text-twittergold"
            >
              <path
                fill="currentColor"
                d="m8.6 22.5l-1.9-3.2l-3.6-.8l.35-3.7L1 12l2.45-2.8l-.35-3.7l3.6-.8l1.9-3.2L12 2.95l3.4-1.45l1.9 3.2l3.6.8l-.35 3.7L23 12l-2.45 2.8l.35 3.7l-3.6.8l-1.9 3.2l-3.4-1.45Zm2.35-6.95L16.6 9.9l-1.4-1.45l-4.25 4.25l-2.15-2.1L7.4 12Z"
              />
            </svg>`;
  }
}
//Get component for tweet text
function getTextContent(tweet_text) {
  if (tweet_text) {
    return `<p class="text-base mt-1 mb-2">${tweet_text}</p>`;
  } else {
    return ``;
  }
}

//Get component for tweet images
function getImageLayoutPag(image_amount, images) {
  if (image_amount == 0) {
    return ``;
  } else {
    switch (image_amount) {
      case 1:
        return `<div class="mt-4">
            <img
              class="rounded-xl w-full h-full object-cover"
              alt="tweet image"
              src="/images/tweet_imgs/${images[0].tweet_image_url}"
            />
          </div>`;
      case 2:
        return `<div class="mt-4 flex gap-0.5">
            <img
              class="rounded-xl w-full h-full object-cover"
              alt="tweet image 1"
              src="/images/tweet_imgs/${images[0].tweet_image_url}"
            />
            <img
              class="rounded-xl w-full h-full object-cover"
              alt="tweet image 2"
              src="/images/tweet_imgs/${images[1].tweet_image_url}"
            />
          </div>`;
      case 3:
        return `<div class="mt-4 grid grid-cols-2 grid-rows-2 gap-0.5 [&>*:nth-child(1)]:row-span-2">
            <img
              class="rounded-xl w-full h-full object-cover"
              alt="tweet image 1"
              src="/images/tweet_imgs/${images[0].tweet_image_url}"
            />
            <img
              class="rounded-xl w-full h-full object-cover"
              alt="tweet image 2"
              src="/images/tweet_imgs/${images[1].tweet_image_url}"
            />
            <img
              class="rounded-xl w-full h-full object-cover"
              alt="tweet image 3"
              src="/images/tweet_imgs/${images[2].tweet_image_url}"
            />
          </div>`;
      case 4:
        return `<div class="mt-4 grid grid-cols-2 grid-rows-2 gap-0.5">
            <img
              class="rounded-xl w-full h-full object-cover"
              alt="tweet image 1"
              src="/images/tweet_imgs/${images[0].tweet_image_url}"
            />
            <img
              class="rounded-xl w-full h-full object-cover"
              alt="tweet image 2"
              src="/images/tweet_imgs/${images[1].tweet_image_url}"
            />
            <img
              class="rounded-xl w-full h-full object-cover"
              alt="tweet image 3"
              src="/images/tweet_imgs/${images[2].tweet_image_url}"
            />
              <img
              class="rounded-xl w-full h-full object-cover"
              alt="tweet image 4"
              src="/images/tweet_imgs/${images[3].tweet_image_url}"
            />
          </div>`;
    }
  }
}
