from __future__ import division
import scipy.stats

INDEPENDENT_VARIABLES_AMOUNT=27
DRAWING_AMOUNT=14
ITEMS_IN_DRAW_AMOUNT=10

class AverageItem(object):
    def __init__(self,i,orderNumber=0):
        self.id=i
        self.average=0
        self.orderNumber=orderNumber

    def __repr__(self):
        return str(self.orderNumber)

class Thurstone(object):
    """def initialize_array(self,size):
        return [0 for i in range(size)]

    """
    def test_data(self):
        return [[8, 3, 3, 4, 4, 4, 2, 2, 2, 3, 4, 2, 3, 2, 2, 2, 3, 3, 1, 3, 2, 2, 2, 4, 3, 3, 4, 2],
                [6, 3, 5, 5, 5, 5, 3, 3, 4, 3, 4, 4, 5, 5, 5, 5, 4, 4, 2, 2, 4, 2, 1, 3, 4, 4, 2, 3],
                [7, 4, 3, 5, 4, 5, 2, 2, 1, 5, 5, 4, 5, 4, 1, 4, 4, 5, 5, 4, 3, 1, 4, 2, 5, 4, 5, 5],
                [8, 4, 4, 5, 5, 5, 3, 4, 3, 2, 4, 5, 5, 3, 5, 3, 5, 5, 4, 5, 3, 4, 3, 2, 5, 4, 3, 2],
                [5, 2, 2, 2, 2, 1, 3, 1, 1, 2, 1, 4, 4, 3, 1, 1, 4, 3, 1, 1, 1, 1, 1, 4, 4, 4, 4, 1],
                [6, 2, 3, 3, 2, 2, 2, 1, 1, 1, 4, 3, 4, 3, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 3, 2, 1, 1],
                [6, 3, 4, 4, 4, 3, 1, 1, 5, 3, 3, 5, 4, 3, 2, 1, 3, 3, 2, 3, 1, 5, 1, 2, 2, 2, 1, 1],
                [3, 3, 4, 3, 4, 5, 3, 3, 3, 4, 4, 4, 5, 2, 5, 2, 3, 3, 2, 3, 2, 2, 1, 3, 4, 4, 3, 1],
                [5, 2, 2, 5, 5, 3, 2, 1, 5, 2, 3, 5, 4, 2, 1, 1, 3, 1, 2, 2, 2, 1, 1, 2, 1, 1, 1, 2],
                [7, 3, 3, 3, 2, 2, 1, 1, 2, 3, 2, 2, 4, 4, 3, 2, 2, 3, 3, 4, 3, 2, 3, 3, 4, 3, 4, 1],]

    def orderNumber_test_data(self):
        test_data=[[27, 21, 23, 17, 13, 10, 3, 1, 19, 22, 18, 26, 25, 2, 7, 24, 14, 9, 12, 11, 5, 8, 16, 20, 15, 4, 6],
                [20, 19, 27, 24, 25, 7, 1, 9, 14, 26, 22, 23, 16, 8, 3, 17, 12, 4, 13, 10, 6, 2, 11, 21, 18, 15, 5],
                [22, 5, 24, 21, 26, 11, 6, 15, 25, 18, 20, 23, 14, 1, 9, 12, 13, 3, 4, 16, 7, 27, 19, 8, 2, 10, 17],
                [6, 12, 9, 19, 20, 1, 14, 17, 10, 21, 22, 27, 23, 24, 13, 16, 3, 11, 15, 2, 8, 4, 25, 26, 18, 5, 7],
                [2, 8, 22, 24, 25, 4, 15, 17, 16, 26, 23, 27, 6, 19, 11, 7, 13, 9, 18, 12, 5, 10, 20, 21, 3, 14, 1],
                [2, 11, 17, 22, 21, 18, 3, 7, 10, 25, 19, 27, 26, 20, 4, 9, 13, 15, 24, 8, 5, 1, 23, 14, 12, 16, 6],
                [10, 9, 15, 7, 24, 25, 19, 8, 17, 14, 20, 27, 23, 2, 26, 22, 3, 6, 13, 11, 12, 21, 18, 16, 5, 4, 1],
                [24, 16, 27, 25, 21, 18, 3, 8, 19, 22, 26, 23, 13, 4, 15, 17, 11, 6, 14, 7, 9, 20, 10, 12, 5, 1, 2],
                [7, 8, 15, 24, 22, 14, 16, 17, 11, 25, 23, 27, 18, 5, 6, 20, 19, 2, 9, 13, 12, 3, 21, 26, 10, 1, 4],
                [20, 15, 17, 21, 26, 19, 1, 13, 23, 18, 25, 27, 24, 8, 2, 22, 5, 11, 12, 9, 6, 3, 14, 16, 10, 4, 7],
                [15, 9, 21, 24, 26, 11, 2, 13, 12, 18, 25, 27, 23, 8, 14, 20, 16, 6, 4, 7, 10, 5, 19, 22, 17, 1, 3],
                [19, 13, 14, 23, 21, 10, 2, 11, 8, 20, 26, 24, 22, 5, 16, 27, 3, 9, 17, 18, 7, 1, 15, 25, 12, 6, 4],
                [23, 26, 19, 21, 13, 9, 8, 6, 16, 22, 18, 24, 17, 1, 3, 25, 11, 12, 20, 10, 7, 5, 14, 27, 15, 2, 4],
                [1, 15, 12, 18, 23, 2, 7, 10, 8, 17, 20, 27, 25, 16, 14, 22, 3, 5, 9, 24, 11, 4, 19, 26, 21, 6, 13]]
        return [[AverageItem(0,test_data[j][i]) for i,item in enumerate(row)] for j,row in enumerate(test_data)]

    def initialize_matrix(self,xSize,ySize=1):
        return [[0 for x in range(xSize)] for y in range(ySize)] if ySize!=1 else [0 for x in range(xSize)]
    def initialize_averages_matrix(self):
        return [[AverageItem(i) for i in range(1,self.xSizeAveragesMatrix+1)] for y in range(self.ySizeAveragesMatrix)]
    def display_matrix(self,matrix):
        for row in matrix:
            print row
        print

    def display_averages_matrix(self):
        for row in self.averagesMatrix:
            print row

    def input_data(self):
        pass
    def draw(self):
        pass

    def __init__(self):
        self.xSizeDrawingMatrix= INDEPENDENT_VARIABLES_AMOUNT + 1
        self.ySizeDrawingMatrix=ITEMS_IN_DRAW_AMOUNT
        self.drawingMatrix=self.initialize_matrix(self.xSizeDrawingMatrix, self.ySizeDrawingMatrix)
        self.xSizeAveragesMatrix=INDEPENDENT_VARIABLES_AMOUNT
        self.ySizeAveragesMatrix=DRAWING_AMOUNT
        self.averagesMatrix=self.initialize_averages_matrix()
        self.currentAveragesMatrixRow=0
        self.zValuesMatrix=self.initialize_matrix(INDEPENDENT_VARIABLES_AMOUNT,INDEPENDENT_VARIABLES_AMOUNT)
        self.weights=[]


