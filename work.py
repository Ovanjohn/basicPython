#Function that concatenates the Fistname, middlename and lastname.
def concatenateNames (firstName, middleName, lastName):
     fullName = firstName + "" + middleName +" "+ lastName
     return fullName
firstName = "john"
middleName = "obi"
lastName = "ibe"
result = concatenateNames(firstName, middleName, lastName)
print(result)

#function that adds two numbers using print
def addAndPrint(num1, num2):
  result = num1 + num2
  print("The sum is:", result)
number1 = 5
number2 = 9
addAndPrint(number1, number2)

#function that adds two numbers using return
def addNumbers(num1, num2):
  result = num1 + num2
  return result
number1 = 40
number2 = 90
sumResult = addNumbers(number1, number2)
print("The sum is:", sumResult)

#function that substract
def subtractNumbers(num1, num2):
  result = num1 - num2
  return result
resultSubtraction = subtractNumbers(89, 19)
print("subtraction result:", resultSubtraction)

#division function
def divideNumbers(num1, num2):
  if num2 != 0:
      result = num1/num2
      return result
  else:
      return "cannot be divided by zero"
resultDivision = divideNumbers(90,3)
print("Division result:", resultDivision)

#multiplication
def multiplyNumbers(num1, num2):
  result = num1 * num2
  return result
resultMultiplication = multiplyNumbers(13,18)
print("Multiplication result:", resultMultiplication)


#function that converts a name to lowercase
def convertToLowercase(name):
  lowercasedName = name.lower()
  return lowercasedName
originalName = "OBI"
lowercasedResult = convertToLowercase(originalName)
print("lower cased name:", lowercasedResult)


#function that converts a name to upper case
def convertToUppercase(name):
  uppercasedName = name.upper()
  return uppercasedName
originalName = "obi"
uppercasedResult = convertToUppercase(originalName)
print("Upper cased name:", uppercasedResult)

#function that grades a student base on the score he/she has inputed
def gradeStudent(score):
  if 90 <= score <= 100:
     return "A"
  elif 80 <= score < 90:
     return "B"
  elif 70 <= score < 80:
     return "C"
  elif 60 <= score < 70:
     return "C"
  elif 0 <= score < 60:
     return "F"
  else:
     return "invalid score"
studentScore = 85
result = gradeStudent(studentScore)
print("Grade:", result)


#class called car
class Car:
  def  __init__ (self):
    pass
  def speed(self):
    print( "i have speed")

car1 = Car()
car1.speed()

car2 = Car()
car2.speed()

#creating a class for signing up, user sign in
class User:
  def __init__(self, firstname, lastname, middlename, dateOfBirth, eligibleVotingStatus=False):
    self.firstname = firstname
    self.lastname = lastname
    self.middlename = middlename
    self.dateOfBirth = dateOfBirth
    self.eligibleVotingStatus = eligibleVotingStatus
    self.is_signed_in = False

  def sign_up(self):
    print(f"User {self.firstname} {self.lastname} signed up successfully.")

  def sign_in(self):
    self.is_signed_in = True
    print(f"User {self.firstname} {self.lastname} signed in successfully.")
new_user = User("Obi", "Oqui", "Nna", "1988-12-01", True)
new_user.sign_up()
new_user.sign_in()


