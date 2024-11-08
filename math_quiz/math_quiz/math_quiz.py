import random


def generate_random_integer(min, max):
   
    #check if there is misorder in the inputs
    if min>max:
        raise ValueError("Minimum number should be less than teh Maximum number")
   
    #check if the inputs are not integers
    if not isinstance(min,int) or not isinstance(max,int):
        raise TypeError("Both min and max values must be integers")
    return random.randint(min, max)


def get_random_operation():
    """
    returning a random mathematical operator from {+,-,*}

    returns:
    a random operator as a string
    """
    return random.choice(['+', '-', '*'])


def perform_operation(n1, n2, o):
    """
    Here we perform a mathematical operation on the two given numbers based on the provided operator.
    n1: first input number
    n2: second input number
    o: the operation to perform

    returns:
    a tuple containing the operation as a string and the result of the calculation
    """

    #check if the inputs are of correct types
    if not isinstance(n1, int) or not isinstance(n2, int):
        raise TypeError("Both numbers must be integers ")
    
    #perform the desired operation
    function = f"{n1} {o} {n2}"
    if o == '+': result = n1 + n2
    elif o == '-': result = n1 - n2
    else: result = n1 * n2
    return function, result

def math_quiz():
    """
    This is a simple math quiz where the user is being asked math problems 
    and he/she must give the correct answers to get points.
    """
    score = 0
    total_questions = 4

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10); 
        num2 = generate_random_integer(1, 5); 
        operator = get_random_operation()

        #Generate the problem and answer
        problem, solution = perform_operation(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        try:
            #get the user answer
            useranswer = int(input("Your answer: "))

            if useranswer == solution:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {solution}.")
        except ValueError:
            print("please enter a valid integer")

    #print final score        
    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()