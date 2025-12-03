import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.route(route="http_trigger", auth_level=func.AuthLevel.ANONYMOUS)
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    number = req.params.get('number')
    if not number:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            number = req_body.get('number')

    if number:
        try:
        # Convert number to integer
            num = int(number)

            response = analyze_number(num)
        except ValueError:
            response = { "error": "please enter a valid number" }
        
        return func.HttpResponse(json.dumps(response), mimetype="application/json")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a number in the query string or in the request body.",
             status_code=200
        )


# TODO: Implement the analyze_number function
# You will only make modifications to the function below
def analyze_number(num):
    # TODO 1: Code Logic to handle number validation
    if num <= 0:
        return { "error": "please enter a number greater than 0" }
    # TODO 2: Code Logic to find the sum of numbers
    sum_of_digits = sum(int(digit) for digit in str(num))
    # TODO 3: Code Logic to check whether number is prime
    is_prime = True
    if num <= 1:
        is_prime = False
    else:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
    # TODO 4: Code Logic to check whether number is odd
    is_odd = (num % 2 != 0)

    # TODO 5: Code Logic to check whether number is perfect
    sum_of_divisors = 0

    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            sum_of_divisors += i
            
    is_perfect = (sum_of_divisors == num)

    # NEW TODO: Code Logic to check whether number is triangular
    # Mathematical rule: A number 'x' is triangular if 8x + 1 is a perfect square
    check_val = 8 * num + 1
    root = int(check_val**0.5)
    is_triangular = (root * root == check_val)
    
    # TODO 6: Replace default values below with the results of the calculations from
    # TODOs 2-5.

    response = {
        "sum_of_digits": 10,
        "is_prime": false,
        "is_odd": false,
        "is_perfect": true,
        "is_triangular": true
        }

    return response