# BEGIN OF STEP 1 COMPUTATIONS
    def compute_averages_and_ratio(self):
        averages=self.initialize_matrix(self.xSizeDrawingMatrix)
        for column in range(0, self.xSizeDrawingMatrix):
            averages[column]=(sum(row[column] for row in self.drawingMatrix))/self.ySizeDrawingMatrix

        for row in self.drawingMatrix:
            for i,item in enumerate(row):
                row[i]=row[i]/averages[i]

    def compute_deltas(self):
        for row in self.drawingMatrix:
            for i,item in enumerate(row):
                if i!=0:
                    row[i]=abs(row[i]-row[0])

    def compute_gammas(self):
        maxvalue= max([max(row[1:]) for row in self.drawingMatrix])
        minvalue= min([min(row[1:]) for row in self.drawingMatrix])

        for row in self.drawingMatrix:
            for i,item in enumerate(row):
                if i!=0:
                    row[i]=(minvalue+(0.5*maxvalue))/(row[i]+(0.5*maxvalue))

    def compute_averages(self):
        for column in range(1, self.xSizeDrawingMatrix):
            self.averagesMatrix[self.currentAveragesMatrixRow][column-1].average=(sum(row[column] for row in self.drawingMatrix))/self.ySizeDrawingMatrix

    def order_averages(self):
        for row in self.averagesMatrix:
            sortedList=sorted(row,key=lambda x:x.average)
            for i,item in enumerate(sortedList):
                row[sortedList[i].id-1].orderNumber=i+1


# END OF STEP 1 COMPUTATIONS


