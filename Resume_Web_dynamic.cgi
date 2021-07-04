#!/usr/bin/env python
# prompt user to enter resume details and 
# display web page with a filled resume
import cgi

def main():
    form = cgi.FieldStorage()
    # Bio
    firstname = form.getfirst('firstname')
    secondname = form.getfirst('secondname')
    user_address = '' if form.getfirst('user_address') == None else form.getfirst('user_address')
    user_cellphone = '' if form.getfirst('user_cellphone') == None else form.getfirst('user_cellphone')
    user_email = '' if form.getfirst('user_email') == None else form.getfirst('user_email')

    # Current Education Details
    major_1 = '' if form.getfirst('major_1') == None else form.getfirst('major_1') 
    schoolname_1 = '' if form.getfirst('schoolname_1') == None else form.getfirst('schoolname_1')
    school_address_1 = '' if form.getfirst('school_address_1') == None else form.getfirst('school_address_1')

    # Undergraduate Education Details
    major_2 = '' if form.getfirst('major_2') == None else form.getfirst('major_2')
    schoolname_2 = '' if form.getfirst('schoolname_2') == None else form.getfirst('schoolname_2')
    school_address_2 = '' if form.getfirst('school_address_2') == None else form.getfirst('school_address_2')
    
    # Main skills
    skill_1 = '' if form.getfirst('skill_1') == None else form.getfirst('skill_1')
    skill_2 = '' if form.getfirst('skill_2') == None else form.getfirst('skill_2')
    skill_3 = '' if form.getfirst('skill_3') == None else form.getfirst('skill_3')
    skill_4 = '' if form.getfirst('skill_4') == None else form.getfirst('skill_4')
    skill_5 = '' if form.getfirst('skill_5') == None else form.getfirst('skill_5')
    skill_6 = '' if form.getfirst('skill_6') == None else form.getfirst('skill_6')
    skill_7 = '' if form.getfirst('skill_7') == None else form.getfirst('skill_7')
    skill_8 = '' if form.getfirst('skill_8') == None else form.getfirst('skill_8')
    
    # Interests
    interest_1 = '' if form.getfirst('interest_1') == None else form.getfirst('interest_1')
    interest_2 = '' if form.getfirst('interest_2') == None else form.getfirst('interest_2')
    interest_3 = '' if form.getfirst('interest_3') == None else form.getfirst('interest_3')

    contents = makePage('ResumeTemplate.html',(firstname,secondname,user_address,user_cellphone,\
        user_email,major_1,schoolname_1,school_address_1,major_2,schoolname_2,school_address_2,\
            skill_1,skill_2,skill_3,skill_4,skill_5,skill_6,skill_7,skill_8,interest_1,\
                interest_2,interest_3))
    print(contents)

def fileToStr(fileName):
    # return a string containing the contents of that file
    fin = open(fileName)
    contents = fin.read()
    fin.close()
    return contents

def makePage(templateFileName, substitutions):
    pageTemplate = fileToStr(templateFileName)
    return pageTemplate.format(*substitutions)

try:
    print("content-type: text/html\n\n")
    main()
except:
    cgi.print_exception()