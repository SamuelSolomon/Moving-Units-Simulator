# walkingUnitsApp
This is an app that simulates a set of units walking across a coordinate field according to a set of program defined coordinate values.\
The main() class is located in the walkingUnitsApp file, as well as the bulk of the class files. The user can press a button to make a unit for the queue and then press another button to send that unit along a path from the queue.\
All the other files in this project are utilities used in the walkingUnitsApp. Except for the Planning.txt file, that was my initial plan for how the program needed to be structured.
## Synopsis
The project uses linked lists to organize data, and the data classes are seperated from the GUI classes, any class with the basic information of a unit should be useable within the data model and could be accessed with a proper GUI class.

## The Data Model
This is the data model for the walking units, it provides a simple way of keeping track of and updating a list of objects designed to be on a XY coordinate field.

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

## Motivation
This project exists to help me understand how to work with lists of objects and handle them in a way that is computationally simple. It is one more step towards creating bigger and more elaborate programs that I can make a living off of. I completed it as a Final Project for a python course focusing on GUI's and data structures. In time I will need to revisit this project to refine the datahandling system, so please feel free to contribute.

### Problems to fix
1. Memory management: the program continually allocates memory, this likely occurs because the draw() method in the walkingUnitsApp file never shuts down as it is supposed to. a way to fix it would be seperate the calls to draw to a level above in terms of how the code runs.
2. Units are not removed correctly from the list of walking units, this contributes to the memory management problem.
3. Path Class: A more flexible path class would need to be made if this were to be used in a professional program.
4. The App does not reference the actual values contained in the units path position to determine where it is drawn.
