const puppeteer = require('puppeteer');

async function run() {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  await page.goto('https://www.amazon.com/gp/product/B01HOS31B0?pf_rd_p=183f5289-9dc0-416f-942e-e8f213ef368b&pf_rd_r=VJQJJSGTMRT23K2K6S8T');
  let price = await page.evaluate(() => document.querySelector('#priceblock_ourprice').innerText)
  console.log(price);
  browser.close();
}

run();