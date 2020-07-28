# encoding:utf-8
import datetime
import collections
import csv
from text_processing import process_text

class Comment:
    __comments = None

    def __init__(self, text, link):
        self.text = text
        self.link = link
        self.processed_text = [word for word in process_text(text).split(' ') if len(word.strip()) > 0]

    @staticmethod
    def all_comments():
        if Comment.__comments is not None:
            return Comment.__comments
        Comment.__comments = Comment.parse_chat_comments() + Comment.parse_site_comments()
        return Comment.__comments

    @staticmethod
    def parse_chat_comments(filename='chat_comments.csv'):
        result = list()
        with open(filename, 'rt', encoding="utf8") as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            for row in csv_reader:
                try:
                    date, author, message = row
                    try:
                        link, text = message.split('|')
                        result.append(Comment(text, link))
                    except:
                        print ("Cannot parse a message (%s)" % message)
                except:
                    print("Cannot parse a row (%s)" % row)
                

        return result

    @staticmethod
    def parse_site_comments(filename='site_comments.csv'):
        result = list()
        with open(filename, 'rt', encoding="utf8") as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            for row in csv_reader:
                try:
                    link, text = row
                    result.append(Comment(text, link))
                except:
                    print("Cannot parse a row (%s)" % row)

        return result