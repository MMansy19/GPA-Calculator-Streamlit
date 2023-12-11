import pandas as pd
import streamlit as st

def grade_to_number(grades,gpa,dictGrades):
 
 keys=list(dictGrades.keys())
 values=list(dictGrades.values())
 for  i,grade in  enumerate(grades):
    for index in range(len(dictGrades)):
        if grade == keys[index]:
            gpa[i]=values[index]
 
    if gpa[i]==0:
        warning('Please write a valid grade')
 return gpa
 '''This Function #Changes Grades into GPA number from 1.0 to 4.0'''

def warning(message,sidebar=0):
    if sidebar:
        st.sidebar.warning(message , icon="⚠️")
    else:
        st.warning(message , icon="⚠️")

st.title('GPA Calculator')
num=st.sidebar.number_input('Number of courses:',5,50)
last_credits=st.sidebar.number_input('Credits:',0,175,step=3)
last_gpa=st.sidebar.number_input('Current GPA:', min_value=0.0, max_value=4.0, value=0.0, step=0.1)

if last_credits==0 and last_gpa!=0:
    warning('Please Enter Credits',1)
if last_credits!=0 and last_gpa==0:
    warning('Please Enter Current GPA',1)

#initialsing
semester_credits=0
qualityPoints=0.0
grades=['A']*num
credits=[3]*num
courses=[]
nums=[]
dictGrades={'A+':4.0,'A':4.0,'A-':3.7,
            'B+':3.3,'B':3.0,'B-':2.7,
            'C+':2.3,'C':2.0,'C-':1.7,
            'D+':1.3,'D':1.0,'F':0.0}
gpaPointValue=[0]*num
#endOfInitialsing

for i in range(num):
    courses.append(f'Course number {i+1}')
    nums.append(f'{i+1}')

#creating a dataframe   
df=pd.DataFrame({'':nums,'Course':courses,
              'Grade':grades,
              'Credits':credits})

#making dataframe editabe to rewrite in it
editable_df=st.experimental_data_editor(df)
courses=editable_df['Course']
grades=editable_df['Grade']
credits=editable_df['Credits']

#Filling Credits Column
for i in range(num):
    if credits[i]<1 or credits[i]>=5:
        warning('Please write a valid credit')
    semester_credits+=credits[i]

#Changing Grades into GPA number from 1.0 to 4.0
gpaPointValue=grade_to_number(grades,gpaPointValue,dictGrades)

#calculating the semester GPA
for i in range(num):
    qualityPoints += gpaPointValue[i]*credits[i]

newGPA=qualityPoints/semester_credits

#calculating the accumulative GPA
all_credits=semester_credits+last_credits
accumulativeGPA=(newGPA*semester_credits+last_gpa*last_credits)/all_credits

st.write("Your Semester GPA is: " + str(newGPA))
st.write("Your Accumulative GPA is: " + str(accumulativeGPA))
