import math
from django.shortcuts import render
from django.http import JsonResponse

def calculator_view(request):
    result = None
    error = None

    if request.method == 'POST':
        try:
            num1 = float(request.POST.get('num1', 0))
            num2 = request.POST.get('num2', None)
            operation = request.POST.get('operation')

            # Basic Operations
            if operation == 'add':
                result = num1 + float(num2)
            elif operation == 'subtract':
                result = num1 - float(num2)
            elif operation == 'multiply':
                result = num1 * float(num2)
            elif operation == 'divide':
                if float(num2) == 0:
                    error = "Cannot divide by zero"
                else:
                    result = num1 / float(num2)
            
            # Advanced Operations
            elif operation == 'modulus':
                if float(num2) == 0:
                    error = "Cannot perform modulus with zero"
                else:
                    result = num1 % float(num2)
            elif operation == 'exponentiation':
                result = num1 ** float(num2)
            elif operation == 'square_root':
                if num1 < 0:
                    error = "Cannot calculate square root of negative number"
                else:
                    result = math.sqrt(num1)
            elif operation == 'factorial':
                if num1 < 0 or not num1.is_integer():
                    error = "Factorial is only defined for non-negative integers"
                else:
                    result = math.factorial(int(num1))
            
            # Logarithmic Functions
            elif operation == 'log':
                if num1 <= 0:
                    error = "Logarithm is not defined for non-positive numbers"
                else:
                    result = math.log10(num1)
            elif operation == 'ln':
                if num1 <= 0:
                    error = "Natural logarithm is not defined for non-positive numbers"
                else:
                    result = math.log(num1)
            
            # Trigonometric Functions (input in degrees)
            elif operation == 'sin':
                result = math.sin(math.radians(num1))
            elif operation == 'cos':
                result = math.cos(math.radians(num1))
            elif operation == 'tan':
                if math.cos(math.radians(num1)) == 0:
                    error = "Tangent is undefined for this angle"
                else:
                    result = math.tan(math.radians(num1))
            
            # Hyperbolic Functions
            elif operation == 'sinh':
                result = math.sinh(num1)
            elif operation == 'cosh':
                result = math.cosh(num1)
            elif operation == 'tanh':
                result = math.tanh(num1)
            
            # Inverse Trigonometric Functions (output in degrees)
            elif operation == 'asin':
                if not -1 <= num1 <= 1:
                    error = "Inverse sine is only defined for values between -1 and 1"
                else:
                    result = math.degrees(math.asin(num1))
            elif operation == 'acos':
                if not -1 <= num1 <= 1:
                    error = "Inverse cosine is only defined for values between -1 and 1"
                else:
                    result = math.degrees(math.acos(num1))
            elif operation == 'atan':
                result = math.degrees(math.atan(num1))
            
            # Additional Mathematical Functions
            elif operation == 'abs':
                result = abs(num1)
            elif operation == 'ceil':
                result = math.ceil(num1)
            elif operation == 'floor':
                result = math.floor(num1)
            elif operation == 'round':
                result = round(num1, int(num2) if num2 else 0)
            elif operation == 'pi':
                result = math.pi
            elif operation == 'e':
                result = math.e
            elif operation == 'degrees':
                result = math.degrees(num1)
            elif operation == 'radians':
                result = math.radians(num1)
            else:
                error = "Invalid operation selected"

        except ValueError as e:
            error = "Invalid input: Please enter valid numbers"
        except TypeError as e:
            error = "Type error: Please check your input"
        except Exception as e:
            error = f"An error occurred: {str(e)}"

        if error:
            return JsonResponse({"error": error})
        return JsonResponse({"result": result})

    return render(request, 'calculator/calculator.html', {'result': result})
