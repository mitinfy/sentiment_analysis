#sentiment analysis : blob : binary large object 
from textblob import TextBlob
# Sample text for emotion analysis
text = "oh this is very good news"
# Create a TextBlob object
blob = TextBlob(text)
# Determine sentiment polarity
sentiment_polarity = blob.sentiment.polarity
# Classify sentiment based on polarity
if sentiment_polarity > 0:
    sentiment = "Positive"
elif sentiment_polarity < 0:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print("Text:", text)
print("Sentiment Polarity:", sentiment_polarity)
print("Sentiment:", sentiment)
