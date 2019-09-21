An implementation of a "flexible" calculator that receives 
a mathematical expression in a form of a list of chars, 
and recursively calculates the results.

The calculator allows the user to choose one of two possible 
mathematical writing notation for interpreting the given expression.

The two possible notation relate specifically to the interpretation 
of implied multiplication - 

1. 8÷2(2+2) = 8÷2*(2+2) = 8÷2*4 = 4*4 = 16
2. 8÷2(2+2) = 8/(2*(2+2)) = 8/(2*4) = 8/8 = 1

Related blog posts - 

Calculator part A - https://mayareads.blog/2019/08/24/cala-part-a/
Calculator part B - https://mayareads.blog/2019/08/24/cala-part-b/