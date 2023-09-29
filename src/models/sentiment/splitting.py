from sklearn.model_selection import train_test_split

def spliting(text, sentiment, score):
    x_sent_train, x_sent_test, y_sent_train, y_sent_test = train_test_split(text, sentiment, test_size=0.2, random_state=42)
    return x_sent_train, x_sent_test, y_sent_train, y_sent_test