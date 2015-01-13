import string



class ClusterSet(object):
    """ A ClusterSet is defined as a list of clusters """
    def __init__(self, pointType):
        """ Initialize an empty set, without any clusters """
        self.members = []
    def add(self, c):
        """ Append a cluster to the end of the cluster list
        only if it doesn't already exist. If it is already in the 
        cluster set, raise a ValueError """
        if c in self.members:
            raise ValueError
        self.members.append(c)
    def getClusters(self):
        return self.members[:]
    def mergeClusters(self, c1, c2):
        """ Assumes clusters c1 and c2 are in self
        Adds to self a cluster containing the union of c1 and c2
        and removes c1 and c2 from self """
        points =  c1.points
        for p2 in c2.points:
            if p2 not in points:
                points.append(p2)
        self.members.remove(c1)
        self.members.remove(c2)
        self.members.append(Cluster(points, City))
          
    def findClosest(self, linkage):
        """ Returns a tuple containing the two most similar 
        clusters in self
        Closest defined using the metric linkage """
        initialPair = False
    
        for i in range(0,len(self.members)):
            for j in range(i+1,len(self.members)):
                if initialPair == False:
                    dist = linkage(self.members[i],self.members[j])
                    closestPair = [(self.members[i],self.members[j]),dist]
                    initialPair = True
                else:
                    dist = linkage(self.members[i],self.members[j])
                    if dist < closestPair[1]:
                        closestPair = [(self.members[i],self.members[j]),dist]
        return closestPair[0]          
        
    def mergeOne(self, linkage):
        """ Merges the two most similar clusters in self
        Similar defined using the metric linkage
        Returns the clusters that were merged """
        clusterToMerge = self.findClosest(linkage)
        self.mergeClusters(clusterToMerge[0],clusterToMerge[1])
        return clusterToMerge
        
    def numClusters(self):
        return len(self.members)
    def toStr(self):
        cNames = []
        for c in self.members:
            cNames.append(c.getNames())
        cNames.sort()
        result = ''
        for i in range(len(cNames)):
            names = ''
            for n in cNames[i]:
                names += n + ', '
            names = names[:-2]
            result += '  C' + str(i) + ':' + names + '\n'
        return result