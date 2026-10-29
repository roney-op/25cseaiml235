#maximum algorithm
def minimax(depth, nodeIndex, ismax, scores, height):
  #basic case: leaf node reached
  if depth == height:
    return scores[nodeIndex]

  if ismax:
    return max(minimax(depth+1, nodeIndex*2, False, scores, height),
               minimax(depth+1, nodeIndex*2+1, False, scores, height))
  else:
    return min(minimax(depth+1, nodeIndex*2, True, scores, height),
               minimax(depth+1, nodeIndex*2+1, True, scores, height))
#main program
scores=list(map(int,input("enter 8 leaf node values:").split()))
height=3
result=minimax(0,0,True,scores,height)
print("The optimal value is:",result)