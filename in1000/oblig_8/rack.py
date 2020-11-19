from node import Node
from exceptions import NotANode


## Rack class that holds nodes
#
class Rack:
    ## Creates the rack that can store nodes
    #
    def __init__(self):
        self._nodes = []

    def __str__(self):
        return 'Rack. Nodes: {}. Processors: {}.'.format(self.getAntNoder(), self.antProsessorer())

    ## Add a new node in the rack
    #  @param node accepts an instance of Node
    def settInn(self, node):
        if isinstance(node, Node):
            self._nodes.append(node)
        else:
            raise NotANode()

    ## Returns the number of nodes in the rack
    # @return antall noder
    def getAntNoder(self):
        return len(self._nodes)

    ## Calculates the number of processors in the nodes of the rack
    # @return number of processors
    def antProsessorer(self):
        return sum([node.antProsessorer() for node in self._nodes])

    ## Calculates the number of nodes with enough memory
    # @param requiredmem size of required memory in GB
    # @return the number of nodes that meet the requirement
    def noderMedNokMinne(self, requiredmem):
        return len([node for node in self._nodes if node.nokMinne(requiredmem)])
