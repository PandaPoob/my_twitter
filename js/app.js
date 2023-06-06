async function follow() {
  const frm = event.target;
  const resp = await fetch("/api-follow", {
    method: "POST",
    body: new FormData(frm),
  });

  const data = await resp.json();
  if (resp.ok) {
    window.location.reload();
    return;
  }
  console.log(data);
}

async function unfollow() {
  const frm = event.target;
  const resp = await fetch("/api-unfollow", {
    method: "POST",
    body: new FormData(frm),
  });
  const data = await resp.json();
  if (resp.ok) {
    window.location.reload();
    return;
  }
  console.log(data);
}

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
  //const url = new URL(window.location.href);
  //url.searchParams.set("query", searchQuery);
  //login?error=Invalid user name
  // Replace the current URL with the updated query parameter
  //window.history.replaceState({}, "", url.toString());
}
