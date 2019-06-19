def getCollatzSequence(x):
    # ADD YOUR CODE HERE
   
      # ADD YOUR CODE HERE
   
    res = [x]    
    if x <= 0:
       return []
    while x > 1:
         if x % 2 != 0:
            x = (x * 3) + 1
            res.append(x)
         else:
              x = x // 2
              res.append(x)
    return res