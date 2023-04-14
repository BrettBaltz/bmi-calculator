""" Web application for calculating a user's BMI """
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import IntegerField, DecimalField, SubmitField
from wtforms.validators import InputRequired, NumberRange
from bmi_calculator import calc_bmi, get_bmi_category

class BmiForm(FlaskForm):
    """ Form for reading user height and weight """
    feet = IntegerField(validators = [
        InputRequired(),
        NumberRange(min=0)
    ])
    inches = DecimalField(validators = [
        InputRequired(),
        NumberRange(min=0)
    ])
    pounds = DecimalField(validators = [
        InputRequired()
    ])
    submit = SubmitField('Calculate BMI')

    def validate(self, extra_validators = None):
        is_valid = True
        if not FlaskForm.validate(self):
            return False

        # Validate positive height
        if self.feet.data == 0 and self.inches.data == 0:
            self.feet.errors.append('Height must be positive')
            is_valid = False

        # Validate positive weight
        if self.pounds.data <= 0:
            self.pounds.errors.append('Weight must be positive')
            is_valid = False

        return is_valid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'T@&5RcGyBwXbVjb^%VX3'
app.config['SERVER_NAME'] = '127.0.0.1:5000'
app.config['SESSION_COOKIE_DOMAIN'] = 'localhost.localdomain'
app.config['APPLICATION_ROOT'] = '/'

@app.route('/', methods=['GET', 'POST'])
def home():
    """ Webpage which takes user height and weight and outputs BMI if valid."""
    bmi_form = BmiForm()

    if bmi_form.validate_on_submit():
        height = bmi_form.feet.data * 12 + float(bmi_form.inches.data)
        bmi = calc_bmi(height, float(bmi_form.pounds.data))
        bmi_category = get_bmi_category(bmi)

        return render_template(
            'bmi_calculator.html',
            bmi_form=bmi_form,
            bmi=bmi,
            bmi_category=bmi_category
        )

    return render_template(
        'bmi_calculator.html',
        bmi_form=bmi_form,
        bmi=0,
        bmi_category=None
    )

if __name__ == '__main__':
    with app.app_context():
        app.run()
