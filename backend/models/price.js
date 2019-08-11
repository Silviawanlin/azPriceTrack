const PriceFecther =  require('../priceFetchers/defaultPriceFetcher');
const PriceViewModel = require('../viewModels/priceViewModel') 
class Price {
    async getPrice(url)
    {
        let priceFecther = new PriceFecther();
        await priceFecther.request(url);
        return new PriceViewModel(url,await priceFecther.price(), await priceFecther.title());
    }

}
module.exports = Price;