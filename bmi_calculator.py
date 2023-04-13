""" Functions for calculating BMI and BMI category"""

# Formula: http://extoxnet.orst.edu/faqs/dietcancer/web2/twohowto.html
def calc_bmi(height, weight):
    """ Calculate BMI """
    bmi = 0.45 * weight / ((height * 0.025) ** 2)
    bmi = round(bmi, 1)
    return bmi

def get_bmi_category(bmi):
    """ Calculate BMI category """
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal weight"
    if bmi < 30:
        return "Overweight"
    return "Obese"
