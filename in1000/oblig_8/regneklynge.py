from exceptions import ClusterMisconfiguration
from node import Node
from rack import Rack
from pathlib import Path


## Class that describes a cluster with racks and nodes
#
class Regneklynge:
    ## Create an empty cluster
    # @param arg can be integer or settings file
    def __init__(self, arg):
        self._racks = []
        self._input_file = None
        if isinstance(arg, int):
            self._nodes_per_rack = arg
        elif isinstance(arg, str) and Path(arg).is_file():
            self._input_file = Path(arg)
            self._load_config(self._input_file)
        else:
            raise ClusterMisconfiguration

    def __str__(self):
        return 'Regneklynge. Racks: {}. CPUs: {}.'.format(self.antRacks(), self.antProsessorer())

    def _load_config(self, file):
        with open(file, 'r') as input_file:
            self._nodes_per_rack = int(input_file.readline())
            for line in input_file:
                args = line.split()
                for _ in range(int(args[0])):
                    self.settInnNode(Node(int(args[1]), int(args[2])))

    ## Inserts a node in a rack with free space or creates a new rack and places it there.
    # @param node reference to the node that should be inserted
    def settInnNode(self, node):
        # Alternatively we can initiate the racks list with 1 empty node and avoid repeating 1st
        # check in the following expression
        if len(self._racks) == 0 or self._racks[-1].getAntNoder() == self._nodes_per_rack:
            self._racks.append(Rack())
        self._racks[-1].settInn(node)

    ## Calculates the total number of processor in the cluster
    # @return total number of processors
    def antProsessorer(self):
        return sum([rack.antProsessorer() for rack in self._racks])

    ## Calculate the number of nodes in the cluster with enough memory
    # @param requiredmem size of required memory in GB
    # @return the number of nodes that meet the requirement
    def noderMedNokMinne(self, requiredmem):
        return sum(rack.noderMedNokMinne(requiredmem) for rack in self._racks)

    ## Returns the number of racks in the cluster
    # @return the number of racks
    def antRacks(self):
        return len(self._racks)
