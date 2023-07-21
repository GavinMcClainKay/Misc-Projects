//Gavin Kay 2023
//Program uses puppeteer paired with brightdata proxy service to scrape 15 types of statistical information on 10,000 valorant players

import puppeteer from 'puppeteer-core';
import 'fs'
import { appendFile, appendFileSync, readFileSync } from 'fs';
const auth = '<AUTH FOR BRIGHTDATA.COM GOES HERE>';

async function ScrapeNames() {
    //init browswer and proxy service
    let browser;
    try {
        browser = await puppeteer.connect({
            browserWSEndpoint: auth
        });
        console.log('Browser Connected');
        browser.

        const page = await browser.newPage();
        page.setDefaultNavigationTimeout(2 * 60 * 1000);
        console.log('Page Initiated');
        
        //scrap top 10k names
        for(let pageNum = 1; pageNum <= 91; pageNum++) {
            //goto leaderboard page
            const url = 'https://tracker.gg/valorant/leaderboards/ranked/all/default?page=' + pageNum;
            await page.goto(url);
            console.log('At Leaderboard');

            //scrape all players on leaderboard page
            const in_game_names = await page.$$('span[class="trn-ign"]');
            for(let name of in_game_names) {
                const ign = await name.evaluate((node) => node.textContent);
                console.log(ign);
                appendFileSync('Playernames.txt', ign + '\n');
            }
        }

        return;

    } catch(e) {
        console.log('scrape failed ' + e);
    }
}

async function ScrapeData(start, end) {
    //init browswer and proxy service
    let browser;
    try {
        browser = await puppeteer.connect({
            browserWSEndpoint: auth
        });
        console.log('Browser Connected');

        //init browser page
        const page = await browser.newPage();
        page.setDefaultNavigationTimeout(2 * 60 * 1000);
        console.log('Page Initiated');
     
        //read playernames from file
        const all_names = readFileSync('Playernames.txt', { encoding:'utf-8' });
        //console.log(all_names)
        const igns = all_names.split('\n');

        for (let p = start; p < end; p++) {
            console.log(igns[p]);
            //format in game name
            let name = igns[p].split('#');
            let username = name[0].trim().replace(' ', '%20');
            let tagline = name[1].trim();

            //generate URL
            let url = 'https://tracker.gg/valorant/profile/riot/' + username + '%23' + tagline + '/overview';
            await page.goto(url);
            console.log('At Profile');

            //scrape data
            let output = igns[p] + '\n' + url + '\n';
            const values = await page.$$('span[class="value"]');
            for(let value of values) {
                let val = await value.evaluate((node) => node.textContent);
                output += val + ' : ';
            }
            appendFileSync('PlayerData.txt', output + '\n');
        }

    } catch(e) {
        console.log('scrape failed ' + e);
    }
    browser.close();
}

ScrapeData(62, 100);
ScrapeData(101, 200);
ScrapeData(201, 300);
ScrapeData(338, 400);
ScrapeData(466, 500);  
ScrapeData(501, 600);
ScrapeData(661, 700);
ScrapeData(701, 800);
ScrapeData(853, 900);
ScrapeData(961, 1000);
ScrapeData(1001, 1100);
ScrapeData(1101, 1200);
ScrapeData(1201, 1300);
ScrapeData(1366, 1400);
ScrapeData(1468, 1500);
ScrapeData(1560, 1600);
ScrapeData(1633, 1700);
ScrapeData(1763, 1800);
ScrapeData(1801, 1900);
ScrapeData(1954, 2000);


//TODO
//remove duplicates from data