# encoding=utf-8

from zapian.api import Zapian
import os
import jieba
idx_db_path = '/home/jiang/works/whoosh_test/xapian'
if not os.path.exists(idx_db_path):
    os.mkdir(idx_db_path)

idx_db = Zapian(idx_db_path)

from models import *
from datetime import datetime


def build_index():


    idx_db.add_part('test')

    session = Session()
    posts = session.query(Post).all()
    for post in posts:



        idx_db.add_document('test',

                            {'title':  " ".join(list(jieba.cut_for_search(post.title))), 
                             'content': " ".join(list(jieba.cut_for_search(post.content)))
                             },

                            uid=unicode(post.id),
                            data={
                                "title": post.title
                            }
                            )


def search():
    query = [
        #[[u'title'], u'招聘', u'parse'],
        [u'content', u'招聘', u'anyof'],
    ]
    results = idx_db.search(["test"], query

                            )
    for result in results:
        doc = idx_db.get_document(result)
        print doc.get('title')

if __name__ == '__main__':
    import sys
    locals()[sys.argv[1]]()
