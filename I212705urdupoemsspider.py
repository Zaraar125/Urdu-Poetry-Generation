import scrapy
import pandas as pd 
class I212705urdupoemsspiderSpider(scrapy.Spider):
    name = "I212705urdupoemsspider"
    allowed_domains = ["www.rekhta.org"]
    start_urls = ["https://www.rekhta.org"]
    # Navigating to the important page 
    def parse(self, response):
        complete_url=response.urljoin(response.xpath('//*[@id="navbarFilter"]/li[1]/a').attrib['href']+'?contentFilter=nazms&lang=ur')
        yield response.follow(complete_url,callback=self.parse_1)   
    # Extracting all required poets         
    def parse_1(self,response):
        a=response.xpath('//*[@id="content"]/div/div/div/div[3]/div/div[5]/div/div[1]/div/div/div/div[2]/a/@href').getall()
        for i in a:
            yield response.follow(i,callback=self.parse2)
    # Extracting links of Poems of each Poet
    def parse2(self,response):
        a=response.xpath('//*[@id="content"]/div/div[2]/div[4]/div/a[2]/@href').getall()
        for i in a:
            yield response.follow(response.urljoin(i),callback=self.extract_text)
    # Extracting Poem from Each link 
    # Parsing the HTML Tags to reach the required text
    def extract_text(self,response):
        poet_name=response.xpath('//*[@id="content"]/div/div/div[1]/div[1]/h2/a/text()').get()
        nazm_name=response.xpath('//*[@id="content"]/div/div/div[1]/h1/text()').get()
        a=response.css('div.w p').getall()
        temper=[]
        for i in a[2:]:
            soup = scrapy.Selector(text=i, type="html")
            urdu_spans = soup.xpath('//span[@data-m]')
            urdu_words = [span.xpath('text()').get().strip() for span in urdu_spans]
            z=' '.join(urdu_words)
            temper.append(z)
    # Saving the extracted poems into a csv file 
        data=pd.read_csv('scrapped_poems.csv',usecols= ['poem_line','nazm_name','author_name'])
        data=pd.concat([data,pd.DataFrame({'poem_line':temper,'nazm_name':[nazm_name for i in range(len(temper))],'author_name':[poet_name for i in range(len(temper))]})])
        data.to_csv('scrapped_poems.csv')
        

