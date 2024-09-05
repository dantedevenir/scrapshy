function get_nordvpn_servers(host) {
    let config = {
        mode: "fixed_servers",
        rules: {
          singleProxy: {
            scheme: "https",
            host: host,
            port: parseInt(__PORT__)
          },
          bypassList: ["localhost"]
        }
    };
    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});
};

function callbackFn(details) {
    return {
        authCredentials: {
            username: "__USERNAME__",
            password: "__PASSWORD__"
        }
    };
}

chrome.webRequest.onAuthRequired.addListener(
        callbackFn,
        {urls: ["<all_urls>"]},
        ['blocking']
);

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === 'setProxy') {
        console.log('Received setProxy message with proxy:', message.proxy);
        get_nordvpn_servers(message.proxy);
        sendResponse({ status: 'success' });
        return true;
    }
});

get_nordvpn_servers("__HOST__")