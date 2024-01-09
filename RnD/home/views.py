from django.shortcuts import render,redirect
from .models import table_info,project_details

# Create your views here.
period=0

def master_sheet(request):
    return render(request, "master_sheet.html")

def index(request):
    if request.method == "POST":
        Project_Fellowship_No =request.POST.get('Project_Fellowship_No')
        PI_of_Project = request.POST.get('PI_of_Project')
        Sanctioned_Date = request.POST.get('Sanctioned_Date')
        Project_Start_Date = request.POST.get('Project_Start_Date')
        Project_Closure_Date = request.POST.get('Project_Closure_Date')
        Title_of_Project = request.POST.get('Title_of_Project')

        start_year = ""
        for i in range(0,4):
            start_year = start_year + Project_Start_Date[i]

        closure_year = ""
        for i in range(0,4):
            closure_year = closure_year + Project_Closure_Date[i]

        period = int(closure_year)-int(start_year)

        details = project_details.objects.create(
            Project_Fellowship_No =Project_Fellowship_No,
            PI_of_Project = PI_of_Project,
            Sanctioned_Date = Sanctioned_Date,
            Project_Start_Date =Project_Start_Date, 
            Project_Closure_Date =Project_Closure_Date,
            Title_of_Project =Title_of_Project,
            project_duration = period
        )
        details.save()

        start_year=int(start_year)
        closure_year=int(closure_year)

        period_range = range(0, period)
        context = {'period': period, 'period_range': period_range}
        years = {'start_year':start_year, 'closure_year':closure_year}

        years_dict = {'context':context, 'years':years, 'fellowship_no':Project_Fellowship_No}

        return render(request,'monthly.html',years_dict)
        
    return render(request,'index.html')


