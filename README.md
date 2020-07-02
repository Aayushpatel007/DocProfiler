## DocProfiler 
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

