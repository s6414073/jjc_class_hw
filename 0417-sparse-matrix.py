#!/usr/bin/env python2

class SparseMatrix(object):

    @classmethod
    def multiply(self, A, B):
        result = []
        BT = zip(*B) # transfer B,get the column of B
        length = len(B)
        for row in A:
            if not any(row):
                result.append([0] * length)
                continue
            result.append([sum(map(lambda (x, y) : x * y, zip(row, col))) if any(col) else 0 for col in BT])

        return result

    @classmethod
    def transpose(self, X):
        


if __name__ == '__main__':

	A = [
		[ 1, 0, 0],
		[-1, 0, 3]
					]

	B = [
		[ 7, 0, 0 ],
 		[ 0, 0, 0 ],
		[ 0, 0, 1 ]
					]

	C = [
		[7, 0, 0],
		[-7, 0, 3]
					]

#	assert SparseMatrix.multiply(A, B) == C, 'Fail'
	print(SparseMatrix.multiply(A, B))
