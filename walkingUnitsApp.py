#for walkingunitsapp
from Tkinter import *
import time
#for walkingunitsmodel
from linkedlist import LinkedList
from linkedqueue import LinkedQueue

class walkingUnitsApp(Frame):
	"""Creates a Frame for showing units moving along a path"""
	
	def __init__(self):
		"""initializes frame"""
		self._dataModel = walkingUnitsModel()
		self._inQueue = 0
		self._isDrawing = False
		
		Frame.__init__(self)
		self.master.title("Walking Units Simulator")
		self.master.resizable(0,0)
		self.grid()
		
		self._canvas = Canvas(width=500, height = 500)
		self._canvasImages = LinkedList()
		self._canvas.grid(row = 0, column = 0)
		
		self._unitImg = PhotoImage(file="unitsmall.gif")
		
		buttonframe = Frame()
		buttonframe.grid(row = 0, column = 1)
		
		enqueueButton = Button(buttonframe, text = "Queue a Unit", command = self._enqueue)
		enqueueButton.grid()
		
		dequeueButton = Button(buttonframe, text = "Start a Unit", command = self._dequeue)
		dequeueButton.grid()
		
		self._queueLabel = Label(buttonframe, text = "In Queue: " + str(self._inQueue))
		self._queueLabel.grid()
		
	def _enqueue(self):
		"""queues a unit in to be set on the path"""
		self._dataModel.makeUnit()
		self._inQueue += 1
		self._queueLabel.configure(text = "In Queue: " + str(self._inQueue))
		
	def _dequeue(self):
		"""sets a queued unit on the path"""
		if not self._inQueue == 0:
			self._dataModel.startUnit()
			self._inQueue -= 1
			self._queueLabel.configure(text = "In Queue: " + str(self._inQueue))
			
			self._canvasImages.add(self._canvas.create_image(500,500,image = self._unitImg))
			if self._isDrawing == False:
				self._isDrawing = True
				self._draw()
							
	def _draw(self):
		"""redraws the units"""
		if self._dataModel._movingUnits.head == None:
			self._isDrawing == False
		else:
			self._dataModel.moveAll()	
			canvasImageNode = self._canvasImages.head
			for unit in self._dataModel._movingUnits:
				self._canvas.move(canvasImageNode.data, -1, -1)
				canvasImageNode = canvasImageNode.next
			self._canvas.update()
			self.after(1, self._draw)
		
				
class walkingUnitsModel(object):
	def __init__(self):
		self._path = LinkedList()
		for i in range(500):
			self._path.add(Coordinate(i, i))
		self._movingUnits = LinkedList()
		self._queuedUnits = LinkedQueue()
		
	def makeUnit(self):
		self._queuedUnits.add(Unit(PhotoImage(file = "unitsmall.gif"), self._path.head))
		
	def startUnit(self):
		self._movingUnits.add(self._queuedUnits.pop())
		
	def __step(self, unit):
		if not unit._position == None:
			unit._position = unit._position.next
		
	def moveAll(self):
		for unit in self._movingUnits:
			self.__step(unit.data)
			if unit.data._position == None:
				self._movingUnits.remove(unit)
		
class Unit:
	def __init__(self, graphic, coordinate):
		self._graphic = graphic
		self._position = coordinate
		
	def getGraphic():
		return self._graphic
	
	def getPosition():
		return self._position
		
class Coordinate:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
		
		
def main():
	frame = walkingUnitsApp()
	frame.mainloop()
	
if __name__ == "__main__":
	main()