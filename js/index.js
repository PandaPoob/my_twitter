let page = 1;
let moreTweets = true;

window.addEventListener("scroll", handlePagnation);

function handlePagnation() {
  // Check if the user has scrolled to the bottom of the page
  if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
    // Increment the page number and load the next set of tweets
    page++;
    fetchTweets();
  }
}

async function fetchTweets() {
  if (moreTweets) {
    try {
      const res = await fetch(`/api-pagination-tweets?page=${page}`);
      const data = await res.json();

      displayTweets(data.tweets);

      //If the number of returned tweets is less than 10
      if (data.tweets.length < 10) {
        //No more tweets to fetch
        moreTweets = false;
        //console.log("All tweets fetched");
      } else {
        //Increment page number for the next request
        page++;
      }
    } catch (error) {
      //An error occurred
      console.log("Error fetching tweets:", error);
    }
  }
}

function displayTweets(tweets) {
  let newTweets = "";

  tweets.forEach((tweet) => {
    let icon = getAccountStatus(tweet.user_twitter_status);
    let text = getTextContent(tweet.tweet_field_text);
    let imageGrid = getImageLayoutPag(
      tweet.tweet_field_images,
      tweet.tweet_images
    );

    newTweets += `<div
    class="relative w-full height-auto flex pt-3 px-4 bg-black border-b border-zinc-700 hover:bg-white hover:bg-opacity-[3%]">
    <a href="/${tweet.user_name}/status/${tweet.tweet_slug}"
      class="absolute top-0 left-0 right-0 bottom-0"
    > </a>
      <!-- left -->
      <div class="pl-4" style="padding-right: 1rem">
        <a href="/${tweet.user_name}" class="relative z-20">
          <img
            src="/images/avatar_imgs/${tweet.user_img_avatar}"
            alt="${tweet.user_name} profile image"
            class="relative rounded-full w-14 z-0"
          />
        </a>
      </div>
      <!-- right -->
      <div class="w-full flex flex-col pr-4">

        <!-- user -->
        <div class="relative flex items-center text-base mr-auto">
          <a
            href="/${tweet.user_name}"
            class="flex items-center gap-0.5 font-bold group"
          >
            <span class="group-hover:underline"
              >${tweet.user_full_name}</span
            >
            ${icon}
            <span class="text-zinc-500 font-normal">
              @${tweet.user_name}</span
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

          <a href="/${tweet.user_name}/status/${tweet.tweet_slug}" class="text-zinc-500 hover:underline">Now</a>
          
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
            <span>${tweet.tweet_total_replies}</span>
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
           <span>${tweet.tweet_total_retweets}</span>
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
              <span>${tweet.tweet_total_likes}</span>
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
  });

  document.querySelector("#tweets").insertAdjacentHTML("beforeend", newTweets);
}
