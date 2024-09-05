(function() {
    function setProxy(host) {
      chrome.runtime.sendMessage({ action: 'setProxy', proxy: host }, (response) => {
        if (response && response.status === 'success') {
          console.log('Proxy set successfully.');
        } else {
          console.log('Failed to set proxy.');
        }
      });
    }

    window.addEventListener("message", (event) => {
        if (event.source !== window)
          return;
    
        if (event.data.type && (event.data.type === "SET_PROXY")) {
            console.log(event.data)
            setProxy(event.data.proxy);
        }
      }, false);
    
})();