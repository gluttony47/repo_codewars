def digital_root(n):
    result = 0
    modulo = 0
## ------------------------------------    
## sumsum(x) is a method that finds out 
## the sum of the digits of the number.
## for example : sumsum(456) returns 
## 4 + 5 + 6 = 15....

    def sumsum(x): 
        result = 0
        while (x>9):
            modulo = x % 10
            result = result + modulo
            x = (int)((x - modulo)/10)
            if(x<10):
                result = result + x
        return result
## -------------------------------------

## since digital root gives back only a 
## single number, check variable will 
## inquire whether result is single digit 
## or not. if not single digit, it runs 
## through while loop again.
    check = sumsum(n)
    while (check>9):
        check = sumsum(check)   
## 'check' is the final answer     
    return check
    
## -----FINISHED-------------------------


### PROBLEM
##In this kata, you must create a digital root function.

##A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has two digits, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.

##Here's how it works (Ruby example given):

##digital_root(16)
##=> 1 + 6
##=> 7

##digital_root(942)
##=> 9 + 4 + 2
##=> 15 ...
##=> 1 + 5
##=> 6

##digital_root(132189)
##=> 1 + 3 + 2 + 1 + 8 + 9
##=> 24 ...
##=> 2 + 4
##=> 6

##digital_root(493193)
##=> 4 + 9 + 3 + 1 + 9 + 3
##=> 29 ...
##=> 2 + 9
##=> 11 ...
##=> 1 + 1
##=> 2

###
