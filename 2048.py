#coding = utf-8

import random

data = [
    
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    
]


line_num = [0, 1, 2, 3]

########################################################################
class main:
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        #super(main, self).__init__(self)
        self.init_display()
        
        if self.x1 == self.x2 and self.y1 == self.y2:
            self.init_display()
            #print 'again'
            
    #----------------------------------------------------------------------
    def display(self):        
        """显示界面"""
        print '{0:4} {1:4} {2:4} {3:4}'.format(data[0][0], data[0][1], data[0][2], data[0][3])
        print '{0:4} {1:4} {2:4} {3:4}'.format(data[1][0], data[1][1], data[1][2], data[1][3])
        print '{0:4} {1:4} {2:4} {3:4}'.format(data[2][0], data[2][1], data[2][2], data[2][3])
        print '{0:4} {1:4} {2:4} {3:4}'.format(data[3][0], data[3][1], data[3][2], data[3][3])
        print '------------------------'
        
    #----------------------------------------------------------------------
    def init_display(self):
        """初始化显示数据"""
        self.x1 = random.choice((0, 1, 2, 3))
        self.x2 = random.choice((0, 1, 2, 3))
        #print self.x1, self.x2
        
        self.y1 = random.choice((0, 1, 2, 3))
        self.y2 = random.choice((0, 1, 2, 3))
        #print self.y1, self.y2
        
        data[self.x1][self.y1] = random.choice((2, 2, 2, 2, 2, 4))
        data[self.x2][self.y2] = random.choice((2, 2, 2, 2, 2, 4))
        #data[i] = [random.choice([0, 0, 0, 2, 2]) for x in range(0, 4)]
        
    
    #----------------------------------------------------------------------
    def init_data(self):
        """在屏幕上的空格子处随机产生一个数字2或者4"""
        while True:
            x = random.choice(line_num)
            y = random.choice(line_num)
            if data[x][y] == 0:
                data[x][y] = random.choice((2, 2, 2, 2, 2, 4))
                #print 'ok', data[x][y], x, y
                break
            else:
                pass
        
    #----------------------------------------------------------------------
    def score_sum(self):
        """计算分数，分数为所有格子的数值总和"""
        self.score = 0
        for x in range(0, 4):
            for y in range(0, 4):
                self.score += data[x][y]
                if data[x][y] == 2048:
                    print 'You win!'
                    
        print 'score is {0:3}'.format(self.score)
        print '------------------------'
        
    
    
    #----------------------------------------------------------------------
    def left(self):
        """左移"""
        for i in line_num:
            
            for x in range(data[i].count(0)):
                data[i].remove(0)

            zeros = [0 for x in range(4 - len(data[i]))]
            #print zeros
            data[i].extend(zeros)
            #print data[i]
            
        for i in line_num:
            for x in line_num:
                if x == 3:
                    if data[i][x] == data[i][x - 1]:
                        if data[i][x] != 0 and data[i][x - 1] != 0:
                            data[i][x] = data[i][x] * 2
                            data[i][x + 1] = 0
                            #print x
                            break
                
                else:
                    if data[i][x] == data[i][x + 1]:
                        if data[i][x] != 0:
                            data[i][x] = data[i][x] * 2
                            data[i][x + 1] = 0
                            #print x
                            break
                        
        for i in line_num:
            
            for x in range(data[i].count(0)):
                data[i].remove(0)

            zeros = [0 for x in range(4 - len(data[i]))]
            #print zeros
            data[i].extend(zeros)
            #print data[i]


    #----------------------------------------------------------------------
    def right(self):
        """右移"""
        for i in line_num:
            #print i
            for x in range(data[i].count(0)):
                data[i].remove(0)

            zeros = [0 for x in range(4 - len(data[i]))]
            #print zeros
            data[i][:0] = zeros
            #print data[i]
            
        for i in line_num:
            for x in line_num:
                if x == 3:
                    if data[i][x] == data[i][x - 1]:
                        if data[i][x] != 0 and data[i][x - 1] != 0:
                            data[i][x] *= 2
                            data[i][x - 1] = 0
                            #print x
                            break
                
                else:
                    if data[i][x] == data[i][x + 1]:
                        if data[i][x] != 0:
                            data[i][x + 1] *= 2
                            data[i][x] = 0
                            #print x
                            break

        for i in line_num:
            #print i
            for x in range(data[i].count(0)):
                data[i].remove(0)

            zeros = [0 for x in range(4 - len(data[i]))]
            #print zeros
            data[i][:0] = zeros
            #print data[i]

            
    #----------------------------------------------------------------------
    def up(self):
        """上移"""
        global data
        temp = map(list, zip(*data))
        
        for i in line_num:
                    
            for x in range(temp[i].count(0)):
                temp[i].remove(0)

            zeros = [0 for x in range(4 - len(temp[i]))]
            #print zeros
            temp[i].extend(zeros)
            #print temp[i]
            
        for i in line_num:
            for x in line_num:
                if x == 3:
                    if temp[i][x] == temp[i][x - 1]:
                        if temp[i][x] != 0 and temp[i][x - 1] != 0:
                            temp[i][x] = temp[i][x] * 2
                            temp[i][x + 1] = 0
                            #print x
                            break
                
                else:
                    if temp[i][x] == temp[i][x + 1]:
                        if temp[i][x] != 0:
                            temp[i][x] = temp[i][x] * 2
                            temp[i][x + 1] = 0
                            #print x
                            break
        
        for i in line_num:
                    
            for x in range(temp[i].count(0)):
                temp[i].remove(0)

            zeros = [0 for x in range(4 - len(temp[i]))]
            #print zeros
            temp[i].extend(zeros)
            #print temp[i]

        data = map(list, zip(*temp))

        
    #----------------------------------------------------------------------
    def down(self):
        """下移"""
        global data
        temp = map(list, zip(*data))
        
        for i in line_num:
                    
            for x in range(temp[i].count(0)):
                temp[i].remove(0)

            zeros = [0 for x in range(4 - len(temp[i]))]
            #print zeros
            temp[i][:0] = zeros
            #print temp[i]
            
        for i in line_num:
            for x in line_num:
                if x == 3:
                    if temp[i][x] == temp[i][x - 1]:
                        if temp[i][x] != 0 and temp[i][x - 1] != 0:
                            temp[i][x + 1] *= 2
                            temp[i][x] = 0
                            #print x
                            break
                
                else:
                    if temp[i][x] == temp[i][x + 1]:
                        if temp[i][x] != 0:
                            temp[i][x + 1] *= 2
                            temp[i][x] = 0
                            #print x
                            break
        
        for i in line_num:
                    
            for x in range(temp[i].count(0)):
                temp[i].remove(0)

            zeros = [0 for x in range(4 - len(temp[i]))]
            #print zeros
            temp[i][:0] = zeros
            #print temp[i]

        data = map(list, zip(*temp))        


    #----------------------------------------------------------------------
    def test(self):
        """"""
        self.display()
        #self.score_sum()
        #self.init_data()
        #self.display()
        #self.score_sum()
        
        while True:
            
            ch = raw_input('input:')
            
            if ch == 'w':
                self.up()
                self.init_data()
                self.display()
                self.score_sum()
                
            if ch == 's':
                self.down()
                self.init_data()
                self.display()
                self.score_sum()
                
            if ch == 'a':
                self.left()
                self.init_data()
                self.display()
                self.score_sum()
                
            if ch == 'd':
                self.right()
                self.init_data()
                self.display()
                self.score_sum()
                
            if ch == 'q':
                break
            
if __name__ == '__main__':
    
    ex = main()
    ex.test()
