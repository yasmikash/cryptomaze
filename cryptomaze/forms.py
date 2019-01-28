from flask_wtf import FlaskForm, RecaptchaField, Recaptcha
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length
from cryptomaze.models import User
from cryptomaze.validate_btc_address import check_bc


class SignUpForm(FlaskForm):
    bitcoin_address = StringField('Bitcoin Address', validators=[DataRequired(), Length(
        max=40)], render_kw={"placeholder": "Enter your Bitcoin Address here"})
    submit_signup = SubmitField('Start Earning Bitcoin')

    def validate_bitcoin_address(self, bitcoin_address):
        if not check_bc(bitcoin_address.data):
            raise ValidationError('Invalid Bitcoin Address.')


class ClaimForm(FlaskForm):
    submit_claim = SubmitField('Claim')
    recaptcha = RecaptchaField(
        validators=[Recaptcha('Please solve recaptcha again.')])


class WithdrawForm(FlaskForm):
    submit_withdraw = SubmitField('Withdraw')
    recaptcha = RecaptchaField(
        validators=[Recaptcha('Please solve recaptcha again.')])
