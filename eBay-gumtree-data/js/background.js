// background.js
// Called when the user clicks on the browser action.
chrome.browserAction.onClicked.addListener(
  function(tab) {
    // Send a message to the active tab
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
      var activeTab = tabs[0];
      chrome.tabs.sendMessage(activeTab.id, {"message": "clicked_browser_action"});
    });
  }
);

// Called when content.js finish extracting data
chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    if(request.message === "gumtree") {
      request.data[5] = localStorage.username;
      copyToClipboard(request.data.join("\t"));
      var opt = {
        type: "basic",
        title: "Hi " + localStorage.username,
        message: request.data[1],
        iconUrl: "img/icon.png"
      }
      chrome.notifications.create("", opt, callback);
    }
    else if (request.message === "ebay") {
      request.data[3] = localStorage.username;
      var fn = request.data;
      console.log(request.data);
      copyToClipboard(fn[0]+'\n'+fn[1]+" "+fn[2]+" "+fn[3]+"\t"+fn[4]+" "+fn[5]+" "+fn[6]);
    }
  }
);

// Copy extracted data to clipboard
function copyToClipboard(str) {
  console.log("a");
  // Create a dummy input to copy the string array inside it
  var dummy = document.createElement("input");
  // Add it to the document
  document.body.appendChild(dummy);
  // Set its ID
  dummy.setAttribute("id", "dummy_id");
  document.getElementById("dummy_id").value=str;
  // Select, copy and remove after
  dummy.select();
  document.execCommand("copy");
  document.body.removeChild(dummy);
}

// dummy function for notification
function callback() {}
