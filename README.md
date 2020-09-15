## DocProfiler 
## Note: (Major changes being made. Will update here in short time)
A Python package to generate document profiles and extract metadata from text in parallel using several Docker images and NLP tools/framweworks.

### Abstract

Amount of unstructured data has been growing continously which includes text documents, social media text, web blogs and articles. Extracting metadata and generating profiles can increase performance of Text/Document Reterival in field of Information Retrieval and also help us to analyze and understand data by converting it from a completly unstructured to a semi-structured format. Motive behind this python library is to combine open-source NLP tools/technologies together in a much efficient and easy way with help of Docker images and Asynchronous functionalities of Python to process them in parallel. 

### NLP tools/framework

| Task | Framework/Model | Docker Image (GPU support available) | Ports |
| ----- | ----- | ----- | ---- |
| Unsupervised Keyphrase Extraction | [SIFRank-2020](https://github.com/sunyilgdx/SIFRank) | [docker pull aayushpatel007/sifrank-keyphrases](https://hub.docker.com/r/aayushpatel007/sifrank-keyphrases)| 5000 |
| Named Entity Recognition | [FlairNer](https://github.com/flairNLP/flair) | [docker pull aayushpatel007/flair_ner](https://hub.docker.com/r/aayushpatel007/flair_ner)| 5001 |
| Entity Linking | [TAGME](https://sobigdata.d4science.org/web/tagme/tagme-help) | [docker pull aayushpatel007/tagme-entity-linking](https://hub.docker.com/r/aayushpatel007/tagme-entity-linking)| 5002 |
| Text Summarization | [TextRank](https://radimrehurek.com/gensim/summarization/summariser.html) | [docker pull aayushpatel007/text-summarization](https://hub.docker.com/r/aayushpatel007/text-summarization)| 5003 | 
| GeoParsing | Mordecai (Upcoming) | --Upcoming-- | N.A |
| Language Detection | --Upcoming-- | --Upcoming-- | N.A |
| Readability Analysis | --Upcoming-- | --Upcoming-- | N.A |

### Run Docker containers

To generate a document profile, you would need to run the above containers: (It is not necassary to run all the containers. You can select the task and run it accordingly.) However, the ports mentioned above needs to be opened for the following containers: 

Eg: 

``` 

docker container run -d -p 5000:5000 aayushpatel007/sifrank-keyphrases 0 # Replace 0 with -1 while running on a CPU. 

docker container run -d -p 5001:5001 aayushpatel007/flair_ner 1 # defaut uses ner-ontonotes trained model. If running on CPU, you can replace 1 with 0. 

docker container run -d -p 5002:5002 aayushpatel007/tagme-entity-linking 0.2 "tag_me_api_token" # Note that when running entity-linking container you need TAGME API token 

docker container run -d - p 5003:5003 aayushpatel007/text-summarization

```


```
Now you can access your API using: 

http://host_ip_address:5000/sifrank # For Unsupervised Keyphrase detection
http://host_ip_address:5001/flairner # For Named Entity Recognition. 14 entities (PERSON, GPE, EVENTS, ORG ,NORP ,ETC)
http://host_ip_address:5002/tagme # For Entity-Linking
http://host_ip_address:5003/textrank # For Text Summarization 

```
### Performance comparision between Docprofiler and running these tools in sequential manner. (+44% times faster)

<img src="https://github.com/Aayushpatel007/DocProfiler/blob/master/Time-comparision.png" width="600" height="500" style="vertical-align:center;">

### Use DocProfiler:

```
pip3 install docprofiler==1.0.1

```

```
from DocProfiler import docprofiler as d


text = """THREE WEEKS ago, Phil Morgan, head of the financial-services initiative at the Welsh Development Agency, took an exhibition to Bristol, to 'sell' to that city's business community the attractions of relocating in south-east Wales. Although the day-long event was one of a series that will shortly go to Reading and then to places along the M25 corridor around London, the Bristol visit touched a raw nerve. Relations have never been good between Bristol and South Wales, and the English city resented what it saw as the seduction of one of its own growth industries. The move illustrates the aggressive policy that is being followed in order to attract financial-services companies to South Wales. Cardiff, as the main centre for the sector in south-east Wales, has never had a particularly strong indigenous financial industry. Before Mr Peter Walker, then secretary of state for Wales, launched his financial services initiative to build the city's financial nexus three years ago, effectively all that the Welsh capital had to offer was: the Bank of Wales, set up in the 1972; one medium-sized building society, the Principality, 28th in the societies' pecking order; the venture capital group, 3i; and one major incomer, Chemical Bank. Mr Walker's initiative had immediate results. NM Rothschild has been the five-star name to arrive, but others - including National Provident Institution, Banque Nationale de Paris, Axa, the French insurance giant, Willis Wrightson (also in insurance), and stockbrokers Bell, Lawrie, White - have strengthened the sector. While this financial muscle has greatly added to the city's commercial depth, it has not yet turned Cardiff into an important financial centre. 'You still have to look at Cardiff as an emerging financial city,' says Peter Davies, Rothschild's director of corporate finance in Wales. 'It is not possible to get institutional support for a major issue, and if a growing business wants to raise equity capital, it has really only one choice - 3i.' Rothschild's own venture fund is based in London, and of two attempts by the WDA to set up funds, the Cardiff Consortium came to nothing and the Welsh Venture Capital Fund was eventually closed. That situation is about to change. Meirion Thomas, an executive director of the WDA, says that a new fund, Venture Link, is raising Pounds 5m from Welsh institutions, such as the local-authority pension funds, and expects to be in business within the next few months. Venture Link, which has two other funds in Britain, has opened an office in Cardiff, and will gear its lending to the bottom end of the market, offering capital between Pounds 25,000 and Pounds 150,000. 'The signs are that people within Wales are looking much more to institutions within the country for their needs,' says Mr Thomas. 'The Bank of Wales, for instance, is getting more into the risk-capital business, and that is encouraging.' Venture Link is not the only one interested in Cardiff. Credit Lyonnais, the French bank, having already opened a dozen regional centres in Britain, is considering an office in Cardiff, which it currently serves from Bristol through a former WDA official. Other entrants are in the pipeline, according to Mr Morgan. At 3i, Nigel Guy, the Cardiff director, says there is plenty of money for lending, but that the city lacks a large corporate base, such as that of the West Midlands, to sustain a major financial sector. Last year, 3i completed Pounds 18m of business in 50 investments, but the 12 months to March 1991 'was not so good. The position in Cardiff reflected what is happening in the rest of the UK economy.' Even so, Mr Guy says there is considerable interest in management buy-outs, boosted by companies drawing back into their core activities and seeking to sell what they see as peripheral businesses. 'There has been an upsurge in interest in this sector in the past four months,' he says, 'including a couple of seven-figure deals, such as that at British Rotatherm, which was bought from its Scandinavian parents.' This activity encourages Mr Morgan at the financial services initiative, who says that the 'temperature is still good, despite the recession. The downturn in the City of London provides us in Cardiff with an opportunity to attract firms to a location that provides them with a better cost base. Both wage and salary levels, and property prices, are much more attractive here than in the south east of England.' Mr Morgan has been aiming particularly at the insurance companies, such as Axa, believing that, as the continental concerns grow increasingly larger in preparation for the single market in 1992, they will want to have national networks of offices. 'We want them to look at Cardiff and the rest of south-east Wales as a potential location,' he says, offering the example of DAS, a German concern, which late last year opened an office in Bedwas, between Cardiff and Newport. 'A number of overseas banks, such as Credit Agricole and Paribas, of France, and the Canadian Imperial Bank of Commerce, have already financed deals in Wales. 'The electronics-based Gooding Group has Japan's C Itoh and the American Citibank among its major shareholders; and with this level of interest, I am convinced we shall be seeing major banks of their standing actually opening offices in Cardiff before long."""

data,final_time = d.generate_profile(text, URL_LIST=['http://host_ip_addr:5001/flairner','http://host_ip_addr:5030/textrank','http://host_ip_addr:5020/tagme','http://host_ip_addr:5000/sifrank'],no_of_keyphrases=10)

print(data)

```

### Output 

```
{
  'DOC': '1',
  'Tagme-entities': [
    'Welsh Development Agency',
    'Bristol',
    'M25 motorway',
    'Wales',
    'Cardiff',
    'Peter Walker Baron Walker of Worcester',
    'Carole King',
    'Galaxy Nexus',
    'Bank of Wales',
    'Venture capital',
    'Chemical Bank',
    'BNP Paribas',
    'Paris',
    'AXA',
    'Equity finance',
    '3i',
    'N M Rothschild amp Sons',
    'Cardiff City F C',
    'Pension',
    'Cr dit Lyonnais',
    'Recession',
    'South East England',
    'East of England',
    'Insurance',
    'Cardiff University',
    'Bedwas',
    'Newport Wales',
    'Cr dit Agricole',
    'Canadian Imperial Bank of Commerce',
    'Japan',
    'Itochu',
    'Citibank'
  ],
  'Keyphrases': [
    'financial-services initiative',
    'phil morgan',
    'welsh development agency',
    'business community',
    'south-east wales',
    'welsh institutions',
    'strong indigenous financial industry',
    'bristol',
    'venture capital group',
    'french insurance giant'
  ],
  'Summary': "THREE WEEKS ago, Phil Morgan, head of the financial-services initiative at the Welsh Development Agency, took an exhibition to Bristol, to 'sell' to that city's business community the attractions of relocating in south-east Wales. Before Mr Peter Walker, then secretary of state for Wales, launched his financial services initiative to build the city's financial nexus three years ago, effectively all that the Welsh capital had to offer was: the Bank of Wales, set up in the 1972; one medium-sized building society, the Principality, 28th in the societies' pecking order; the venture capital group, 3i; and one major incomer, Chemical Bank. 'You still have to look at Cardiff as an emerging financial city,' says Peter Davies, Rothschild's director of corporate finance in Wales. 'It is not possible to get institutional support for a major issue, and if a growing business wants to raise equity capital, it has really only one choice - 3i.' Rothschild's own venture fund is based in London, and of two attempts by the WDA to set up funds, the Cardiff Consortium came to nothing and the Welsh Venture Capital Fund was eventually closed. Meirion Thomas, an executive director of the WDA, says that a new fund, Venture Link, is raising Pounds 5m from Welsh institutions, such as the local-authority pension funds, and expects to be in business within the next few months. At 3i, Nigel Guy, the Cardiff director, says there is plenty of money for lending, but that the city lacks a large corporate base, such as that of the West Midlands, to sustain a major financial sector. Both wage and salary levels, and property prices, are much more attractive here than in the south east of England.' Mr Morgan has been aiming particularly at the insurance companies, such as Axa, believing that, as the continental concerns grow increasingly larger in preparation for the single market in 1992, they will want to have national networks of offices. 'We want them to look at Cardiff and the rest of south-east Wales as a potential location,' he says, offering the example of DAS, a German concern, which late last year opened an office in Bedwas, between Cardiff and Newport.",
  'GPE': [
    'South Wales,',
    'South Wales. Cardiff,',
    'Wales,',
    'France,',
    'Bedwas,',
    'Cardiff',
    'Bristol',
    'Newport.',
    'Wales.',
    'Bristol,',
    'Britain,',
    'Reading',
    "England.'",
    'Cardiff,',
    'Wales',
    'UK',
    'London,'
  ],
  'ORG': [
    "Japan's C Itoh",
    'Venture Link',
    'Banque Nationale de Paris, Axa,',
    'DAS,',
    'Chemical Bank.',
    'the City of London',
    'Willis Wrightson',
    'the Principality, 28th',
    'Cardiff. Credit Lyonnais,',
    'the Cardiff Consortium',
    'Gooding Group',
    'Wales,',
    'Venture Link,',
    'NM Rothschild',
    "'The Bank of Wales,",
    'Axa,',
    'WDA',
    'Paribas,',
    'the Welsh Development Agency,',
    'WDA,',
    'British Rotatherm,',
    'the Canadian Imperial Bank of Commerce,',
    'Citibank',
    'the Bank of Wales,',
    'state',
    'Credit Agricole'
  ],
  'PERSON': [
    'Nigel Guy,',
    'Peter Walker,',
    'Bell, Lawrie, White',
    'Thomas.',
    "Peter Davies, Rothschild's",
    'Guy',
    'Morgan',
    'Meirion Thomas,',
    'Phil Morgan,',
    'Morgan.',
    "Walker's"
  ],
  'LOC': [
    'the West Midlands,'
  ],
  'NORP': [
    'Welsh',
    'French',
    'English',
    'Scandinavian',
    'American',
    'German'
  ],
  'EVENT': [
    
  ],
  'DATE': [
    'the next few months.',
    'Last year, 3i',
    'the 12 months to March 1991',
    'THREE WEEKS ago,',
    'three years ago,',
    '1992,',
    'late last year',
    'the 1972;',
    "the past four months,'"
  ],
  'MONEY': [
    'Pounds 25,000',
    'Pounds 5m',
    'Pounds 18m'
  ],
  'ADDITIONAL': [
    '50',
    'M25',
    'one',
    '150,000.',
    'two',
    'dozen'
  ],
  'Time_by_SIFRank_keyphrases': 1.515525030998106,
  'Time_by_EntityLinking': 3.566188880999107,
  'Time_by_TextSummarization': 0.07235045199922752,
  'Time_by_FlairNER': 2.02276362200064
}

Total time taken by docprofiler : 3.9456855

```

### Refrences

Sun, Yi & Qiu, Hangping & Zheng, Yu & Wang, Zhongwei & Zhang, Chaoran. (2020). SIFRank: A New Baseline for Unsupervised Keyphrase Extraction Based on Pre-trained Language Model. IEEE Access. PP. 1-1. 10.1109/ACCESS.2020.2965087. 


Akbik, Alan & Bergmann, Tanja & Vollgraf, Roland. (2019). Pooled Contextualized Embeddings for Named Entity Recognition. 724-728. 10.18653/v1/N19-1078. 


Hasibi, Faegheh & Balog, Krisztian & Bratsberg, Svein. (2016). On the Reproducibility of the TAGME Entity Linking System. 10.1007/978-3-319-30671-1. 


