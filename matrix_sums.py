class MatrixPosistion(object):
    def __init__(self,i,j):
        self.i = i
        self.j = j

class MatrixSums(object):
    def __init__(self):
        self.sums_matrix = None
        self.rows = 0
        self.columns = 0

    def sum(self, pos_a,pos_b):
        pos_b_sum = self.get_cell_value(pos_b)
        left_mat_sum = self.get_cell_value(MatrixPosistion(pos_b.i, pos_a.j-1))
        top_mat_sum = self.get_cell_value(MatrixPosistion(pos_a.i-1,pos_b.j))
        corner_mat_sum = self.get_cell_value(MatrixPosistion(pos_a.i-1, pos_a.j-1))

        return pos_b_sum - left_mat_sum - top_mat_sum + corner_mat_sum

    def get(self, pos_a):
        return self.sum(pos_a, pos_a)

    def set(self,pos,val):
        original_set_value = self.get(pos)
        diff = val - original_set_value
        for i in range(pos.i,self.rows):
            for j in range(pos.j,self.columns):
                self.sums_matrix[i][j] += diff

    def init_sums_matrix(self, base_matrix):
        self.rows = len(base_matrix)
        self.columns = len(base_matrix[0])
        self.sums_matrix = []
        for i in range(0,self.rows):
            self.sums_matrix.append(list())
            for j in range(0,self.columns):
                self.sums_matrix[i].append(0)

        for i in range(self.rows-1,-1,-1):
            for j in range(self.columns-1,-1,-1):
                self.set(MatrixPosistion(i,j),base_matrix[i][j])

    def get_cell_value(self,pos):
        if pos.i < 0:
            return 0
        if pos.j < 0:
            return 0
        return self.sums_matrix[pos.i][pos.j]


def run_tests():
    t = MatrixSums()

    # [1]
    t.init_sums_matrix([[1]])
    assert t.get(MatrixPosistion(0, 0)) == 1
    assert t.sum(MatrixPosistion(0, 0),MatrixPosistion(0, 0)) == 1
    t.set(MatrixPosistion(0, 0),5)
    assert t.get(MatrixPosistion(0, 0)) == 5
    assert t.sum(MatrixPosistion(0, 0),MatrixPosistion(0, 0)) == 5

    # [[1,2,3]
    #   [2,0,1]]
    t.init_sums_matrix([[1, 2, 3], [2, 0, 1]])
    assert t.get(MatrixPosistion(0, 0)) == 1
    assert t.get(MatrixPosistion(0, 2)) == 3
    assert t.sum(MatrixPosistion(0, 0), MatrixPosistion(0, 2)) == 6
    assert t.get(MatrixPosistion(1, 2)) == 1
    assert t.sum(MatrixPosistion(1, 1), MatrixPosistion(1, 2)) == 1

    # [[1,0,3]
    #   [2,0,1]]
    t.set(MatrixPosistion(0, 1), 0)
    assert t.get(MatrixPosistion(0, 1)) == 0
    assert t.get(MatrixPosistion(0, 2)) == 3
    assert t.sum(MatrixPosistion(0, 0), MatrixPosistion(0, 2)) == 4
    assert t.sum(MatrixPosistion(0, 0), MatrixPosistion(1, 2)) == 7
    assert t.get(MatrixPosistion(1, 2)) == 1
    assert t.sum(MatrixPosistion(1, 1), MatrixPosistion(1, 2)) == 1

    # [[5,2,3]
    #   [2,0,1]]
    t.set(MatrixPosistion(0, 1), 2)
    t.set(MatrixPosistion(0, 0), 5)
    assert t.get(MatrixPosistion(0, 0)) == 5
    assert t.get(MatrixPosistion(0, 2)) == 3
    assert t.sum(MatrixPosistion(0, 0), MatrixPosistion(0, 2)) == 10
    assert t.sum(MatrixPosistion(0, 0), MatrixPosistion(1, 2)) == 13
    assert t.get(MatrixPosistion(1, 2)) == 1
    assert t.sum(MatrixPosistion(1, 1), MatrixPosistion(1, 2)) == 1


if __name__ == '__main__':
    run_tests()