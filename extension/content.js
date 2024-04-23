const links = document.querySelectorAll('a');
console.log("Making an API call");

links.forEach(link => {
  link.addEventListener('mouseover', function(e) {
    const href = this.href;

    // Fetch data from the API
    fetch(`https://api.example.com/data?url=${encodeURIComponent(href)}`)
      .then(response => response.json())
      .then(data => {
        // Create tooltip element and show data
        displayTooltip(e, data.description);
      })
      .catch(error => {
        console.error('Fetch error:', error);
        // Display error tooltip
        displayTooltip(e, "Error loading data. Please try again later.");
      });
  });
});

function displayTooltip(e, text) {
  const tooltip = document.createElement('div');
  tooltip.style.position = 'absolute';
  tooltip.style.left = `${e.pageX}px`;
  tooltip.style.top = `${e.pageY + 20}px`;
  tooltip.style.background = 'white';
  tooltip.style.border = '1px solid black';
  tooltip.style.padding = '5px';
  tooltip.innerHTML = text;
  document.body.appendChild(tooltip);

  e.currentTarget.addEventListener('mouseout', function() {
    tooltip.remove();
  });
}
