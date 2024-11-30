class InputValidator:
    def validate_positive_integer(self, inputs):
        validintegers = []
        for item in inputs:
            if item.isdigit() and int(item) > 0:
                validintegers.append(int(item))
        return validintegers
    
    def display_validation_message(self):
        print("The list has been succesfully validated.")