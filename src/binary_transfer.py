#!/bin/env python
#coding:utf-8
#Author:hanzhonghua@dingfudata.com

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

seq = set([u'一', u'二', u'三', u'四', u'五', u'六', u'七', u'八', u'九' \
            , u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9', u'0'])

seq2one = { u'一':u'一', u'二':u'一', u'三':u'一', u'四':u'一', u'五':u'一' \
            , u'六':u'一', u'七':u'一', u'八':u'一', u'九':u'一' \
            , u'十':u'一' \
            , u'1':u'1', u'2':u'1', u'3':u'1', u'4':u'1', u'5':u'1' \
            , u'6':u'1', u'7':u'1', u'8':u'1', u'9':u'1', u'0':u'1'}
seqUniq = { u'一':u'1', u'二':u'2', u'三':u'3', u'四':u'4', u'五':u'5' \
            , u'六':u'6', u'七':u'7', u'八':u'8', u'九':u'9' \
            , u'十':u'10' \
            , u'1':u'1', u'2':u'2', u'3':u'3', u'4':u'4', u'5':u'5' \
            , u'6':u'6', u'7':u'7', u'8':u'8', u'9':u'9', u'0':u'0'}

seperate = set([u'、', u'.', u'(', u'（', u')', u'）', u' ', u'\t'])

seq2label = {
            u'':u''
            , u'':u''
            , u'':u''
            , u'':u''
            , u'':u''
            , u'【':u'【'
            , u'◆':u'◆'
            , u'■':u'■'
            , u'':u''
            , u'+':u'+'
            , u'':u''
            , u'*':u'*'
        }

import cPickle

def dumps(dirs):
    dirs = dirs.strip()
    with open(dirs+'/seq.pkl', 'wb') as fid:
        cPickle.dump(seq, fid)
    with open(dirs+'/seq2one.pkl', 'wb') as fid:
        cPickle.dump(seq2one, fid)
    with open(dirs+'/seqUniq.pkl', 'wb') as fid:
        cPickle.dump(seqUniq, fid)
    with open(dirs+'/seperate.pkl', 'wb') as fid:
        cPickle.dump(seperate, fid)
    with open(dirs+'/seq2label.pkl', 'wb') as fid:
        cPickle.dump(seq2label, fid)
    print >> sys.stderr, "dump over"


if __name__ == '__main__':
    dumps(sys.argv[1])

