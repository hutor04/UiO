from exceptions import LimitCPUs


## Class that represents nodes
#
class Node:
    ## Create new node with given memory size and number of CPUs
    #  @param memory GB in node (int)
    #  @param cpus number of CPUs in the node, max 2
    def __init__(self, memory, cpus):
        max_cpus = 2
        if isinstance(memory, int) and isinstance(cpus, int):
            self._memory = memory
            if cpus <= max_cpus:
                self._cpus = cpus
            else:
                raise LimitCPUs
        else:
            raise TypeError('Class Node accepts only integers.')

    def __str__(self):
        return 'Node. Memory: {}. CPUs: {}.'.format(self._memory, self._cpus)

    ## Return the number of CPUs in the node
    #  @return number of CPUs in the node
    def antProsessorer(self):
        return self._cpus

    ## Check if the node has enough memory for the program
    #  @param requiredmem size of required memory in GB
    #  @return True if the node has minimum this amount of memory
    def nokMinne(self, requiredmem):
        if requiredmem <= self._memory:
            return True
        else:
            return False
