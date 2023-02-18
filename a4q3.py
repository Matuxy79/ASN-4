#John Matukutire
#11303324
#CMPT 145 CRN 27177
#L16


#importing mode for use later
from statistics import mode

class Statistics(object):
    def __init__(self):
        """
        Purpose:
            Initialize a Statistics object instance.
        """
        self.values =[]

    def add(self, value):
        """
        Purpose:
            Use the given value in the calculation of mean and 
            variance.
        Pre-Conditions:
            :param value: the value to be added
        Post-Conditions:
            none
        Return:
            :return none
        """
        self.values.append(value)

    def mean(self):
        """
        Purpose:
            Return the average of all the values seen so far.
        Post-conditions:
            (none)
        Return:
            The mean of the data seen so far.
        """
        if not self.values:
            return None
        return sum(self.values) / len(self.values)

    def count(self):
        """
        Purpose:
            Return the number of values seen so far.
        Post-conditions:
            (none)
        Return:
            The number of values seen so far.
        """
        return len(self.values)

    def get_min(self):
        """
        Purpose:
            Return the smallest out of the values seen so far.
        Post-conditions:
            (none)
        Return:
            The smallest out of the values seen so far.
        """        
        if not self.values:
            return None
        return min(self.values)

    def get_max(self):
        """
        Purpose:
            Return the largest out of the values seen so far.
        Post-conditions:
            (none)
        Return:
            The largest out of the values seen so far.
        """         
        if not self.values:
            return None
        return max(self.values)

    def get_range(self):
        """Purpose:
            Return the range of the values seen so far.
        Post-conditions:
            (none)
        Return:
            The range of the values seen so far.
        """            
        if not self.values:
            return None
        return self.get_max() - self.get_min()

    def get_mode(self):
        """Purpose:
            Return the mode of the values seen so far.
        Post-conditions:
            (none)
        Return:
            The mode of the values seen so far.
        """        
        if not self.values:
            return None
        return mode(self.values)