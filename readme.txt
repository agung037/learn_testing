Berikut adalah jawaban Quiz 2: Equivalence PartitioningFile, oleh Agung Kurniawan 2113070017
kode program implementasi terlampir dalam folder ex1_code, ex2_code dan ex3_code, ditulis menggunakan bahasa python

# Excersise 1
the equivalent cases possible is infinite, but 
the recommended equivalent cases is 3 for each partition
one case for invalid test with input value below minimum 
one case for invalid test with input value beyond maximum
and one case valid input

– input values between 0 and 15: grey bar 
  * invalid test   n < 0 	example: -1
  * valid test   0 <= n <= 15	example: 5
  ans : 2 EC

- input values between 16 and 50: green bar 
  * valid test 15 <= n <= 50  	example: 20
  ans : 1 EC

- input values between 51 and 85: yellow bar
  * valid test 51 <= n <= 85 	example: 56
  ans : 1 EC

- input values between 86 and 100: red bar
  * valid test 86 <= n <= 100	example: 90 
  * invalid test n > 100 	example: 230
  ans : 2 EC

answer 6 EC


# Excersise 2
- input value between 0 and 100 : 3% rate
  	* invalid test  n < 0 	example: -50
  	* valid test 0 <= n <= 100 	example 89

- input value between 101 and 1000 : 5% rate
	* valid test 101 <= n <= 1000 	example 502

- input value over 1000 : 7% rate
	* valid test 1001 <= n 		example 91000

answer 4 EC



#Excersise 3
-test base good price between 0 and infinite :
	*valid test 0 <= n  example : 89
	*invalid test n < 0 example : -81

-test discount percentage between 0 and 100 :
	*valid test n <= 0 <= 100 example : 7.5
	*invalid test n < 0 example : -7.5
	*invalid test n > 100 example : 101

-test shipping mode regular or express or priority
	* valid test x = "regular"
	* valid test x = "express"
	* valid test x = "priority"
	* invalid test x = "super" 

answer 9 EC