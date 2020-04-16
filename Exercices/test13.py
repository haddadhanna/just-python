##import mymodule
##from mymodule import do_factorial

#print(mymodule.do_square(2))
#print(do_factorial(4))

#import mypackage.mymodule
#from mypackage import mymodule
from mypackage.mymodule import do_square, do_factorial


print(do_square(2))
print(do_factorial(2))