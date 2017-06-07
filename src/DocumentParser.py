#!/usr/bin/env python2
#-*- coding:utf-8 -*-

from __future__ import unicode_literals

from SegmentParser import SegmentParser

class DocNode(object):
	"""将整个文档视为一个tree,每一个部分是这个tree上的一个节点。
	"""
	
	def __init__(self,node_type = None):
		"""
		"""
		self.__type__ = node_type
		self.__content__ = None
		self.__meta_data__ = None

		self.__child_node__ = []  #子节点，多个
		self.__parent_node__ = None #父节点，一个

	@property	
	def type(self):
		return self.__type__

	@property
	def content(self):
		return self.__content__

	@content.setter
	def content(self,content):
		self.__content__ = content

	@property
	def set_meta_data(self,meta_data):
		self.__meta_data = meta_data

	def add_child_node(self,doc_node):
		"""增加孩子节点。no-thread-safety
		"""
		assert isinstance(doc_node,DocNode)
		self.__child_node__.append(doc_node)
	
	def set_parent_node(self,doc_node):
		"""设置父亲节点。
		"""
		assert isinstance(doc_node,DocNode)
		self.__parent_node__ = doc_node

DocTree = DocNode

class DocumentParser(object):
	"""Document Parser
	"""
	def __init__(self):
		"""
		"""
		self.seg_parser = SegmentParser()
	
	def parse_content_block_list(self,content_block_list):
		"""parse content-block list
		   Parameters:
			content_block_list : [{'content':"..",},{'content':"..."},]
		   Return:
		   	DocTree
		"""
		root_node = DocTree()
		last_node = root_node
		for index,content_block in enumerate(content_block_list):
			content = content_block.get("content")
			if content is None:
				continue
			doc_node = DocNode()
			doc_node.set_content(content)
			seq_type,seq_id = self.seg_parser.get_seq_beg(content)
			doc_node.set_type(seq_type)
			
			if seq_type != last_node.
				