# BEGIN OF STEP 2 COMPUTATIONS

    def compute_greater_ratio(self):
        self.averagesMatrix=self.orderNumber_test_data() # TUTAJ ZMIENIANE SA DANE BY MOGLY BYC TESTOWANE, KONIECZNA ZMIANA NA PRODUKCJI
        for j,row in enumerate(self.zValuesMatrix):
            for i,item in enumerate(row):
                licznik=0
                for averagesRow in self.averagesMatrix:
                    licznik=licznik+1 if averagesRow[j].orderNumber<averagesRow[i].orderNumber else licznik
                row[i]=licznik/DRAWING_AMOUNT

    def compute_zValuesMatrix(self):
        for row in self.zValuesMatrix:
            for i,item in enumerate(row):
                row[i]=scipy.stats.norm(0, 1).cdf(row[i])-0.5

    def compute_weights(self):
        self.weights=[(sum(row[i] for row in self.zValuesMatrix)/INDEPENDENT_VARIABLES_AMOUNT) for i,item in enumerate(self.zValuesMatrix[0])]
        minvalue=min(self.weights)
        maxvalue=max(self.weights)
        self.weights=[(item-minvalue)/(maxvalue-minvalue)+1 for item in self.weights]

# END OF STEP 2 COMPUTATIONS

    def step1(self):
        for i in range(DRAWING_AMOUNT):
            #self.drawData()
            self.compute_averages_and_ratio()
            self.compute_deltas()
            self.compute_gammas()
            self.compute_averages()
            self.currentAveragesMatrixRow=self.currentAveragesMatrixRow+1
        self.order_averages()

    def step2(self):
        self.compute_greater_ratio()
        self.compute_zValuesMatrix()
        self.compute_weights()

    def get_weights(self):
        self.input_data()
        self.step1()
        self.step2()
        return self.weights

class FunctionItem(object):
    def __init__(self,id,value):
        self.id=id
        self.value=value

    def __repr__(self):
        return str(self.value)

class GroupSum(object):
    def __init__(self,id,sum):
        self.id=id
        self.sum=sum

    def __repr__(self):
        return str(self.sum)


class GreyStatistics(object):

    def __init__(self):
# NALEZY ZMIENIC PONIZSZA LINIE W PRODUKCJI
        #self.weights=[1.4657428013262215, 1.4163249754726168, 1.6843749718347434, 1.7770940271427662, 1.8300274532931691, 1.3116041237882821, 1.084495684627417, 1.2792538602216039, 1.4925389089860017, 1.7863704870915869, 1.8331998828613862, 2.0, 1.7298595679753663, 1.1735379323945843, 1.2528613319754356, 1.6803569182014886, 1.2332299460635296, 1.1108476257115703, 1.4006840485678369, 1.3032769715379329, 1.118077099607764, 1.14399697653501, 1.6093807314276036, 1.7455372652971093, 1.3219316524318421, 1.039350923383928, 1.0] # NALEZY ZMIENIC TE LINIJKE NA PRODUKCJI\
        self.weights=[1.4651194211, 1.4112710732, 1.6826295168, 1.7896056325, 1.8315493973, 1.30935403, 1.0783780944, 1.2777986279, 1.4955489169, 1.7839911128, 1.8372840136, 2, 1.7342560761, 1.1717982976, 1.2544698482, 1.6818939246, 1.2301052347, 1.1078618288, 1.3985408254, 1.3031840632, 1.1161334875, 1.1423145632, 1.6109318001, 1.7432783391, 1.307222314, 1.036329245, 1]
        self.groupsAmount=4
        self.highestSurveyGrade=10
        self.groupsThreshold=self.highestSurveyGrade/self.groupsAmount
        self.survey=self.test_survey()
        self.functions=self.compute_functions()

    def test_survey(self):
        return [8, 6, 10, 8, 10, 4, 4, 2, 10, 10, 8, 10, 8, 2, 8, 8, 10, 10, 8, 6, 2, 8, 4, 10, 8, 10, 10]
    def compute_functions(self):
        return [[FunctionItem(id,(item/(self.groupsThreshold*i) if item <= (self.groupsThreshold*i) else (10-item)/(self.groupsThreshold*(self.groupsAmount-i)))*self.weights[id]) for id,item in enumerate(self.survey)] for i in range(1,self.groupsAmount+1)]
    def choose_group(self):
        return max([GroupSum(i+1,sum(item.value for item in function)) for i,function in enumerate(self.functions)],key=lambda x:x.sum).id
    def most_important_criteria(self):
        return sorted(self.functions[self.choose_group()-1],key=lambda x:x.value,reverse=True)[0:4]

obiekt = Thurstone()
obiekt.drawingMatrix=obiekt.test_data()
obiekt.get_weights()
#obiekt.display_matrix(obiekt.averagesMatrix)
#obiekt.display_matrix(obiekt.zValuesMatrix)
#obiekt.display_matrix(obiekt.weights)

stat=GreyStatistics()
#print stat.compute_functions()
print stat.choose_group()
print stat.most_important_criteria()