const eBayApi = require('ebay-api')

const eBay = new eBayApi({
  appId: 'NamTran-ChromeEx-PRD-608cfd9b0-9fcfd6a0',
  certId: 'PRD-08cfd9b0a4e4-3145-4a45-a944-e658',
  sandbox: false
});
 
async function get_data() {
    const item = await eBay.buy.browse.getItem('v1|254188828753|0');
    console.log(JSON.stringify(item, null, 2));

    //return item
}

get_data()