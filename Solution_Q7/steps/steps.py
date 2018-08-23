import behave

@given('I have entered {number1:d} and {number2:d}')

def read_numbers(context, number1, number2):
    context.number1 = number1
    context.number2 = number2

@when('I chose to perform addition')

def compute_result(context):
    context.result = context.number1+context.number2

 
@then('the sum should be {result:d}')

def validate_result(context, result):
    assert context.result == result 
