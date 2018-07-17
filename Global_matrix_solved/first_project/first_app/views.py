from django.shortcuts import render
from . import forms
import numpy as np
# Create your views here.
BeamLengthList = []
PinSupLoc = []
RollerSupLoc = []
FixSupLoc = []
PointLoadLoc = []
PointMag = []
PointAngle = []
MomentLoc = []
MomentMag = []
UDLStartLoc = []
UDLEndLoc = []
UDLMag = []
NDLStartLoc = []
NDLEndLoc = []
NDLStartMag = []
NDLEndMag = []
def index(request):
    return render(request,'basicapp/index.html')

def myview(request):
    BeamForm = forms.BeamForm()

    if request.method == 'POST':
        BeamForm = forms.BeamForm(request.POST)
#display entered form on command pormpt (feedback)
        if BeamForm.is_valid():
            print("NAME: ", BeamForm.cleaned_data['BeamLength'])
            print("NAME: ", BeamForm.cleaned_data['Pin_Support_Location'])
            print("NAME: ", BeamForm.cleaned_data['Roller_Support_Location'])
            print("NAME: ", BeamForm.cleaned_data['Fixed_Support_Location'])
            print("NAME: ", BeamForm.cleaned_data['Point_Load_Location'])
            print("NAME: ", BeamForm.cleaned_data['Point_Magnitude'])
            print("NAME: ", BeamForm.cleaned_data['Point_Angle'])
            print("NAME: ", BeamForm.cleaned_data['Moment_Location'])
            print("NAME: ", BeamForm.cleaned_data['Moment_Magnitude'])
            print("NAME: ", BeamForm.cleaned_data['UDL_Start_Location'])
            print("NAME: ", BeamForm.cleaned_data['UDL_End_Location'])
            print("NAME: ", BeamForm.cleaned_data['UDL_Magnitude'])
            print("NAME: ", BeamForm.cleaned_data['NDL_Start_Location'])
            print("NAME: ", BeamForm.cleaned_data['NDL_End_Location'])
            print("NAME: ", BeamForm.cleaned_data['NDL_Start_Magnitude'])
            print("NAME: ", BeamForm.cleaned_data['NDL_End_Magnitude'])
#Assign form variable to backend
            BeamLength = BeamForm.cleaned_data['BeamLength']
            Pin_Support_Location = BeamForm.cleaned_data['Pin_Support_Location']
            Roller_Support_Location = BeamForm.cleaned_data['Roller_Support_Location']
            Fixed_Support_Location = BeamForm.cleaned_data['Fixed_Support_Location']
            Point_Load_Location = BeamForm.cleaned_data['Point_Load_Location']
            Point_Magnitude = BeamForm.cleaned_data['Point_Magnitude']
            Point_Angle = BeamForm.cleaned_data['Point_Angle']
            Moment_Location = BeamForm.cleaned_data['Moment_Location']
            Moment_Magnitude = BeamForm.cleaned_data['Moment_Magnitude']
            UDL_Start_Location = BeamForm.cleaned_data['UDL_Start_Location']
            UDL_End_Location = BeamForm.cleaned_data['UDL_End_Location']
            UDL_Magnitude = BeamForm.cleaned_data['UDL_Magnitude']
            NDL_Start_Location = BeamForm.cleaned_data['NDL_Start_Location']
            NDL_End_Location = BeamForm.cleaned_data['NDL_End_Location']
            NDL_Start_Magnitude = BeamForm.cleaned_data['NDL_Start_Magnitude']
            NDL_End_Magnitude = BeamForm.cleaned_data['NDL_End_Magnitude']
#Append further entry into list
            BeamLengthList.append(BeamLength)
            PinSupLoc.append(Pin_Support_Location)
            RollerSupLoc.append(Roller_Support_Location)
            FixSupLoc.append(Fixed_Support_Location)
            PointLoadLoc.append(Point_Load_Location)
            PointMag.append(Point_Magnitude)
            PointAngle.append(Point_Angle)
            MomentLoc.append(Moment_Location)
            MomentMag.append(Moment_Magnitude)
            UDLStartLoc.append(UDL_Start_Location)
            UDLEndLoc.append(UDL_End_Location)
            UDLMag.append(UDL_Magnitude)
            NDLStartLoc.append(NDL_Start_Location)
            NDLEndLoc.append(NDL_End_Location)
            NDLStartMag.append(NDL_Start_Magnitude)
            NDLEndMag.append(NDL_End_Magnitude)
