document.getElementById('toggle').addEventListener('click', function() {
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
      chrome.scripting.executeScript({
        target: {tabId: tabs[0].id},
        function: toggleHover
      });
    });
  });
  
  function toggleHover() {
    const existingStyle = document.querySelector('style#hoverOverrideStyle');
    if (existingStyle) {
      existingStyle.remove();
    } else {
      const styleSheet = document.createElement('style');
      styleSheet.id = 'hoverOverrideStyle';
      styleSheet.type = 'text/css';
      styleSheet.innerText = 'a:hover { color: inherit !important; text-decoration: none !important; }';
      document.head.appendChild(styleSheet);
    }
  }
  