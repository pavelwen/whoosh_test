#!/usr/bin/env python
# -*- coding: UTF-8 -*-


from whoosh.analysis import Tokenizer, Token

from whoosh.index import create_in, open_dir
from whoosh.fields import *
from whoosh.query import Term, And

import jieba
from models import *

class ChineseTokenizer(Tokenizer):
    def __call__(self, value, positions=False, chars=False,
                 keeporiginal=False, removestops=True,
                 start_pos=0, start_char=0, mode='', **kwargs):
        assert isinstance(value, text_type), "%r is not unicode" % value
        t = Token(positions, chars, removestops=removestops, mode=mode,
                  **kwargs)
        seglist = jieba.cut_for_search(value)                       #使用结巴分词库进行分词
        for w in seglist:
            t.original = t.text = w
            t.boost = 1.0
            if positions:
                t.pos = start_pos + value.find(w)
            if chars:
                t.startchar = start_char + value.find(w)
                t.endchar = start_char + value.find(w) + len(w)
            yield t                                               #通过生成器返回每个分词的结果token


def ChineseAnalyzer():
    return ChineseTokenizer()


analyzer = ChineseAnalyzer()





def reindex(*args, **kwargs):

    import os
    _dir = 'indexdir'
    if os.path.exists(_dir):
        os.rmdir(_dir)
    os.mkdir(_dir)
    schema = Schema(title=TEXT(stored=True, analyzer=analyzer), path=ID(stored=True), content=TEXT(stored=True, analyzer=analyzer))
    ix = create_in(_dir, schema)




    session = Session()
    posts = session.query(Post).all()
    writer = ix.writer()
    for post in posts:
        writer.add_document(title=post.title, path=unicode(post.id), content=post.content)
    writer.commit()

    session.close()


def search(*args, **kwargs):

    ix = open_dir("indexdir")
    with ix.searcher() as searcher:


        term  = (Term("title", args[0].decode('utf-8')) & Term('content', args[0].decode('utf-8')))
        #term = Term("title", args[0].decode('utf-8'))
        results = searcher.search(term, limit=None)
        print results
        for result in results:
            print result.get('title'), result.get('path')


if __name__ == '__main__':
    import sys
    locals()[sys.argv[1]](*sys.argv[2:])
