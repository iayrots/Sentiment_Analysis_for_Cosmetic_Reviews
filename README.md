# Sentiment Analysis for Cosmetic Reviews

<br>

## [ Overview ]

### (1) Reason for topic selection :
> - Sometimes product ratings and reviews do not match.
> - When buying a product, the impact of reviews is higher than ratings.
> - I want to know whether a product is recommended according to the cosmetic terms in the reviews.

### (2) Objective : 
> #### Dictionary construction of cosmetic terminology emotion --> Sentiment Analysis of reviews

### (3) Source of Data : 
> #### Glowpick 화장품 리뷰 데이터

### (4) Tool :
> - Numpy
> - Pandas
> - Selenium
> - MongoDB
> - KoNLPy
> - NLTK
> - Gensim(Doc2Vec)
> - scikit-learn

<br>

## [ Contents ]

### (1) Data Crawling
> - Crawling data with the Selenium library
> - Storing the crawled data in MongoDB

### (2) Data Preprocessing
> - Removing emoticons, special symbols, etc. using regular expressions
> - Tokenizing/Pos tagging with Twitter(KoNLPy)
> - Exploring data using NLTK --> Plot sorted frequency of top 100 tokens
> - Building a dictionary of sentiments in cosmetic terms by hand
> - Classifying sentiments in reviews

### (3) Modeling
> - CountVectorizer --> Multinomial Naive Bayes
> - Doc2Vec --> Logistic Regression

### (4) Results
> - Precision : 0.85
> - Recall : 0.83
> - F1-score : 0.82

### (5) Limitation
> - Decreased accuracy due to low total amount of data
> - Vulnerable to mis-spell, typing errors, and spacing --> Importance of preprocessing
> - There is no cosmetic terms in the existing sentiment word dictionary

### (6) Follow Up
> - Crawling more data
> - Applying Deep Learning Neural Network Model to improve performance
> - Applying an item-based recommendation algorithm
> - Web implementation using the Flask library
