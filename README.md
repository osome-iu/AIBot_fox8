# Introduction
This repo contains the code and information for the paper "Anatomy of an AI-powered malicious social botnet".

We provide a case study on a Twitter botnet that use ChatGPT to generate negative/harmful content and promote suspcious websites.

# Data release

We release the `fox8-23` benchmark dataset for distinguishing LLM-powered social bots and humans. 
The raw data can be downloaded from [zenodo link here].

The dataset contains the following accounts:

| Account type | Source | Number |
|--------------|--------|--------|
| Bot          | fox8 bots (this work) | 1140|
| Human        | [botometer-feedback](https://doi.org/10.1002/hbe2.115) | 285 |
| Human        | [gilani-17](https://doi.org/10.1145/3110025.3110090) | 285 |
| Human        | [midterm-2018](https://doi.org/10.1609/aaai.v34i01.5460) | 285 |
| Human        | [varol-icwsm](https://doi.org/10.1609/icwsm.v11i1.14871) | 285 |

For each account, we share up to 200 tweets from it.
Each line of the raw data file is a JSON object with the following schema:

```json
{
  "user_id": 123456,
  "label": "bot",
  "dataset": "fox8",
  "user_tweets": [
    tweet1,
    tweet2
    ...
  ]
}

```

# Code

We also share the code used to query [OpenAI's AI text editor](https://platform.openai.com/ai-text-classifier).

# Citation

```bib
@article{yang2023anatomy,
  title={Anatomy of an AI-powered malicious social botnet},
  author={Yang, Kai-Cheng and Menczer, Filippo},
  journal={Preprint arXiv:xxxx.xxxxx},
  year={2023}
}
```
