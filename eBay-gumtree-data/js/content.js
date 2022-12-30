// content.js
chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    if( request.message === "clicked_browser_action" ) {
        var url = window.location.href;
        var pageTitle = $('title').text().split("|");
        if (window.location.hostname == "www.gumtree.com.au") {
        
          let val = [];
          var item_info = $('#ad_description_details_content').text().split("#")[1].split("-");
          val.push(item_info[0]);
          val.push(pageTitle[0]);
          val.push(pageTitle[pageTitle.length-1]);
          val.push($('.j-original-price').text());
          val.push($('#ad-attributes dd:first').text());
          val.push("","","",url);
          if (item_info[1] == null) {
            val[6] = prompt("Please enter item location!");
          } 
          else {
            val[6] = item_info[1];
          }
          chrome.runtime.sendMessage({"message": "gumtree", "data": val});
        } 
        else if (window.location.hostname == "www.ebay.com.au") {
          let itemName = pageTitle[0];
          let itemID = $('#descItemNumber').text();
          let itemPrice = $('#prcIsum').text().split(" ")[1];
          let itemDate = null;

          try {
            let tmp = $('.listingHistoryInfo tr:last td:eq(1)').text().split(",");
            itemDate = tmp[0].substring(22,28)+" "+tmp[1].substring(1,5);
          } 
          catch (error) {
            itemDate = $(".ux-textspans").eq(15).text();
          }

          var tmp = prompt("Please enter stock id followed by '-' and location! Ex: O15-45666").split("-");
          let itemLocation = tmp[0]; 
          let itemSKU = tmp[1];

          let spacer = " ";
          let obj = [
            itemName,
            itemID,
            itemPrice,
            spacer,
            itemLocation,
            itemDate,
            itemSKU
          ];
        console.log(obj);
        chrome.runtime.sendMessage({"message": "ebay", "data": Object.values(obj)});
        console.log("Hi");
        }
        else {
          alert("Not supported webpage!")
        }

        //$(".container-ld-description").textContent.split('#')[1].split("INTERNATIONAL")
    }
  }
)
