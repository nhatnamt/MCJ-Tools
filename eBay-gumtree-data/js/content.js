// content.js
chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    if( request.message === "clicked_browser_action" ) {
        var url = window.location.href;
        var p_title = $('title').text().split("|");

        let val = [];
        val.push($('#ad_description_details_content').text().split("#")[1].substring(0,5));
        val.push(p_title[0]);
        val.push(p_title[p_title.length-1]);
        val.push($('.j-original-price').text());
        val.push($('#ad-attributes dd:first').text());
        val.push("","","",url);
        chrome.runtime.sendMessage({"message": "pass_it_on", "data": val});
        //alert(stock_id + " " + ad_name + " " + ad_id + " " + price);
    }
  }
)