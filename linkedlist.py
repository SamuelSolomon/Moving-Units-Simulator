
from node import Node

class LinkedList :
	def __init__( self ) :
		self.head = None		

	def add( self, data ) :
		node = Node( data )
		if self.head == None :	
			self.head = node
		else :
			node.next = self.head
			node.next.prev = node						
			self.head = node			

	def __iter__(self):
		"""Supports iteration over a view of self."""
		node = self.head
		while not node == None:
			yield node
			node = node.next

	def search( self, k ) :
		p = self.head
		if p != None :
			while p.next != None :
				if ( p.data == k ) :
					return p				
				p = p.next
			if ( p.data == k ) :
				return p
		return None

	def remove( self, p ) :
		if not p == None:
			tmp = p.prev
			if not p.prev == None:
				p.prev.next = p.next
				p.prev = tmp		

	def __str__( self ) :
		s = ""
		p = self.head
		if p != None :		
			while p.next != None :
				s += p.data
				p = p.next
			s += p.data
		return s