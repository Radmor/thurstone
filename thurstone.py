from __future__ import division

INDEPENDENT_VARIABLES_AMOUNT=27
DRAWING_AMOUNT=14
ITEMS_IN_DRAW_AMOUNT=10

class average_item(object):
    def __init__(self):
        self.id
        self.average
        self.orderNumber

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

    def initialize_matrix(self,xSize,ySize=1):
        return [[0 for x in range(xSize)] for y in range(ySize)] if ySize!=1 else [0 for x in range(xSize)]
    def display_matrix(self,matrix):
        for row in matrix:
            print row
        print

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
        self.averagesMatrix=self.initialize_matrix(self.xSizeAveragesMatrix,self.ySizeAveragesMatrix)
        self.currentAveragesMatrixRow=0
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
            self.averagesMatrix[self.currentAveragesMatrixRow][column-1]=(sum(row[column] for row in self.drawingMatrix))/self.ySizeDrawingMatrix


    def step1_computations(self):
        self.compute_averages_and_ratio()
        self.compute_deltas()
        self.compute_gammas()
        self.compute_averages()

    def step1(self):
        for i in range(DRAWING_AMOUNT):
            #self.drawData()
            self.step1_computations()

            self.currentAveragesMatrixRow=self.currentAveragesMatrixRow+1


obiekt=Thurstone()
obiekt.drawingMatrix=obiekt.test_data()
obiekt.step1()
obiekt.display_matrix(obiekt.averagesMatrix)