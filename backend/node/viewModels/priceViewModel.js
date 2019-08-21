class PriceViewModel{
    constructor(url, price, title, historicalPrices)
    {
        this.url = url;
        this.price = price;
        this.title = title;
        this.historicalPrices = [{"date": "06/30/2019", "price": "90"}, {"date": "07/31/2019", "price": "80"}, {"date": "08/1/2019", "price": "90"}];
    }
}
module.exports = PriceViewModel;