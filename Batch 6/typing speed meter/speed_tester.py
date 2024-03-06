import time
import random

def make_sentence():
    nouns = ['Puppy','Car','Rabbit','Girl','Monkey']
    verbs = ['runs','hits','jumps','drives','brafs']
    adv = ['crazily','dutifully','foolishly','merrily','occasionally']
    adj = ['adorable','clueless','dirty','odd','stupid']
    num = random.randint(0,5)
    Sentence = (f"{nouns[num]} {verbs[num]} {adv[num]} {adj[num]}")
    return Sentence

def typing_accuracy(word,type):
    char = sum(1 for a , t in zip(word,type) if a == t)
    accuracy = (char / len(word)) * 100
    return accuracy

def Wpm(word_type,running_time):
    minutes = running_time / 60 
    wpm = word_type / minutes
    return wpm
def main():
    print("Welcome to Typing Speed Test.!")
    input("Press Enter to start Typing...")
    
    sen  = make_sentence()
    print("Start Typing to Following the sentence:")
    print(sen)
    
    start_time = time.time()
    user_time = input()
    end_time = time.time
    
    running_time = end_time - start_time
    words_type = len(user_time.split())
    accuracy = typing_accuracy(sen,user_time)
    WordsPerMinute = Wpm(words_type,running_time)
    
    print("\nResults: ")
    print(f"Time Taken: {running_time} seconds")
    print(f"Word Type: {words_type}")
    print(f"Accuracy of your Typing: {accuracy}")
    print(f"Words Per Minute(WPM): {WordsPerMinute:.}")
    
main()