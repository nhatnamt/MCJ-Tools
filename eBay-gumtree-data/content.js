
// content.js
chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    if( request.message === "clicked_browser_action" ) {
        var url = window.location.href;
        var p_title = $('title').text().split("|");
        
        var ad_name = p_title[0];
        var ad_id = p_title[p_title.length-1];
        var price = $('.j-original-price').text(); 
        var stock_id = $('#ad_description_details_content').text().split("#")[1].substring(0,5);
        var date = $('#ad-attributes dd:first').text();
        console.log(url);
        console.log(price);
        console.log(date);
        var output = price + "\t" + ad_id;
        chrome.runtime.sendMessage({"message": "open_new_tab", "data": output});
        //alert(stock_id + " " + ad_name + " " + ad_id + " " + price);
    }
  }
)
