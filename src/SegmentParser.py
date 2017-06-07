#!/bin/env python
#-*- coding:utf-8 -*-

from __future__ import unicode_literals

import sys
import cPickle
import logging

class SegmentParser:

	def __init__(self):
		self.seq = None
		self.seq2one = None
		self.seqUniq = None
		self.seperate = None
		self.seq2label = None

	def init(self, dirs):
		'''
		加载字典
		'''
		dirs = dirs.strip()
		with open(dirs+'/seq.pkl', 'rb') as fid:
			self.seq = cPickle.load(fid)
		with open(dirs+'/seq2one.pkl', 'rb') as fid:
			self.seq2one = cPickle.load(fid)#编号->样式
		with open(dirs+'/seqUniq.pkl', 'rb') as fid:
			self.seqUniq = cPickle.load(fid) #编号归一化
		with open(dirs+'/seperate.pkl', 'rb') as fid:
			self.seperate = cPickle.load(fid)#分隔符吧
		with open(dirs+'/seq2label.pkl', 'rb') as fid:
			self.seq2label = cPickle.load(fid)
		return True
		
	def seq_type(self, ss):
		'''
		返回序列的样式，以 1 为类型
		'''
		if len(ss) < 3:
			return None, None
		beg= -1
		end = -1
		nums = ''
		is_num = False
		typ = None
		for i in range(2):
			beg = i
			if ss[i] not in self.seq2one:
				continue
			j = i
			while j < len(ss) and j < i + 4:
				end = j
				if ss[j] not in self.seq2one:
					break
				nums += self.seqUniq[ss[j]]
				typ = self.seq2one[ss[j]]
				j += 1
			break
		if end < 0:
			return None, None
		nn = int(nums)
		if nn > 30:
			return None, None
		if ss[end] in self.seperate:
			typ += ss[end]
		else:
			return None, None
		if end+1 <len(ss):
			if ss[end+1] <= '9' and ss[end+1] >='0':
				return None, None
			if ss[end+1] == '%':
				return None, None
		if beg>0:
			typ = ss[0] + typ
		return typ, nn

	def get_seq_beg(self, ss):
		'''
		是否是序列起始
		是: (序列类别，序列号）序列号为0，则为非数字序列
		否: (None, None)
		'''
		if len(ss) < 3:
			return None, None
		if ss[0] in self.seq2label:
			return self.seq2label[ss[0]], 0
		return self.seq_type(ss)


