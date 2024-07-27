import sys
sys.path.append(r"D:\Project\query_classification")
from classifier import result


query = input('enter query')

print(result(query))