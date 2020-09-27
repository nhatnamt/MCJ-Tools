
// content.js
chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    if( request.message === "clicked_browser_action" ) {
        var url = window.location.href;
        //var myVar = $('.breadcrumbs__summary').val();
        var ad_id = $('.breadcrumb__item').text(); 
        var price = $('.j-original-price').text(); 
        var name = $('#ad-title').text();
        var stock_id = $('#ad_description_details_content').text()
        //var value = $('').$(this).attr('value');
        console.log(url);
        console.log(ad_id);
        console.log(price);
        alert(stock_id);
    }
  }
)