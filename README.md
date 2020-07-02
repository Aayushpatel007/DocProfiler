## DocProfiler 
#### A Python package to generate document profiles and extract metadata from text in parallel using several Docker images and NLP tools/framweworks.

### Abstract

Amount of unstructured data has been growing continously which includes text documents, social media text, web blogs and articles. Extracting metadata and generating profiles can increase performance of Text/Document Reterival in field of Information Retrieval and also help us to analyze and understand data by converting it from a completly unstructured to a semi-structured format. Motive behind this python library is to combine open-source NLP tools/technologies together in a much efficient and easy way with help of Docker images and Asynchronous functionalities of Python to process them in parallel. 

### NLP tools/framework

| Task | Framework/Model | Docker Image
| ----- | ----- | ----- |
| Named Entity Recognition | [FlairNer](https://github.com/flairNLP/flair) | [docker pull aayushpatel007/flair_ner](https://hub.docker.com/r/aayushpatel007/flair_ner)|

