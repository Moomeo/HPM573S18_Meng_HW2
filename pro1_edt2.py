#Week 2, HW 2 try another method
# #scac

Constant1 = 1.371
Constant2 = 0.371

alsit = ([1, 0.98, 0.89, 0.84, 0.75, 0.61],
         [1, 0.95, 0.89, 0.80, 0.74, 0.61],
         [1, 0.94, 0.89, 0.81, 0.68],
         [1, 0.93, 0.86, 0.73, 0.65, 0.58],
         [1, 0.95, 0.88, 0.76, 0.65, 0.56],
         [1, 0.95, 0.85, 0.64, 0.46],
         [1, 0.92, 0.95, 0.83, 0.60, 0.42],
         [1, 0.96, 0.90, 0.77, 0.55])

class HUI3:
    def __init__(self, level):
        self.level = level

    def cal_urility_score(self):
        num_level = len(self.level)
        u_sco = 1
        for i in range(num_level):
            lis_comp = alsit[i]
            u_sco *= lis_comp[int(self.level[i]-1)]
        u_sco = Constant1 * u_sco - Constant2
        return u_sco

myHUI3 = HUI3([2, 1, 1, 2, 1, 2, 1, 3])

print(myHUI3.cal_urility_score())