def monthly(request):

    one_expenses=0
    three_expenses=0
    four_expenses=0
    five_expenses=0
    six_expenses=0
    two_expenses=0
    seven_expenses=0    

    total_grant=0 
    total_Apr = 0
    total_May = 0
    total_Jun = 0
    total_Jul = 0
    total_Aug = 0
    total_Sep = 0
    total_Oct = 0
    total_Nov = 0
    total_Dec = 0
    total_Jan = 0
    total_Feb = 0
    total_Mar = 0
    total_expenses = 0
    total_closing_balances = 0

    one_closing =0
    two_closing =0
    three_closing =0
    four_closing =0
    five_closing =0
    six_closing =0
    seven_closing =0
    
    if request.method == "POST":

        table_no = int(request.POST.get('table_no'))
        fellowship_no = request.POST.get('fellowship_no')
        one_Grant_Amount = int(request.POST.get('one_Grant_Amount') if request.POST.get('one_Grant_Amount')!="" else 0)
        one_Apr = int(request.POST.get('one_Apr') if request.POST.get('one_Apr')!="" else 0)
        one_May = int(request.POST.get('one_May') if request.POST.get('one_May')!="" else 0)
        one_Jun = int(request.POST.get('one_Jun') if request.POST.get('one_Jun')!="" else 0)
        one_Jul = int(request.POST.get('one_Jul') if request.POST.get('one_Jul')!="" else 0)
        one_Aug = int(request.POST.get('one_Aug') if request.POST.get('one_Aug')!="" else 0)
        one_Sep = int(request.POST.get('one_Sep') if request.POST.get('one_Sep')!="" else 0)
        one_Oct = int(request.POST.get('one_Oct') if request.POST.get('one_Oct')!="" else 0)
        one_Nov = int(request.POST.get('one_Nov') if request.POST.get('one_Nov')!="" else 0)
        one_Dec = int(request.POST.get('one_Dec') if request.POST.get('one_Dec')!="" else 0)
        one_Jan = int(request.POST.get('one_Jan') if request.POST.get('one_Jan')!="" else 0)
        one_Feb = int(request.POST.get('one_Feb') if request.POST.get('one_Feb')!="" else 0)
        one_Mar = int(request.POST.get('one_Mar') if request.POST.get('one_Mar')!="" else 0)

        two_Grant_Amount = int(request.POST.get('two_Grant_Amount') if request.POST.get('two_Grant_Amount')!="" else 0)
        two_Apr = int(request.POST.get('two_Apr') if request.POST.get('two_Apr')!="" else 0)
        two_May = int(request.POST.get('two_May') if request.POST.get('two_May')!="" else 0)
        two_Jun = int(request.POST.get('two_Jun') if request.POST.get('two_Jun')!="" else 0)
        two_Jul = int(request.POST.get('two_Jul') if request.POST.get('two_Jul')!="" else 0)
        two_Aug = int(request.POST.get('two_Aug') if request.POST.get('two_Aug')!="" else 0)
        two_Sep = int(request.POST.get('two_Sep') if request.POST.get('two_Sep')!="" else 0)
        two_Oct = int(request.POST.get('two_Oct') if request.POST.get('two_Oct')!="" else 0)
        two_Nov = int(request.POST.get('two_Nov') if request.POST.get('two_Nov')!="" else 0)
        two_Dec = int(request.POST.get('two_Dec') if request.POST.get('two_Dec')!="" else 0)
        two_Jan = int(request.POST.get('two_Jan') if request.POST.get('two_Jan')!="" else 0)
        two_Feb = int(request.POST.get('two_Feb') if request.POST.get('two_Feb')!="" else 0)
        two_Mar = int(request.POST.get('two_Mar') if request.POST.get('two_Mar')!="" else 0)

        three_Grant_Amount = int(request.POST.get('three_Grant_Amount') if request.POST.get('three_Grant_Amount')!="" else 0)
        three_Apr = int(request.POST.get('three_Apr') if request.POST.get('three_Apr')!="" else 0)
        three_May = int(request.POST.get('three_May') if request.POST.get('three_May')!="" else 0)
        three_Jun = int(request.POST.get('three_Jun') if request.POST.get('three_Jun')!="" else 0)
        three_Jul = int(request.POST.get('three_Jul') if request.POST.get('three_Jul')!="" else 0)
        three_Aug = int(request.POST.get('three_Aug') if request.POST.get('three_Aug')!="" else 0)
        three_Sep = int(request.POST.get('three_Sep') if request.POST.get('three_Sep')!="" else 0)
        three_Oct = int(request.POST.get('three_Oct') if request.POST.get('three_Oct')!="" else 0)
        three_Nov = int(request.POST.get('three_Nov') if request.POST.get('three_Nov')!="" else 0)
        three_Dec = int(request.POST.get('three_Dec') if request.POST.get('three_Dec')!="" else 0)
        three_Jan = int(request.POST.get('three_Jan') if request.POST.get('three_Jan')!="" else 0)
        three_Feb = int(request.POST.get('three_Feb') if request.POST.get('three_Feb')!="" else 0)
        three_Mar = int(request.POST.get('three_Mar') if request.POST.get('three_Mar')!="" else 0)

        four_Grant_Amount = int(request.POST.get('four_Grant_Amount') if request.POST.get('four_Grant_Amount')!="" else 0)
        four_Apr = int(request.POST.get('four_Apr') if request.POST.get('four_Apr')!="" else 0)
        four_May = int(request.POST.get('four_May') if request.POST.get('four_May')!="" else 0)
        four_Jun = int(request.POST.get('four_Jun') if request.POST.get('four_Jun')!="" else 0)
        four_Jul = int(request.POST.get('four_Jul') if request.POST.get('four_Jul')!="" else 0)
        four_Aug = int(request.POST.get('four_Aug') if request.POST.get('four_Aug')!="" else 0)
        four_Sep = int(request.POST.get('four_Sep') if request.POST.get('four_Sep')!="" else 0)
        four_Oct = int(request.POST.get('four_Oct') if request.POST.get('four_Oct')!="" else 0)
        four_Nov = int(request.POST.get('four_Nov') if request.POST.get('four_Nov')!="" else 0)
        four_Dec = int(request.POST.get('four_Dec') if request.POST.get('four_Dec')!="" else 0)
        four_Jan = int(request.POST.get('four_Jan') if request.POST.get('four_Jan')!="" else 0)
        four_Feb = int(request.POST.get('four_Feb') if request.POST.get('four_Feb')!="" else 0)
        four_Mar = int(request.POST.get('four_Mar') if request.POST.get('four_Mar')!="" else 0)

        five_Grant_Amount = int(request.POST.get('five_Grant_Amount') if request.POST.get('five_Grant_Amount')!="" else 0)
        five_Apr = int(request.POST.get('five_Apr') if request.POST.get('five_Apr')!="" else 0)
        five_May = int(request.POST.get('five_May') if request.POST.get('five_May')!="" else 0)
        five_Jun = int(request.POST.get('five_Jun') if request.POST.get('five_Jun')!="" else 0)
        five_Jul = int(request.POST.get('five_Jul') if request.POST.get('five_Jul')!="" else 0)
        five_Aug = int(request.POST.get('five_Aug') if request.POST.get('five_Aug')!="" else 0)
        five_Sep = int(request.POST.get('five_Sep') if request.POST.get('five_Sep')!="" else 0)
        five_Oct = int(request.POST.get('five_Oct') if request.POST.get('five_Oct')!="" else 0)
        five_Nov = int(request.POST.get('five_Nov') if request.POST.get('five_Nov')!="" else 0)
        five_Dec = int(request.POST.get('five_Dec') if request.POST.get('five_Dec')!="" else 0)
        five_Jan = int(request.POST.get('five_Jan') if request.POST.get('five_Jan')!="" else 0)
        five_Feb = int(request.POST.get('five_Feb') if request.POST.get('five_Feb')!="" else 0)
        five_Mar = int(request.POST.get('five_Mar') if request.POST.get('five_Mar')!="" else 0)

        six_Grant_Amount = int(request.POST.get('six_Grant_Amount') if request.POST.get('six_Grant_Amount')!="" else 0)
        six_Apr = int(request.POST.get('six_Apr') if request.POST.get('six_Apr')!="" else 0)
        six_May = int(request.POST.get('six_May') if request.POST.get('six_May')!="" else 0)
        six_Jun = int(request.POST.get('six_Jun') if request.POST.get('six_Jun')!="" else 0)
        six_Jul = int(request.POST.get('six_Jul') if request.POST.get('six_Jul')!="" else 0)
        six_Aug = int(request.POST.get('six_Aug') if request.POST.get('six_Aug')!="" else 0)
        six_Sep = int(request.POST.get('six_Sep') if request.POST.get('six_Sep')!="" else 0)
        six_Oct = int(request.POST.get('six_Oct') if request.POST.get('six_Oct')!="" else 0)
        six_Nov = int(request.POST.get('six_Nov') if request.POST.get('six_Nov')!="" else 0)
        six_Dec = int(request.POST.get('six_Dec') if request.POST.get('six_Dec')!="" else 0)
        six_Jan = int(request.POST.get('six_Jan') if request.POST.get('six_Jan')!="" else 0)
        six_Feb = int(request.POST.get('six_Feb') if request.POST.get('six_Feb')!="" else 0)
        six_Mar = int(request.POST.get('six_Mar') if request.POST.get('six_Mar')!="" else 0)

        seven_Grant_Amount = int(request.POST.get('seven_Grant_Amount') if request.POST.get('seven_Grant_Amount')!="" else 0)
        seven_Apr = int(request.POST.get('seven_Apr') if request.POST.get('seven_Apr')!="" else 0)
        seven_May = int(request.POST.get('seven_May') if request.POST.get('seven_May')!="" else 0)
        seven_Jun = int(request.POST.get('seven_Jun') if request.POST.get('seven_Jun')!="" else 0)
        seven_Jul = int(request.POST.get('seven_Jul') if request.POST.get('seven_Jul')!="" else 0)
        seven_Aug = int(request.POST.get('seven_Aug') if request.POST.get('seven_Aug')!="" else 0)
        seven_Sep = int(request.POST.get('seven_Sep') if request.POST.get('seven_Sep')!="" else 0)
        seven_Oct = int(request.POST.get('seven_Oct') if request.POST.get('seven_Oct')!="" else 0)
        seven_Nov = int(request.POST.get('seven_Nov') if request.POST.get('seven_Nov')!="" else 0)
        seven_Dec = int(request.POST.get('seven_Dec') if request.POST.get('seven_Dec')!="" else 0)
        seven_Jan = int(request.POST.get('seven_Jan') if request.POST.get('seven_Jan')!="" else 0)
        seven_Feb = int(request.POST.get('seven_Feb') if request.POST.get('seven_Feb')!="" else 0)
        seven_Mar = int(request.POST.get('seven_Mar') if request.POST.get('seven_Mar')!="" else 0)

        column1 = [one_Apr,two_Apr,three_Apr,four_Apr,five_Apr,six_Apr,seven_Apr]
        column2 = [one_May,two_May,three_May,four_May,five_May,six_May,seven_May]
        column3 = [one_Jun,two_Jun,three_Jun,four_Jun,five_Jun,six_Jun,seven_Jun]
        column4 = [one_Jul,two_Jul,three_Jul,four_Jul,five_Jul,six_Jul,seven_Jul]
        column5 = [one_Aug,two_Aug,three_Aug,four_Aug,five_Aug,six_Aug,seven_Aug]
        column6 = [one_Sep,two_Sep,three_Sep,four_Sep,five_Sep,six_Sep,seven_Sep]
        column7 = [one_Oct,two_Oct,three_Oct,four_Oct,five_Oct,six_Oct,seven_Oct]
        column8 = [one_Nov,two_Nov,three_Nov,four_Nov,five_Nov,six_Nov,seven_Nov]
        column9 = [one_Dec,two_Dec,three_Dec,four_Dec,five_Dec,six_Dec,seven_Dec]
        column10 = [one_Jan,two_Jan,three_Jan,four_Jan,five_Jan,six_Jan,seven_Jan]
        column11 = [one_Feb,two_Feb,three_Feb,four_Feb,five_Feb,six_Feb,seven_Feb]
        column12 = [one_Mar,two_Mar,three_Mar,four_Mar,five_Mar,six_Mar,seven_Mar]

        row1 = [one_Apr,one_May,one_Jun,one_Jul,one_Aug,one_Sep,one_Oct,one_Nov,one_Dec]
        row2 = [two_Apr,two_May,two_Jun,two_Jul,two_Aug,two_Sep,two_Oct,two_Nov,two_Dec]
        row3 = [three_Apr,three_May,three_Jun,three_Jul,three_Aug,three_Sep,three_Oct,three_Nov,three_Dec]
        row4 = [four_Apr,four_May,four_Jun,four_Jul,four_Aug,four_Sep,four_Oct,four_Nov,four_Dec]
        row5 = [five_Apr,five_May,five_Jun,five_Jul,five_Aug,five_Sep,five_Oct,five_Nov,five_Dec]
        row6 = [six_Apr,six_May,six_Jun,six_Jul,six_Aug,six_Sep,six_Oct,six_Nov,six_Dec]
        row7 = [seven_Apr,seven_May,seven_Jun,seven_Jul,seven_Aug,seven_Sep,seven_Oct,seven_Nov,seven_Dec]

        columns = [column1,column2,column3,column4,column5,column6,column7,column8,column9,column10,column11,column12]
        rows = [row1,row2,row3,row4,row5,row6,row7]

        for i,row in enumerate(rows):
            for j, value in enumerate(row):
                if i==0:
                    one_expenses=one_expenses+value
                elif i==1:
                    two_expenses=two_expenses+value
                elif i==2:
                    three_expenses=three_expenses+value
                elif i==3:
                    four_expenses=four_expenses+value
                elif i==4:
                    five_expenses=five_expenses+value
                elif i==5:
                    six_expenses=six_expenses+value
                elif i==6:
                    seven_expenses=seven_expenses+value
                

        expenses_column = [one_expenses,two_expenses,three_expenses,four_expenses,five_expenses,six_expenses,seven_expenses]
        grants_cloumn = [one_Grant_Amount,two_Grant_Amount,three_Grant_Amount,four_Grant_Amount,five_Grant_Amount,six_Grant_Amount,seven_Grant_Amount]

        # print(expenses_column)
        for i in grants_cloumn:
            total_grant=total_grant+i

        one_closing=one_closing+one_Grant_Amount-one_expenses
        two_closing=two_closing+two_Grant_Amount-two_expenses
        three_closing=three_closing+three_Grant_Amount-three_expenses
        four_closing=four_closing+four_Grant_Amount-four_expenses
        five_closing=five_closing+five_Grant_Amount-five_expenses
        six_closing=six_closing+six_Grant_Amount-six_expenses
        seven_closing=seven_closing+seven_Grant_Amount-seven_expenses

        closing_balances_column = [one_closing,two_closing,three_closing,four_closing,five_closing,six_closing,seven_closing]
        # print(closing_balances_column)
        for i,column in enumerate(columns):
            for j, value in enumerate(column):
                if i==0:
                    total_Apr = total_Apr +value
                elif i==1:
                    total_May = total_May +value
                elif i==2:
                    total_Jun = total_Jun +value
                elif i==3:
                    total_Jul = total_Jul+value
                elif i==4:
                    total_Aug = total_Aug+value
                elif i==5:
                    total_Sep = total_Sep+value
                elif i==6:
                    total_Oct = total_Oct+value
                elif i==7:
                    total_Nov = total_Nov+value
                elif i==8:
                    total_Dec = total_Dec+value
                elif i==9:
                    total_Jan = total_Jan+value
                elif i==10:
                    total_Feb = total_Feb+value
                elif i==11:
                    total_Mar = total_Mar+value

        # print(total_Apr)

        for i in expenses_column:
            total_expenses=total_expenses+i
        
        for i in closing_balances_column:
            total_closing_balances=total_closing_balances+i
        
        sum_data = {
                'table_no' : table_no,
                'one_Grant_Amount' : one_Grant_Amount,
                'one_Apr' : one_Apr,
                'one_May' : one_May,
                'one_Jun' : one_Jun,
                'one_Jul' : one_Jul,
                'one_Aug' : one_Aug,
                'one_Sep' : one_Sep,
                'one_Oct' : one_Oct,
                'one_Nov' : one_Nov,
                'one_Dec' : one_Dec,
                'one_Jan' : one_Jan,
                'one_Feb' : one_Feb,
                'one_Mar' : one_Mar,
                'one_expenses' : one_expenses,
                'one_closing':one_closing,

                'two_Grant_Amount':two_Grant_Amount ,
                'two_Apr' : two_Apr,
                'two_May' : two_May,
                'two_Jun' : two_Jun,
                'two_Jul' : two_Jul,
                'two_Aug' : two_Aug,
                'two_Sep' : two_Sep,
                'two_Oct' : two_Oct,
                'two_Nov' : two_Nov,
                'two_Dec' : two_Dec,
                'two_Jan' : two_Jan,
                'two_Feb' : two_Feb,
                'two_Mar' : two_Mar,
                'two_expenses' : two_expenses,
                'two_closing':two_closing,

                'three_Grant_Amount' : three_Grant_Amount ,
                'three_Apr' : three_Apr,
                'three_May' : three_May,
                'three_Jun' : three_Jun,
                'three_Jul' : three_Jul,
                'three_Aug' : three_Aug,
                'three_Sep' : three_Sep,
                'three_Oct' : three_Oct,
                'three_Nov' : three_Nov,
                'three_Dec' : three_Dec,
                'three_Jan' : three_Jan,
                'three_Feb' : three_Feb,
                'three_Mar' : three_Mar,
                'three_expenses' : three_expenses,
                'three_closing':three_closing,

                'four_Grant_Amount' : four_Grant_Amount ,
                'four_Apr' : four_Apr,
                'four_May' : four_May,
                'four_Jun' : four_Jun,
                'four_Jul' : four_Jul,
                'four_Aug' : four_Aug,
                'four_Sep' : four_Sep,
                'four_Oct' : four_Oct,
                'four_Nov' : four_Nov,
                'four_Dec' : four_Dec,
                'four_Jan' : four_Jan,
                'four_Feb' : four_Feb,
                'four_Mar' : four_Mar,
                'four_expenses' : four_expenses,
                'four_closing':four_closing,

                'five_Grant_Amount' : five_Grant_Amount ,
                'five_Apr' : five_Apr,
                'five_May' : five_May,
                'five_Jun' : five_Jun,
                'five_Jul' : five_Jul,
                'five_Aug' : five_Aug,
                'five_Sep' : five_Sep,
                'five_Oct' : five_Oct,
                'five_Nov' : five_Nov,
                'five_Dec' : five_Dec,
                'five_Jan' : five_Jan,
                'five_Feb' : five_Feb,
                'five_Mar' : five_Mar,
                'five_expenses' : five_expenses,
                'five_closing':five_closing,

                'six_Grant_Amount' : six_Grant_Amount ,
                'six_Apr' : six_Apr,
                'six_May' : six_May,
                'six_Jun' : six_Jun,
                'six_Jul' : six_Jul,
                'six_Aug' : six_Aug,
                'six_Sep' : six_Sep,
                'six_Oct' : six_Oct,
                'six_Nov' : six_Nov,
                'six_Dec' : six_Dec,
                'six_Jan' : six_Jan,
                'six_Feb' : six_Feb,
                'six_Mar' : six_Mar,
                'six_expenses' : six_expenses,
                'six_closing':six_closing,

                'seven_Grant_Amount' : seven_Grant_Amount ,
                'seven_Apr' : seven_Apr,
                'seven_May' : seven_May,
                'seven_Jun' : seven_Jun,
                'seven_Jul' : seven_Jul,
                'seven_Aug' : seven_Aug,
                'seven_Sep' : seven_Sep,
                'seven_Oct' : seven_Oct,
                'seven_Nov' : seven_Nov,
                'seven_Dec' : seven_Dec,
                'seven_Jan' : seven_Jan,
                'seven_Feb' : seven_Feb,
                'seven_Mar' : seven_Mar,
                'seven_expenses' : seven_expenses,
                'seven_closing':seven_closing,

                'total_grant' : total_grant,
                'total_Apr': total_Apr,
                'total_May': total_May,
                'total_Jun': total_Jun,
                'total_Jul': total_Jul,
                'total_Aug': total_Aug,
                'total_Sep': total_Sep,
                'total_Oct': total_Oct,
                'total_Nov': total_Nov,
                'total_Dec': total_Dec,
                'total_Jan': total_Jan,
                'total_Feb': total_Feb,
                'total_Mar': total_Mar,
                'total_expenses':total_expenses,
                'total_closing_balances':total_closing_balances
        }

        entries = table_info.objects.create(
                table_no = table_no,
                one_Grant_Amount = one_Grant_Amount ,
                one_Apr = one_Apr,
                one_May = one_May,
                one_Jun = one_Jun,
                one_Jul = one_Jul,
                one_Aug = one_Aug,
                one_Sep = one_Sep,
                one_Oct = one_Oct,
                one_Nov = one_Nov,
                one_Dec = one_Dec,
                one_Jan = one_Jan,
                one_Feb = one_Feb,
                one_Mar = one_Mar,
                one_expenses = one_expenses,
                one_closing=one_closing,

                two_Grant_Amount = two_Grant_Amount ,
                two_Apr = two_Apr,
                two_May = two_May,
                two_Jun = two_Jun,
                two_Jul = two_Jul,
                two_Aug = two_Aug,
                two_Sep = two_Sep,
                two_Oct = two_Oct,
                two_Nov = two_Nov,
                two_Dec = two_Dec,
                two_Jan = two_Jan,
                two_Feb = two_Feb,
                two_Mar = two_Mar,
                two_expenses = two_expenses,
                two_closing=two_closing,

                three_Grant_Amount = three_Grant_Amount ,
                three_Apr = three_Apr,
                three_May = three_May,
                three_Jun = three_Jun,
                three_Jul = three_Jul,
                three_Aug = three_Aug,
                three_Sep = three_Sep,
                three_Oct = three_Oct,
                three_Nov = three_Nov,
                three_Dec = three_Dec,
                three_Jan = three_Jan,
                three_Feb = three_Feb,
                three_Mar = three_Mar,
                three_expenses = three_expenses,
                three_closing=three_closing,

                four_Grant_Amount = four_Grant_Amount ,
                four_Apr = four_Apr,
                four_May = four_May,
                four_Jun = four_Jun,
                four_Jul = four_Jul,
                four_Aug = four_Aug,
                four_Sep = four_Sep,
                four_Oct = four_Oct,
                four_Nov = four_Nov,
                four_Dec = four_Dec,
                four_Jan = four_Jan,
                four_Feb = four_Feb,
                four_Mar = four_Mar,
                four_expenses = four_expenses,
                four_closing=four_closing,

                five_Grant_Amount = five_Grant_Amount ,
                five_Apr = five_Apr,
                five_May = five_May,
                five_Jun = five_Jun,
                five_Jul = five_Jul,
                five_Aug = five_Aug,
                five_Sep = five_Sep,
                five_Oct = five_Oct,
                five_Nov = five_Nov,
                five_Dec = five_Dec,
                five_Jan = five_Jan,
                five_Feb = five_Feb,
                five_Mar = five_Mar,
                five_expenses = five_expenses,
                five_closing=five_closing,

                six_Grant_Amount = six_Grant_Amount ,
                six_Apr = six_Apr,
                six_May = six_May,
                six_Jun = six_Jun,
                six_Jul = six_Jul,
                six_Aug = six_Aug,
                six_Sep = six_Sep,
                six_Oct = six_Oct,
                six_Nov = six_Nov,
                six_Dec = six_Dec,
                six_Jan = six_Jan,
                six_Feb = six_Feb,
                six_Mar = six_Mar,
                six_expenses = six_expenses,
                six_closing=six_closing,

                seven_Grant_Amount = seven_Grant_Amount ,
                seven_Apr = seven_Apr,
                seven_May = seven_May,
                seven_Jun = seven_Jun,
                seven_Jul = seven_Jul,
                seven_Aug = seven_Aug,
                seven_Sep = seven_Sep,
                seven_Oct = seven_Oct,
                seven_Nov = seven_Nov,
                seven_Dec = seven_Dec,
                seven_Jan = seven_Jan,
                seven_Feb = seven_Feb,
                seven_Mar = seven_Mar,
                seven_expenses = seven_expenses,
                seven_closing=seven_closing,

                total_grant = total_grant,
                total_Apr = total_Apr,
                total_May = total_May,
                total_Jun= total_Jun,
                total_Jul=total_Jul,
                total_Aug= total_Aug,
                total_Sep = total_Sep,
                total_Oct = total_Oct,
                total_Nov = total_Nov,
                total_Dec = total_Dec,
                total_Jan = total_Jan,
                total_Feb = total_Feb,
                total_Mar = total_Mar,
                total_expenses=total_expenses,
                total_closing_balances=total_closing_balances
        )
        entries.save()

        projects = project_details.objects.filter(Project_Fellowship_No = str(fellowship_no))
        if projects.exists():
                
                project_duration = projects.first().project_duration
                period_range = range(0,project_duration)

                context = {'period_range':period_range}
                

                Project_Start_Date = str(projects.first().Project_Start_Date)
                Project_Closure_Date = str(projects.first().Project_Closure_Date)

                start_year = ""
                for i in range(0,4):
                    start_year = start_year + Project_Start_Date[i]

                closure_year = ""
                for i in range(0,4):
                    closure_year = closure_year + Project_Closure_Date[i]

                start_year=int(start_year)
                closure_year=int(closure_year)
                years = {'start_year':start_year, 'closure_year':closure_year}

                dictionary={'sum_data':sum_data,'context':context,'years':years,'table_no':table_no}

                return render(request,'monthly.html',dictionary)
        else:
            return redirect('/monthly') 
    
    return render(request,'monthly.html')

def homepage(request):
    return render(request, "homepage.html")         

def login(request):
    return render(request, "login.html")         


       
