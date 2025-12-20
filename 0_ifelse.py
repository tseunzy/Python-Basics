print('======IF/ELSE CONDITION STATEMENT=========')
# if/else statments

age = 18
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

print('=======Example 2========')

#to lookout for even and odd numbers
n = 11
if n % 2 == 0:
    print('Number is divisible by 2')
elif n % 3 == 0:
    print('Number is divisible by 3')
else:
    print('Number is neither divisible by 2 nor 3')
print('Done!')

print('======Example 3=========')
#Grading of students scores using the if, elif 
score = int(input("Enter your score: "))
if score >= 70:
    print("Excellent! Grade A")
elif score >= 60:
    print("Very Good! Grade B")
elif score >= 50:
    print("Good! Grade C")
elif score >= 40:
    print("Pass! Grade D")
else:
    print("Fail! Grade F")




print('======Nested if statement=========')
# this if a nested if statement
age = 20
nationality = 'Nigerian'
if age > 18:
    if age < 30:
        if nationality == 'Nigerian':
            print('You are qualify for this Exam')

print('=======Example========')


#using the AND with IF statement
age = 20
nationality = 'Nigerian'
if age > 18 and age < 30 and nationality == 'Nigerian':
    print('You are qualify for this Exam')

print('=======Example========')


# LOGICAL AND WITH IF-ELSE STATEMENT
age = 41
nationality = 'Nigerian'
if age > 18 and age < 30 and nationality == 'Nigerian':
    print('You are qualify for this Exam')
else:
    print('You are not eligible for the exam')


print('=======Example========')


# LOGICAL AND WITH IF-ELIF-ELSE STATEMENT
age = int(input('whats your age?'))
nationality = 'American'
if age > 18 and age < 30 and nationality == 'Nigerian':
    print('You are qualify for this Exam. Exam fee is 2000 naira')
elif age > 18 and age < 30 and nationality == 'American':
    print('You are not eligible for the exam. Exam fee is $50')
else:
    print('You are not eligible for the exam.')