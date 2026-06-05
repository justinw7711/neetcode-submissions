class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = [] 
        final = 0
        for op in operations:
            if op == "+":
                score = record[-1] + record[-2]
                record.append(score)
            elif op == "D":
                score = record[-1] * 2
                record.append(score)
            elif op == 'C':
                record.pop()
            else:
                score = int(op)
                record.append(score)
        for i in record:
            final += i
        return final