import numpy as np

class Doors():
    def __init__(self):
        self.env = np.zeros((3))
        self.win_idx = self.rand()
        self.env[self.win_idx] = 1
        self.first_choice_idx = self.rand()
        self.render()
        self.wrong_idx = self.tell_the_wrong_door()
        self.switch()
    
    def rand(self):
        return np.random.randint(0, self.env.shape[0])
        
    def tell_the_wrong_door(self):
        miss_idx = self.rand()
        while miss_idx == self.win_idx or \
            miss_idx == self.first_choice_idx:
            miss_idx = self.rand()
        return miss_idx

    def switch(self):
        for i in range(self.env.shape[0]):
            if i != self.first_choice_idx and i != self.wrong_idx:
                self.switched_idx = i

    def render(self):
        d = [None, None, None]

        for i in range(self.env.shape[0]):
            if self.win_idx == self.first_choice_idx:
                if i == self.win_idx:
                    d[i] = "W 1 "
                else:
                    d[i] = "    "
            else:
                if i == self.win_idx:
                    d[i] = "Win "
                elif i == self.first_choice_idx:
                    d[i] = "1st "
                else:
                    d[i] = "    "
            

        print(" ______  ______  ______")
        print("|      ||      ||      |")
        print("| {} || {} || {} |".format(d[0], d[1], d[2]))
        print("|      ||      ||      |")
        print(" ------  ------  ------")
        

test_num = 10
stick_win_counter = 0
switch_win_counter = 0
for i in range(test_num):
    doors = Doors()
    # print("win idx",doors.win_idx)
    # print("first choice",doors.first_choice_idx)
    # print("wrong door",doors.tell_the_wrong_door())
    # print("Stick:", doors.first_choice_idx)
    # print("Swtich:", doors.switched_idx )
    if doors.first_choice_idx == doors.win_idx:
        stick_win_counter += 1
    if doors.switched_idx == doors.win_idx:
        switch_win_counter += 1

print("Stick win ratio: {}%, Switch win ratio: {}%".format(
    stick_win_counter/float(test_num)*100,
    switch_win_counter/float(test_num)*100
))
