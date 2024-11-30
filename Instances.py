from UserInputValidator import InputValidator

validator1 = InputValidator()
validator2 = InputValidator()

input1 = ["2", "b", "9000", "6.7", "40", "three"]
input2 = ["-2", "26", "eight hunred", "546", "40", "17"]

checkinput1 = validator1.validate_positive_integer(input1)
checkinput2 = validator2.validate_positive_integer(input2)

validator1.display_validation_message()
validator2.display_validation_message()

print(f"results for inputs 1: {checkinput1}")
print(f"results for inputs 2: {checkinput2}")