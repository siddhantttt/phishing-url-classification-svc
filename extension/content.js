const links = document.querySelectorAll("a");
console.log("Making an API call");

links.forEach((link) => {
  link.addEventListener("mouseover", function (e) {
    const href = this.href;

    removeTooltips();

    // Fetch data from the API
    fetch(`https://api.example.com/data?url=${encodeURIComponent(href)}`)
      .then((response) => response.json())
      .then((data) => {
        // Create tooltip element and show data
        console.log(data);
        displayTooltip(e, data.output);
      })
      .catch((error) => {
        console.error("Fetch error:", error);
        // Display error tooltip
        displayTooltip(e, "Error loading data. Please try again later.");
      });
  });

  link.addEventListener("mouseout", removeTooltips);
});

function displayTooltip(e, text) {
  const tooltip = document.createElement("div");
  tooltip.className = "tooltip";
  tooltip.style.position = "absolute";
  tooltip.style.left = `${e.pageX}px`;
  tooltip.style.top = `${e.pageY + 20}px`;
  tooltip.style.background = text == 0 ? "green" : "red";
  tooltip.style.color = "white";
  tooltip.style.border = "1px solid black";
  tooltip.style.padding = "5px";
  tooltip.style.borderRadius = "0.5rem";
  tooltip.style.boxShadow = "0 4px 8px rgba(0,0,0,0.2)";
  tooltip.innerHTML = text == 0 ? <strong>✔</strong> : <strong>✖</strong>;
  tooltip.innerHTML += text == 0 ? "Looks safe!" : "Seems fishy!";
  document.body.appendChild(tooltip);
}

function removeTooltips() {
  const tooltips = document.querySelectorAll(".tooltip");
  tooltips.forEach((tooltip) => {
    tooltip.remove();
  });
}
