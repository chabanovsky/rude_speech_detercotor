# encoding:utf-8
import csv
from models import Comment
from wiktionary_org import WiktionaryOrg
from utils import RudeWordsFromTheSite

class Analyser:
    def __init__(self):
        self.rude_word_list = WiktionaryOrg.all_words() + RudeWordsFromTheSite.processed_rude_words()
        for e in [u'ест', u'год', u'год', u'гугл', u'поиск',
                  u'уч', u'плат', u'плат', u'белар', u'гугл', 
                  u'русск', u'украин', u'росс', u'гугл', u'бан', 
                  u'минус', u'вуз', u'студент', 'фриланс', u'минусова', 
                  u'заминусова', u'спам', u'ум', u'порн',
                  u'вуз', u'бесполезн', u'лен', u'обоснова',
                  u'бирж']:
            try:
                self.rude_word_list.remove(e)
            except:
                print("Error removing key (%s)" % e)
        self.rude_word_list + [u'быдл']

    def analyse(self):
        comments = Comment.all_comments()
        rude_comments = list()
        for comment in comments:
            words = [word for word in comment.processed_text if word in self.rude_word_list]
            if len(words) > 0:
                rude_comments.append(comment)
                print("Found rude words (%s) by link (%s)" % (str(words), comment.link))
        print ("Found at total %s" % str(len(rude_comments)))
        return rude_comments

def main():
    analyser = Analyser()
    rude_comments = analyser.analyse()
    with open('result.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        for comment in rude_comments:
            writer.writerow((comment.text, comment.link))

if __name__ == "__main__":
    main()