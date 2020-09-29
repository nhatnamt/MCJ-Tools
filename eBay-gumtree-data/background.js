// background.js
var user_name = "";
// Called when the user clicks on the browser action.
chrome.contextMenus.create({
  title: "Your title here",
  contexts: ["browser_action"],
  onclick: function() {
      chrome.tabs.create({ url: chrome.runtime.getURL("options.html") });
      console.log("click");
  }
});
chrome.browserAction.onClicked.addListener(function(tab) {
    // Send a message to the active tab
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
      var activeTab = tabs[0];
      chrome.tabs.sendMessage(activeTab.id, {"message": "clicked_browser_action"});
    });
  });
chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    if( request.message === "open_new_tab" ) {
      copyToClipboard(request.data);
      var opt = {
        type: "basic",
        title: "Primary Title",
        message: "Primary message to display",
        iconUrl: "img/icon.png"
      }
      chrome.notifications.create("", opt, callback);
    }
  }
);
function copyToClipboard(str) {
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
function callback() {
  console.log("Notification succesfull");
  //notification confirmed
}
