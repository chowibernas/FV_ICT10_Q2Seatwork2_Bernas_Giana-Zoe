from pyscript import document, display
#Code above links the main.py to the index

def general_weighted_average(e):

    #These document.getElementById's avoid repeating results.
    document.getElementById("student_info").innerHTML = " "
    document.getElementById("allGrades").innerHTML = " "
    document.getElementById("finalGWA").innerHTML = " "
    
    """Step 2"""
    #These variables collect the user's input from the text boxes. 
    first_name = document.getElementById('studentFirstName').value
    last_name = document.getElementById('studentLastName').value

    
    #This is the if/if not condition code that ensures that the user fills up all the boxes.
    if not first_name or not last_name:
        document.getElementById("student_info").innerText = "⚠️ ERROR - Please fill out all the boxes!"
        return

    #These variables are the organized data of the user's inputted grades, converted into float data type. 
    # ValueError code is used to make sure that the user fills up all values/boxes for the grade input.
    try:
        Science = float(document.getElementById('grade_Science').value)
        Math = float(document.getElementById('grade_Math').value)
        English = float(document.getElementById('grade_English').value)
        Philosophy = float(document.getElementById('grade_Philosophy').value)
        Filipino = float(document.getElementById('grade_Filipino').value)
        ICT = float(document.getElementById('grade_ICT').value)
        TLE = float(document.getElementById('grade_TLE').value)
        CAT = float(document.getElementById('grade_CAT').value)
        PE = float(document.getElementById('grade_PE').value)
        VE = float(document.getElementById('grade_VE').value)
        Music_Arts = float(document.getElementById('grade_Music and Arts').value)

    except ValueError: 
            display("⚠️ ERROR - Please make sure all the boxes are filled!", target="student_info")
            return 
            #the code return is used to remove the display error once the user clicks the button again after completing all the boxes
    
    subjects = ["Science", "Math", "English", "Philosophy", "Filipino", "ICT", "TLE", "CAT", "PE", "VE", "Music & Arts"]

    """Step 3"""
    #This area contains the subject weights and the computation for the GWA. 
    #It gathers the data and multiply it based on the number of sessions with this subject. The product will then be divided with the total sum of sessions in order to get the GWA.
    all_grades = (Science*5 + Math*5 + English*5 + Philosophy*3 + Filipino*3 + 
                    ICT*2 + TLE*2 + CAT*2 + PE*1 + VE*1 + Music_Arts*1)
    amt_of_Ses = (5*3) + (3*2) + (2*3) + (1*3)
    gwa = all_grades/amt_of_Ses


    #F-STRING
    #The numbers enclosed in brackets are index of the subjects. .0f makes sure that there are no decimal places in the user's inputted data.
    summary = f"""{subjects[0]}: {Science:.0f}
    \n{subjects[1]}: {Math:.0f}
    \n{subjects[2]}: {English:.0f}
    \n{subjects[3]}: {Philosophy:.0f}
    \n{subjects[4]}: {Filipino:.0f}
    \n{subjects[5]}: {ICT:.0f}
    \n{subjects[6]}: {TLE:.0f}
    \n{subjects[7]}: {CAT:.0f}
    \n{subjects[8]}: {PE:.0f}
    \n{subjects[9]}: {VE:.0f}
    \n{subjects[10]}: {Music_Arts:.0f}"""
    
    #This area will display the results once the user filled up everything and clicked the button.
    display(f'Name: {first_name} {last_name}', target="student_info")
    display(summary, target="allGrades")
    display(f'Your general weighted average is {gwa:.2f}', target='finalGWA')

    


    

    