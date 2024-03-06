import pandas as pd

def get_data_from_user():
    FACILITY=input('Enter FACILITY:')
    ACUITY_LEVEL=input('Enter ACUITY_LEVEL:')
    BUILDING=input('Enter BUILDING:')
    ADMIT_MODE=input('Enter ADMIT_MODE:')
    DAY_OF_WEEK=input('Enter DAY_OF_WEEK:')

    while True:
        try:
            AGE=int(input('Enter AGE:'))
            break
        except ValueError:
            print('invalid input for AGE. please enter a valid integer.')

    data=pd.DataFrame({'FACILITY':[FACILITY],
                        'ACUITY_LEVEL':[ACUITY_LEVEL],
                        'BUILDING':[BUILDING],
                        'ADMIT_MODE':[ADMIT_MODE],
                        'DAY_OF_WEEK':[DAY_OF_WEEK],
                        'AGE':[AGE]
    })

    return data