from wtforms import StringField, IntegerField, SubmitField, SelectField
from flask import Flask, render_template, session
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from src.main import preprocess_data, load_model, get_prediction
import pandas as pd
from datetime import datetime

class PredictionForm(FlaskForm):
    FACILITY = SelectField('Enter Facility: ', choices=[('KFSH&RC Riyadh', 'KFSH&RC Riyadh'), ('KFSH&RC Jeddah', 'KFSH&RC Jeddah'), ('KFNCCC', 'KFNCCC'), ('KFSH&RC MADINAH', 'KFSH&RC MADINAH')])
    ACUITY_LEVEL = SelectField('Enter Acuity Level: ', choices=[('1-Resuscitation', '1-Resuscitation'), ('2-Emergent', '2-Emergent'),
                                                                ('3-Urgent', '3-Urgent'), ('4-Less Urgent', '4-Less Urgent'), ('5-Nonurgent', '5-Nonurgent')])
    BUILDING = SelectField('Enter Building: ', choices=[('EMS', 'EMS'), ('Main Building', 'Main Building'), ('East Wing', 'East Wing'),
                                                        ('West Wing', 'West Wing'), ('South Building', 'South Building'), ('Main-CCC', 'Main-CCC')])
    ADMIT_MODE = SelectField('Enter Admit Mode: ', choices=[('Red Crescent Ambulance', 'Red Crescent Ambulance'), ('Family', 'Family'), ('Wheelchair', 'Wheelchair'),
                                                            ('Walking', 'Walking'), ('KFSH Ambulance', 'KFSH Ambulance'), ('Threat to Life', 'Threat to Life'),
                                                            ('Other Hospital Ambulance', 'Other Hospital Ambulance'), ('Relative', 'Relative'), ('Police custody', 'Police custody'),
                                                            ('Stretcher', 'Stretcher'), ('Carried', 'Carried'), ('Helicopter', 'Helicopter'), ('Other', 'Other')])
    DAY_OF_WEEK = StringField('Enter Day Of The Week: ')
    AGE = IntegerField('Enter Age: ', validators=[DataRequired()])
    SUBMIT= SubmitField('Predict')

app=Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

@app.route('/')
def home():
    return render_template('start.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    form = PredictionForm()
    prediction=None
    if form.validate_on_submit():
        user_data ={'FACILITY':form.FACILITY.data, 
                    'ACUITY_LEVEL':form.ACUITY_LEVEL.data,
                    'BUILDING':form.BUILDING.data, 
                    'ADMIT_MODE':form.ADMIT_MODE.data,
                    'DAY_OF_WEEK':datetime.now().strftime('%A'), 
                    'AGE':form.AGE.data}
        user_data_df=pd.DataFrame([user_data])
        processed_data, acuity_level=preprocess_data(user_data_df)
        
        try:
            model=load_model(acuity_level)
        except Exception as load_model_error:
            return render_template('index.html', form=form, prediction=None, error=str(load_model_error))
        
        try:
            prediction=get_prediction(model, processed_data)
        except Exception as prediction_error:
            return render_template('index.html', form=form, prediction=None, error=str(prediction_error))

    form.DAY_OF_WEEK.data=datetime.now().strftime('%A')

    return render_template('index.html', form=form, prediction=prediction)

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')