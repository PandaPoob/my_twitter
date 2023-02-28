async function handleSubmitTweet() {
  const frm = event.target;

  const resp = await fetch("/tweet", {
    method: "POST",
    body: new FormData(frm),
  });

  const data = await resp.json();
  console.log(data);
}
