# Task 1 :Write a program that searches through reviews list and looks for keywords such as
#  "good", "excellent", "bad", "poor", and "average".
#  We want you to capitalize those keywords then print out each review.
#  Print out each review with the keywords in uppercase so they stand out.


keywords = ["good", "excellent", "bad", "poor", "average"]
reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."]

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]


def keyword_highlighter(reviews):
    # my_reviews = reviews.split(",")
    new_reviews = []
    new_review = ""
    for review in reviews:
        # arr = review.split()
        # for i in range(len(arr)): 
        #     if arr[i].lower().strip(".,") in keywords:
        #         arr[i] = arr[i].upper()
        # var = " ".join(arr)
        for keyword in keywords:
            if keyword in review:
                new_review = review.replace(keyword, keyword.upper())
            elif keyword.capitalize() in review:
                new_review = review.replace(keyword.capitalize(), keyword.upper())

        new_reviews.append(new_review)
        

    return new_reviews

print(keyword_highlighter(reviews))

# Task 2 :Develop a function that tallies the number of positive and negative words in each review. 
#  The function should return the total count of positive and negative words.

def sentiment_tally(reviews,positive_words,negative_words):
    positive_counter = 0
    negative_counter = 0
    for review in reviews:
        for positive_word in positive_words:
            positive_counter += review.lower().count(positive_word)
        for negative_word in negative_words:
            negative_counter += review.lower().count(negative_word)

    return positive_counter, negative_counter

positive_counter, negative_counter = sentiment_tally(reviews, positive_words, negative_words)

print(positive_counter, negative_counter)
        
            





# Task 3: Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. 
# Ensure that the summary does not cut off in the middle of a word.

summaries = []

def summarize_reviews(reviews, length=30):
    for review in reviews:
        if len(review) <= length:
            summaries.append(review)
            continue
        last_space_index = review.rfind(' ', 0, length)
        if last_space_index != -1:
            summary = review[:last_space_index] + "..."
        else:
             summary = review[:length] + "..."

        summaries.append(summary)
    return summaries
print(summaries)
    


summarized_reviews = summarize_reviews(reviews)
for i, summary in enumerate(summarized_reviews):
    print(f'Reviews {i+1}: {summary}')
        




