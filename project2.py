import numpy as np
#representing a sqaure
square=np.array([[0,0,1,1],
                [0,1,0,1]])
#trasnformation 
scale=np.array([[2,0],
                [0,2]])
#if we want to roate sahpe in 90*
rotation90=np.array([[0,-1],
                  [1,0]])
#if we want to roatate shape in 180*
rotation180=np.array([[-1,0],
                      [0,-1]])
#stretch  transformation
stretch5times=np.array([[1,0],[0,5]])
#we apply dot product on vector for applying transformation
#skew transformation
skew7=np.array([[1,7],
              [0,1]])
scaled_sqaure=np.dot(scale,square)  

print("scaled sqaure",scaled_sqaure)
print("rotating square",np.dot(rotation90,square))
print("skewed sqaure",np.dot(stretch5times,square))
print("skewed",np.dot(skew7,square))
#representing a triangle
triangle=np.array([[1,4,3],
                  [2,2,5]])
scaled_triangle=np.dot(scale,triangle)
print("sacled triangle",scaled_triangle)
print("rotating triangle",np.dot(rotation90,triangle))
print("stretched triangle",np.dot(stretch5times,triangle))
print("skewed",np.dot(skew7,triangle))
