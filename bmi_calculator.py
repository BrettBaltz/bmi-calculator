def verify_height(feet, inches):
    try:
        if not feet.isdigit():
            return False
        
        feet = int(feet)
        inches = float(inches)

        if feet < 0 or inches < 0:
            return False
        if feet == 0 and inches == 0:
            return False
        return True
    
    except ValueError:
        return False

def verify_weight(weight):
    try:
        weight = float(weight)
        if weight <= 0:
            return False
        return True
    except ValueError:
        return False

# Formula: http://extoxnet.orst.edu/faqs/dietcancer/web2/twohowto.html
def calc_bmi(height, weight):
    bmi = 0.45 * weight / ((height * 0.025) ** 2)
    bmi = round(bmi, 1)
    return bmi

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal weight"
    if bmi < 30:
        return "Overweight"
    return "Obese"

def main():
    feet = input("Enter your height in feet: ")
    inches = input("Enter your height in inches: ")
    while not verify_height(feet, inches):
        print("Invalid input. Feet must be a nonnegative integer. Inches must be a nonnegative number. Height must be positive number.")
        feet = input("Enter your height in feet: ")
        inches = input("Enter your height in inches: ")
    height = int(feet) * 12 + float(inches)

    weight = input("Enter your weight in pounds: ")
    while not verify_weight(weight):
        print("Invalid input. Weight must be a nonnegative number.")
        weight = input("Enter your weight in pounds: ")
    weight = float(weight)

    bmi = calc_bmi(height, weight)
    bmi_category = get_bmi_category(bmi)

    print("Your bmi is", bmi)
    print("You are", bmi_category)

if __name__ == "__main__":
    main()