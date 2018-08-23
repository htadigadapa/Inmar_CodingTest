Feature: Addition of two numbers

	
	Scenario Outline: Add any two numbers

        Given I have entered <number1> and <number2>

        When I chose to perform addition

        Then the sum should be <result>

 

        Examples:

            |  number1|  number2|   result|

            |        3|        2|        5|

            |        9|        8|       17|  

            |       22|       22|       44|
			
			|       22|      -10|       12|
			
			|      -10|      -10|      -20|