#convert list to float
            map(float,BeamLengthList)
            map(float,PinSupLoc)
            map(float,RollerSupLoc)
            map(float,FixSupLoc)
            map(float,PointLoadLoc)
            map(float,PointMag)
            map(float,PointAngle)
            map(float,MomentLoc)
            map(float,MomentMag)
            map(float,UDLStartLoc)
            map(float,UDLEndLoc)
            map(float,UDLMag)
            map(float,NDLStartLoc)
            map(float,NDLEndLoc)
            map(float,NDLStartMag)
            map(float,NDLEndMag)


#elements list consist of Pin sup and Roller sup location
            elements = PinSupLoc + RollerSupLoc
            print("Current list:",PinSupLoc,RollerSupLoc)
            elements = list(filter(None,elements))

#Append Beam length list for and "0" into elements, these are the features which determines number of elements
            elements.append(float(BeamLengthList[0])) #error at this
            elements.append( 0 )
            elements.sort()
            print("Elements list; 0, PinSupLoc, RollerSupLoc and Beam length:",elements)
            print("Number of elements:",len(elements) - 1)


#Segmentize elements
            p2 = 0
            elements1 = []
            #Formula for number of element
            z1 = len(elements) - 1
            #Taking 2nd point in beam - first point in beam to get local beamlength
            while z1> 0:
                elements2 = float(elements[p2+1]) - float(elements[p2])
                p2 += 1
                z1 -= 1
                elements1.append(elements2)

            #elements1 is list of local beamlength
            print("elements1 IS HREE!!!",elements1)

            #matrix elements#
            z = len(elements) - 1
            x = 1
            p = 0
            CounterA = 0
            Currentcount = 0
            StoreA = []
            Mlist = []
            while z> 0:
                A = np.array([
                [12/float(elements1[p])**3,6/float(elements1[p])**2,-12/float(elements1[p])**3,6/float(elements1[p])**2],
                [6/float(elements1[p])**2,4/float(elements1[p]),-6/float(elements1[p])**2,2/float(elements1[p])],
                [-12/float(elements1[p])**3,-6/float(elements1[p])**2,12/float(elements1[p])**3,-6/float(elements1[p])**2],
                [6/float(elements1[p])**2,2/float(elements1[p]),-6/float(elements1[p])**2,4/float(elements1[p])]
                ])
                CounterA += 1
                StoreA.append(CounterA)
                Currentcount = StoreA[-1]
                print("Current count is:", Currentcount)
                Mlist.append(A)
                print("Local stiffness matrix of element",x ,"\n",A)
                print("current element length: ",elements1[p])
                z = z - 1
                x = x + 1
                p = p + 1
                print("List of Local stiffness matrix are:\n",Mlist,"\n")
            #Global matrix
            A1 = 2
            A2 = Currentcount
            A3 = Currentcount*2
            A4 = 1
            A5 = 6
            A6 = 2
            A7 = 3

            GlobalM = np.zeros(shape=((A3)+2,(A3)+2))

            GlobalM1 = GlobalM
            #Assigning first matrix into emty matrix of 0
            GlobalM1[:4,:4] = Mlist[0][:4,:4]
            #adding the rest of matrix into global matrix
            while 1:
                #[2:5,2:5]
                GlobalM1[A1:A5,A1:A5] = Mlist[A4][:4,:4]
                #3,3
                GlobalM1[A6,A6] = Mlist[A4][0,0] + Mlist[A4-1][2,2]
                #3,4,2,3
                GlobalM1[A6,A7] = Mlist[A4][0,1] + Mlist[A4-1][2,3]
                #4,3

                GlobalM1[A7,A6] = Mlist[A4][1,0] + Mlist[A4-1][3,2]
                #4,4
                GlobalM1[A7,A7] = Mlist[A4][1,1] + Mlist[A4-1][3,3]
                A1 += 2
                A5 += 2
                A4 += 1
                A6 += 2
                A7 += 2

                if A4 == A2:
                    break
            print("The global matrix is:\n",GlobalM1)

    return render(request,'first_app/index.html',{'BeamView':BeamForm})
