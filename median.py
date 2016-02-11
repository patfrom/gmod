def median(lst):
 sortedLst = sorted(lst)
 lstLen = len(lst)
 index = (lstLen - 1) // 2
 print sortedLst
 print lstLen
 print index
 if (lstLen % 2):
  return sortedLst[index]
 else:
  return (sortedLst[index] + sortedLst[index + 1])/2.0

lista = [10,12,3,4,5,6,7]
print lista
print median(lista)
raw_input()
