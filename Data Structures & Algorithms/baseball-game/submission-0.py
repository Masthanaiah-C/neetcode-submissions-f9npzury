class Solution:
    def calPoints(self, operations: List[str]) -> int:
        Record = list()
        for op in operations:
            if (op == "+"):
                Record.append(Record[-1] + Record[-2])
                continue
            if (op == "D"):
                    Record. append(Record[-1] * 2)
                    continue
            if (op == "C"):
                    Record. pop()
                    continue
            # Convert str to num.
            Record.append(int(op))
        
        TotalSum = 0
        for num in Record:
            TotalSum += num
        
        return TotalSum
