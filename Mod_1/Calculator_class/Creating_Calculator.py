
class Calculator:
    def __init__ (self, data):
        data.sort()
        self.data = data
        self.length = self._calc_length()
        self.mean = self._calc_mean()
        self.median = self._calc_median()
        self.variance = self._calc_variance()
        self.std_dev = self._calc_stand_dev()

    def _calc_mean(self):
        return(sum(self.data)/len(self.data))

    def _calc_length(self):
        return(len(self.data))

    def _calc_median(self):
        if len(self.data) % 2 == 0:
            mid_left = self.data[len(self.data) // 2 - 1]
            mid_right = self.data[len(self.data) // 2]
            avg = (mid_left + mid_right) / 2
        else:
            avg = self.data[len(self.data) // 2]
        return avg

    def _calc_variance(self):
        avg_x = (sum(self.data) / len(self.data))
        added_up = []
        for item in self.data:
            added_up.append((item - avg_x) ** 2)
        return (sum(added_up) / (len(self.data) - 1))

    def _calc_stand_dev(self):
        avg_x = (sum(self.data) / len(self.data))
        added_up = []
        for item in self.data:
            added_up.append((item - avg_x) ** 2)
        return ((sum(added_up) / (len(self.data) - 1))**0.5)
   #can also do standard deviation this way:
    # def _calc_stndev(self):
        #return math.sqrt(self.variance)

    def add_data(self,new_data):
        self.data.append(new_data)
        self.data.sort()
        self.update_data()

    def update_data(self):
        data.sort()
        self.data = data
        self.length = self._calc_length()
        self.mean = self._calc_mean()
        self.median = self._calc_median()
        self.variance = self._calc_variance()
        self.std_dev = self._calc_stand_dev()
        #self.data.data
        #self.data.length
        #self.data.mean
        #self.data.median
        #self.data.variance
        #self.data.stand_dev

    def remove_data(self,old_data):
        self.data.remove(old_data)
        self.data.sort()
        self.update_data()

### Everything below here just messing around to test things out


data_1 = Calculator([2,1,3,4,5,6,7,8,9,10])
print(data_1.data)
data_1.remove_data(7)
print(data_1.data)

#print(data_1.data)
#data_1.remove_data(8)
#print(data_1.data)
#print(data_1._calc_stndev())