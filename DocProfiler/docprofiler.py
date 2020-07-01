import asyncio
from timeit import default_timer
import requests
from aiohttp import ClientSession
json_data = {}

total_asynchronous_time = 0.0
total_synchronous_time = [0]

time_by_sifrank = [0]
time_by_flairner = [0] 
time_by_tagme = [0]
time_by_textrank = [0]
       
current_document = ""

def demo_async(urls):
    """Fetch list of web pages asynchronously."""
    loop = asyncio.get_event_loop() # event loop
    future = asyncio.ensure_future(fetch_all(urls,time_by_sifrank,time_by_flairner,time_by_tagme,time_by_textrank,total_asynchronous_time,total_synchronous_time,current_document)) # tasks to do
    loop.run_until_complete(future) # loop until done
    
async def fetch_all(urls,time_by_sifrank,time_by_flairner,time_by_tagme,time_by_textrank,total_asynchronous_time,total_synchronous_time,current_document):
    """Launch requests for all web pages."""
    tasks = []
    fetch.start_time = dict() # dictionary of start times for each url
    async with ClientSession() as session:
        for url in urls:
            task = asyncio.ensure_future(fetch(url, session,time_by_sifrank,time_by_flairner,time_by_tagme,time_by_textrank,current_document))
            tasks.append(task) # create list of tasks
        r = await asyncio.gather(*tasks) # gather task responses
        text_sum=entities_tagme=keyphrases=GPE=ORG=PERSON=EVENT=DATE=MONEY=NORP=LOC=ADDITIONAL = ""
        for i in r:
            import json
            i = json.loads(i.decode('utf-8')) 
            for k,v in i.items():
                if k == "Summary":
                    text_sum = v
                elif k == "Entity-Linking-Entities":
                    entities_tagme = v
                elif k == "Keyphrases":
                    keyphrases = v
                elif k == "GPE":
                    GPE = v
                elif k == "ORG":
                    ORG = v
                elif k == "PERSON":
                    PERSON = v
                elif k == "EVENT":
                    EVENT = v
                elif k == "DATE":
                    DATE = v
                elif k == "MONEY":
                    MONEY = v
                elif k == "NORP":
                    NORP = v
                elif k == "LOC":
                    LOC = v
                elif k == "ADDITIONAL":
                    ADDITIONAL = v
        global json_data
        json_data = {
            'DOC': current_document.strip(),
            'Tagme-entities': entities_tagme,
            'Keyphrases': keyphrases,
            'Summary': text_sum.strip().replace("\n", " ").replace("\r", " ").replace("\t", " "),
            'GPE' : GPE,
            'ORG' : ORG,
            'PERSON': PERSON,
            'LOC': LOC,
            'NORP': NORP,
            'EVENT' : EVENT,
            'DATE': DATE,
            'MONEY': MONEY,
            'ADDITIONAL' : ADDITIONAL,
            'Time_by_SIFRank_keyphrases': time_by_sifrank[-1],
            'Time_by_EntityLinking' : time_by_tagme[-1],
            'Time_by_TextSummarization' : time_by_textrank[-1],
            'Time_by_FlairNER' : time_by_flairner[-1]

        } 

async def fetch(url, session,time_by_sifrank,time_by_flairner,time_by_tagme,time_by_textrank,current_document):
    """Fetch a url, using specified ClientSession."""
    fetch.start_time[url] = default_timer()
    
    async with session.post(url,json = {"text":data,"N":number_of_keyphrases,"Sifrankplus":1}) as response:
        resp = await response.read()
        
        elapsed = default_timer() - fetch.start_time[url]
        if 'sifrank' in url:
            time_by_sifrank.append(elapsed)
        elif 'flairner' in url:
            time_by_flairner.append(elapsed)
        elif 'tagme' in url:
            time_by_tagme.append(elapsed)
        elif 'textrank' in url:
            time_by_textrank.append(elapsed)
        return resp

def generate_profile(textdata,URL_LIST,no_of_keyphrases):
    
    global data 
    global number_of_keyphrases
    number_of_keyphrases = no_of_keyphrases
    data = textdata
    start_time = default_timer()
    demo_async(URL_LIST)
    tot_elapsed = default_timer() - start_time
    return json_data,tot_elapsed
    
#s,tt = generate_profile(data_a,URL_LIST = ['http://127.0.0.1:5002/tagme','http://127.0.0.1:5003/textrank'],no_of_keyphrases=10)
#print(s)
#print(tt)
