// content.js
chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    if( request.message === "clicked_browser_action" ) {
        var url = window.location.href;
        var p_title = $('title').text().split("|");
        if (window.location.hostname == "www.gumtree.com.au") {
        
        let val = [];
        val.push($('#ad_description_details_content').text().split("#")[1].substring(0,5));
        val.push(p_title[0]);
        val.push(p_title[p_title.length-1]);
        val.push($('.j-original-price').text());
        val.push($('#ad-attributes dd:first').text());
        val.push("","","",url);
        val[6] = prompt("Please enter item location!");
        chrome.runtime.sendMessage({"message": "pass_it_on", "data": val});
        } 
        else if (window.location.hostname == "www.ebay.com.au") {

        }
        else {
          alert("Not supported webpage!")
        }
    }
  }
)
