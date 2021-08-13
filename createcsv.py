import numpy as np
import pandas as pd
student=pd.DataFrame([
                     [1,'aria',2,8.3,8,7,np.nan,np.nan,np.nan,np.nan,np.nan],
                     [2,'banu',3,8.3,8,7,7.5,8.5,9,np.nan,np.nan]
                    ],columns=['roll_no','student_name','year','gpa_sem1','gpa_sem2','gpa_sem3','gpa_sem4','gpa_sem5','gpa_sem6','gpa_sem7','gpa_sem8'])
student.to_csv('student.csv')
data=pd.read_csv('student.csv')
