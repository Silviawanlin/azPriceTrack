const BasePriceFecther = require('./basePriceFetcher');
const puppeteer = require('puppeteer');
var browser = null;
async function getBrowser()
{
    if(browser)
        return browser;
    else
        return await puppeteer.launch();
}
class DefaultPriceFetcher extends BasePriceFecther
{
    constructor()
    {
        super();
    }
    async request(url){
        this.browser = await getBrowser();
        this.page = await this.browser.newPage();
        await this.page.goto(url);
    }
    async price(){
        return await this.page.evaluate(() => document.querySelector('#priceblock_ourprice').innerText);
    }
    async title()
    {
        return await this.page.evaluate(() => document.querySelector('title').innerText);
    }

} 
module.exports = DefaultPriceFetcher