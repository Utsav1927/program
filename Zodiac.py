# Test change for pull request
import datetime
from datetime import date
import pandas
import csv

Dictionary1={}
def takeUserDay():
    try:
        
        day=int(input('Enter Day: '))

        if day != str:
            if day < 0 or day > 31:
                print('Enter a valid Day!')
                return takeUserDay()
            else:
                return day
    except:
        print('Only Numbers are accepted!')
        return takeUserDay()

def takeUserMonth():
    month = input('Enter Month: ')
    if month == 'january' or month == '1' or month == 'jan' or month == '01':
        monthNumber = 1
        return monthNumber
    elif month == 'february' or month == '2' or month == 'feb' or month == '02':
        monthNumber = 2
        return monthNumber
    elif month == 'march' or month == '3' or month == 'mar' or month == '03':
        monthNumber = 3
        return monthNumber
    elif month == 'april' or month == '4' or month == 'April' or month == '04':
        monthNumber = 4
        return monthNumber
    elif month == 'may' or month == '5' or month == 'May' or month == '05':
        monthNumber = 5
        return monthNumber
    elif month == 'june' or month == '6' or month == 'jun' or month == '06':
        monthNumber = 6
        return monthNumber
    elif month == 'july' or month == '7' or month == 'jul' or month == '07':
        monthNumber = 7
        return monthNumber
    elif month == 'august' or month == '8' or month == 'aug' or month == '08':
        monthNumber = 8
        return monthNumber
    elif month == 'september' or month == '9' or month == 'sep' or month == '09':
        monthNumber = 9
        return monthNumber
    elif month == 'october' or month == '10' or month == 'oct' or month == '10':
        monthNumber = 10
        return monthNumber
    elif month == 'november' or month == '11' or month == 'nov' or month == '11':
        monthNumber = 11
        return monthNumber
    elif month == 'december' or month == '12' or month == 'dec' or month == '12':
        monthNumber = 12
        return monthNumber
    else:
        print('!!!Not a valid month Please enter valid month!!!')
        return takeUserMonth()

def takeUserYear():

    try:
        year = int(input('Enter Year: '))

        if year != str:
            if year < 0:
                print('!!!Error!!!')
                return takeUserYear()
            elif year % 4 == 0:
                print('Leap Year!')
                return year
            else:
                return year
            
    except:
        print('Enter Numerical Value Only!!!')
        return takeUserYear()

def CalZodiacSign(day,month):

    if month == 12:
        astroSign = 'Sagittarius' if (day<22) else 'Capricorn'
    elif month == 1:
        astroSign = 'Capricorn' if (day<20) else 'Aquarius'
    elif month == 2:
        astroSign = 'Aquarius' if (day<19) else 'Pisces'
    elif month == 3:
        astroSign = 'Pisces' if (day<21) else 'Aries'
    elif month == 4:
        astroSign = 'Aries' if (day<20) else 'Taurus'
    elif month == 5:
        astroSign = 'Taurus' if (day<21) else 'Gemini'
    elif month == 6:
        astroSign = 'Gemini' if (day<21) else 'Cancer'
    elif month == 7:
        astroSign = 'Cancer' if (day<23) else 'Leo'
    elif month == 8:
        astroSign = 'Leo' if (day<23) else 'Virgo'
    elif month == 9:
        astroSign = 'Virgo' if (day<23) else 'Lebra'
    elif month == 10:
        astroSign = 'Lebra' if (day<23) else 'Scorpio'
    elif month == 11:
        astroSign = 'Scorpio' if (day<22) else 'Sagittarius'
    return astroSign

def takeDate(year ,month ,day):
    date1 = datetime.date(year ,month ,day)
    print('DOB',date1)
    return date1

def repQuestion():
    finder = input('Do you want to find and other Zodiac Signb (YES/NO)')
    if finder == 'yes':
        return True
    else:
        return False

def UserInput(count):

    username = input('Enter the name of the user: ')
    useryear = takeUserYear()
    usermonth = takeUserMonth()
    userdate =  takeUserDay()
    fulldate = takeDate(useryear,usermonth,userdate)
    yoursign = CalZodiacSign(userdate,usermonth)
    print(username,"Your Zodiac sign is : ",yoursign)
    Dictionary1[count] = {'FullNAME' : '','DOB' : '','ZodiacSign' : ''}
    Dictionary1[count] ['FullNAME'] = username
    Dictionary1[count] ['DOB'] = str(fulldate)
    Dictionary1[count] ['ZodiacSign'] = yoursign

    print(Dictionary1[count])

# def SavetoPandas():
#     pass
if __name__=='__main__':
    repeat = True
    count = 1
    while repeat == True:
        UserInput(count)
        count +=1
        repeat = repQuestion()
    df = pandas.DataFrame(data=Dictionary1)
    filename = input('PLEASE ENTER FILE NAME :')
    saveData = df.to_csv(filename+'.csv', index = True)
    print(df)
