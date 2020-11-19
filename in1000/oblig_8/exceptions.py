## Exception is raised in case of CPU misconfiguration
# @return custom message
class LimitCPUs(Exception):
    def __str__(self):
        return 'Node accepts 2 CPUs max.'


## Exception is raised in case if non-Node argument is passed where Node is expected
# @return custom message
class NotANode(Exception):
    def __str__(self):
        return 'Only nodes can be put in a rack.'


## Exception is raised in case if non-Node argument is passed where Node is expected
# @return custom message
class ClusterMisconfiguration(Exception):
    def __str__(self):
        return 'Provide either nodes per rack (int) or config file.'


