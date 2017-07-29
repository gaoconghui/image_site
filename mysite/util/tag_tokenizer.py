# -*- coding:utf-8 -*-
from normal import ensure_unicode


class TagTokenizer(object):
    def __init__(self, tag_list):
        """
        在title中找到所有的tag
        最简单的实现是对遍历每个tag，看是否在title中，显然太慢
        这边采用类似jieba分词中的方法
        :param tag_list: 所有的tag list of string
        """
        self.tag_list = tag_list
        self.FREQ = {}
        self.initialize()

    def initialize(self):
        lfreq = {}
        for word in self.tag_list:
            try:
                word = ensure_unicode(word)
                lfreq[word] = 1
                for ch in xrange(len(word)):
                    wfrag = word[:ch + 1]
                    if wfrag not in lfreq:
                        lfreq[wfrag] = 0
            except ValueError:
                raise ValueError(
                    'invalid tag list entry  %s' % (word))
        self.FREQ = lfreq

    def get_DAG(self, sentence):
        DAG = {}
        N = len(sentence)
        for k in xrange(N):
            tmplist = []
            i = k
            frag = sentence[k]
            while i < N and frag in self.FREQ:
                if self.FREQ[frag]:
                    tmplist.append(i)
                i += 1
                frag = sentence[k:i + 1]
            DAG[k] = tmplist
        return DAG

    def cut(self, sentence):
        sentence = ensure_unicode(sentence)
        DAG = self.get_DAG(sentence)
        for k, v in DAG.iteritems():
            if not v:
                continue
            for end in v:
                yield sentence[k:end + 1]


if __name__ == '__main__':
    tag_list = ["夏美酱", "你好", "花の颜", "夏美", "天天"]
    tokenizer = TagTokenizer(tag_list)
    for k in tokenizer.cut("heelo 夏美酱 worl你好d 花の颜"):
        print k
