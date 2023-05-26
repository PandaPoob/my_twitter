async function follow() {
  //alert("Form submitted");

  const frm = event.target;
  const resp = await fetch("/api-follow", {
    method: "POST",
    body: new FormData(frm),
  });

  const data = await resp.json();
  if (resp.ok) {
    console.log(data);
    document.getElementById(`profile_follow_form`).style.display = "none";
    document.getElementById(`profile_unfollow_form`).style.display = "block";
    document.getElementById(`profile_followers_number`).innerHTML =
      data.follower_count;

    return;
  }
  console.log(data);
}

async function unfollow() {
  //alert("Form submitted");

  const frm = event.target;
  const resp = await fetch("/api-unfollow", {
    method: "POST",
    body: new FormData(frm),
  });
  const data = await resp.json();
  if (resp.ok) {
    console.log(data);
    document.getElementById(`profile_follow_form`).style.display = "block";
    document.getElementById(`profile_unfollow_form`).style.display = "none";

    document.getElementById(`profile_followers_number`).innerHTML =
      data.follower_count;
    return;
  }

  console.log(data);
}

function getFollowerNumber(follower_number, operator) {
  if (operator == "plus") {
    if (parseInt(follower_number) < 9999) {
      return parseInt(follower_number) + 1;
    } else if (follower_number == "9999") {
      return "10K";
    } else {
      return follower_number;
    }
  } else if (operator == "minus") {
    if (parseInt(follower_number) < 9999) {
      return parseInt(follower_number) - 1;
    } else if (follower_number == "10K") {
      return "9999";
    } else {
      return follower_number;
    }
  }
}

function showSearchResults() {
  document
    .getElementById(`search_results_container`)
    .classList.remove("hidden");
}

function hideSearchResults() {
  document.getElementById(`search_results_container`).classList.add("hidden");
}

let the_timer;
function search() {
  clearTimeout(the_timer);
  the_timer = setTimeout(async function () {
    //console.log("x")
    const res = await fetch("/api-search", {
      method: "POST",
    });
    const data = await res.json();
    console.log(data);
    //TODO redo to insert adjacent html
    document.getElementById("search_results_container").innerHTML = data
      .map(
        (result) =>
          `<div>
      <div>Name: ${result.name}</div>
    </div>`
      )
      .join("");
  }, 500);
}
