import {basePriceFecther} from "basePriceFecther";
import "puppeteer"
export class DefaultPriceFetcher extends basePriceFecther
{
    constructor()
    {
        this.browser = await puppeteer.launch();
        this.page = await browser.newPage();
    }
    async request(url){
        await this.page.goto(url);
    }
    async price(){
        return await page.evaluate(() => document.querySelector('#priceblock_ourprice').innerText);
    }

} 