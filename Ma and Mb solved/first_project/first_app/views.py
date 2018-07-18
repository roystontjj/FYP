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

BeamLengthList0 = []
PinSupLoc0 = []
RollerSupLoc0 = []
FixSupLoc0 = []
PointLoadLoc0 = []
PointMag0 = []
PointAngle0 = []
MomentLoc0 = []
MomentMag0 = []
UDLStartLoc0 = []
UDLEndLoc0 = []
UDLMag0 = []
NDLStartLoc0 = []
NDLEndLoc0 = []
NDLStartMag0 = []
NDLEndMag0 = []
def index(request):
    return render(request,'basicapp/index.html')

def myview(request):
    BeamForm = forms.BeamForm()

    if request.method == 'POST':
        BeamForm = forms.BeamForm(request.POST)
#display entered form on command pormpt (feedback)
        if BeamForm.is_valid():
            '''print("NAME: ", BeamForm.cleaned_data['BeamLength'])
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
            print("NAME: ", BeamForm.cleaned_data['NDL_End_Magnitude'])'''
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
            BeamLengthList0.append(BeamLength)
            PinSupLoc0.append(Pin_Support_Location)
            RollerSupLoc0.append(Roller_Support_Location)
            FixSupLoc0.append(Fixed_Support_Location)
            PointLoadLoc0.append(Point_Load_Location)
            PointMag0.append(Point_Magnitude)
            PointAngle0.append(Point_Angle)
            MomentLoc0.append(Moment_Location)
            MomentMag0.append(Moment_Magnitude)
            UDLStartLoc0.append(UDL_Start_Location)
            UDLEndLoc0.append(UDL_End_Location)
            UDLMag0.append(UDL_Magnitude)
            NDLStartLoc0.append(NDL_Start_Location)
            NDLEndLoc.append(NDL_End_Location)
            NDLStartMag0.append(NDL_Start_Magnitude)
            NDLEndMag0.append(NDL_End_Magnitude)

            BeamLengthList = list(filter(None,BeamLengthList0))
            PinSupLoc = list(filter(None,PinSupLoc0))
            RollerSupLoc = list(filter(None,RollerSupLoc0))
            FixSupLoc = list(filter(None,FixSupLoc0))
            PointLoadLoc = list(filter(None,PointLoadLoc0))
            PointMag = list(filter(None,PointMag0))
            PointAngle = list(filter(None,PointAngle0))
            MomentLoc = list(filter(None,MomentLoc0))
            MomentMag = list(filter(None,MomentMag0))
            UDLStartLoc = list(filter(None,UDLStartLoc0))
            UDLEndLoc = list(filter(None,UDLEndLoc0))
            UDLMag = list(filter(None,UDLMag0))
            NDLStartLoc = list(filter(None,NDLStartLoc0))
            NDLEndloc = list(filter(None,NDLEndLoc0))
            NDLStartMag = list(filter(None,NDLStartMag0))
            NDLEndMag = list(filter(None,NDLEndMag0))

            '''print(BeamLengthList)
            print(PinSupLoc)
            print(RollerSupLoc)
            print(FixSupLoc)
            print(PointLoadLoc)
            print(PointMag)
            print(PointAngle)
            print(MomentLoc)
            print(MomentMag)
            print(UDLStartLoc)
            print(UDLEndLoc)
            print(UDLMag)
            print(NDLStartLoc)
            print(NDLEndloc)
            print(NDLStartMag)
            print(NDLEndMag)'''

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
            PinSupLoc1 = list(filter(None,PinSupLoc))
            elements = PinSupLoc + RollerSupLoc
            elements = list(filter(None,elements))

#Append Beam length list for and "0" into elements, these are the features which determines number of elements
            elements.append(float(BeamLengthList[0]))
            elements = list(filter(None,elements))
            elements.append( 0 )
            elements.sort()
            print("Elements list; 0, PinSupLoc, RollerSupLoc and Beam length [elements]:",elements)
            print("Number of elements: ",len(elements) - 1)


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
            print("Interval between elements [elements1]: ",elements1)

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
            print("===================================== GLOBAL MATRIX SOLVED============================ \n\n")

            print("Point load to Moment A calculation\n")
            """print("Separate pointLoad locations into individual elements list\n")"""
            #Pointload location seperate into list
            PointMag2 = PointMag
            PointMag2 = list(filter(None,PointMag2))
            CountPointMag = len(PointMag2)
            NumElements = len(elements) - 1
            Pointelements2 = elements
            PointElementList = []
            PointIndicator1 = 0
            PointIndicator2 = 1
            PointLoadIndicator = 0
            CounterPointList = 1
            CountListOfList = 0
            PointLoadLoc1 = PointLoadLoc
            PointLoadLoc1 = list(filter(None,PointLoadLoc1))
            AscendingPointLoadLoc = sorted(PointLoadLoc1)
            AscendingPointLoadLoc = list(filter(None,AscendingPointLoadLoc))

            print('No.elements [NumElements]: ',NumElements,"| Elements locations [Pointelements2]: ",Pointelements2,"|Elements interval [elements1]: ",elements1)
            print("No.Point loads [CountPointMag]: ",CountPointMag," | Point load Magnitude [PointMag2]: ",PointMag2," @ Point load location [AscendingPointLoadLoc]: ",AscendingPointLoadLoc)
            print("Creating same number of list as elements [ListOflist]")
            #Create list of list based on number of elements
            ListOfList = [[] for i in range(NumElements)]
            if len(AscendingPointLoadLoc) > 0:
                while CountPointMag > 0:
                    if Pointelements2[PointIndicator1] < AscendingPointLoadLoc[PointLoadIndicator] < Pointelements2[PointIndicator2]:
                        ListOfList[CountListOfList].append(AscendingPointLoadLoc[PointLoadIndicator])
                        PointLoadIndicator += 1
                        CountPointMag -=1
                    elif AscendingPointLoadLoc[PointLoadIndicator] > elements[PointIndicator2]:
                        CountListOfList += 1
                        PointIndicator1 += 1
                        PointIndicator2 += 1
                    elif AscendingPointLoadLoc[PointLoadIndicator] <elements[PointIndicator1]:
                        PointIndicator1 -= 1
                        PointIndicator2 -= 1
                    else:
                        pass
                print("Number of element lists [ListOfList]: ",ListOfList)
            else:
                pass

            #==============convert point load into fixed end Moment (Ma)===================
            #rename so can use in while loop locally
            PointMag1 = PointMag
            PointMag1 = list(filter(None,PointMag1))
            Pointelements = elements
            PointLoadLoc1 = list(filter(None,PointLoadLoc))
            #align force and location after sorting with zip
            PointSortedZip = sorted(zip(PointLoadLoc1,PointMag1))
            PointListOfList = [list(t) for t in zip(*PointSortedZip)]
            #list for point load @ Ma for each element
            PointMa = [[] for i in range(NumElements)]

            #counters for while loop sA
            sA = 0
            sB = 1
            PointForce = 0
            CountPointMag1A = len(PointMag1)

            print("PointSortedZip:" ,PointSortedZip)
            print("len(PointLoadLoc1): ",len(PointLoadLoc1))
            print("PointListOfList: ", PointListOfList)

            if len(PointLoadLoc1) > 0:
                while CountPointMag1A > 0:
                    if Pointelements[sA] < PointListOfList[0][PointForce] < Pointelements[sB] and len(PointLoadLoc) > 0:
                        print("PointLoadLoc[sA]: ",PointLoadLoc[PointForce])
                        print("PointListOfList[1][PointForce]: ",PointListOfList[1][PointForce])
                        print("Point Ma = (",PointListOfList[1][PointForce],"*(",Pointelements[sB],"-",PointListOfList[0][PointForce],")^2(",PointListOfList[0][PointForce],"-",Pointelements[sA],"))/(",Pointelements[sB],"-",Pointelements[sA],")^2")

                        PointMAformula = (PointListOfList[1][PointForce]*(Pointelements[sB]-PointListOfList[0][PointForce])**2*(PointListOfList[0][PointForce]-Pointelements[sA]))/((Pointelements[sB]-Pointelements[sA])**2)
                        PointMa[sA].append(PointMAformula)
                        CountPointMag1A -= 1
                        PointForce += 1

                    elif PointListOfList[0][PointForce] > Pointelements[sB]:
                        sA += 1
                        sB += 1
                    elif PointListOfList[0][PointForce] < Pointelements[sB]:
                        sA -= 1
                        sB -= 1
                    else:
                        pass
                    print("PointMa: ",PointMa)
                    print("====================================== Ma solved =============================================\n\n")
            else:
                pass

            #==============convert point load into fixed end Moment (Mb)===================
            #rename so can use in while loop locally
            PointMag1 = PointMag
            PointMag1 = list(filter(None,PointMag1))
            Pointelements = elements
            PointLoadLoc1 = list(filter(None,PointLoadLoc))
            #align force and location after sorting with zip
            PointSortedZip = sorted(zip(PointLoadLoc1,PointMag1))
            PointListOfList = [list(t) for t in zip(*PointSortedZip)]
            #list for point load @ Ma for each element
            PointMb = [[] for i in range(NumElements)]

            #counters for while loop sA
            sA = 0
            sB = 1
            PointForce = 0
            CountPointMag1A = len(PointMag1)

            print("PointSortedZip:" ,PointSortedZip)
            print("len(PointLoadLoc1): ",len(PointLoadLoc1))
            print("PointListOfList: ", PointListOfList)

            if len(PointLoadLoc1) > 0:
                while CountPointMag1A > 0:
                    if Pointelements[sA] < PointListOfList[0][PointForce] < Pointelements[sB] and len(PointLoadLoc) > 0:
                        print("PointLoadLoc[sA]: ",PointLoadLoc[PointForce])
                        print("PointListOfList[1][PointForce]: ",PointListOfList[1][PointForce])
                        print("Point Mb = (",PointListOfList[1][PointForce],"*(",Pointelements[sB],"-",PointListOfList[0][PointForce],")*(",PointListOfList[0][PointForce],"-",Pointelements[sA],")^2)/(",Pointelements[sB],"-",Pointelements[sA],")^2")

                        PointMAformula = (PointListOfList[1][PointForce]*(Pointelements[sB]-PointListOfList[0][PointForce])*(PointListOfList[0][PointForce]-Pointelements[sA])**2)/((Pointelements[sB]-Pointelements[sA])**2)
                        PointMb[sA].append(PointMAformula)
                        CountPointMag1A -= 1
                        PointForce += 1

                    elif PointListOfList[0][PointForce] > Pointelements[sB]:
                        sA += 1
                        sB += 1
                    elif PointListOfList[0][PointForce] < Pointelements[sB]:
                        sA -= 1
                        sB -= 1
                    else:
                        pass
                    print("PointMb: ",PointMb)
                    print("========================================== Mb solved ========================================\n\n")
            else:
                pass



            '''#convert UDL and NDL to PointLoad============
            #convert UDL to point load (UDLpoint)
            CountUDLPointLen = len(UDLMag)
            UDLindicator = 0
            UDLpointformulaList = []
            UDLpoint = []

            while CountUDLPointLen > 0:
                UDLpointformula = (UDLEndLoc[UDLindicator] - UDLStartLoc[UDLindicator])*UDLMag[UDLindicator]
                UDLpointformulaList.append(UDLpointformula)
                CountUDLPointLen -= 1
                UDLindicator += 1
                UDLpoint.append(UDLpointformulaList[-1])
            print(UDLpoint)

            #convert NDL to pointload (NDLpoint)
            NDLpoint = []
            CountPL = len(NDLStartMag)
            #NDL net increase
            CountPLDistance = len(NDLStartMag)
            CountNDLSign = 0
            NDLCentroidDistanceList = []
            NDLPointLoad = []
            NDLToUDL = []
            #distance from 0,0 to point load for Sharp NDL
            while CountPLDistance > 0:
                if (NDLStartMag[CountNDLSign] - NDLEndMag[CountNDLSign]) > 0:
                    NDLStartPositiveCentroidFormula = (((NDLEndLoc[CountNDLSign]-NDLStartLoc[CountNDLSign])/3) + NDLStartLoc[CountNDLSign])
                    NDLCentroidDistanceList.Append(NDLStartPositiveCentroidFormula)
                else:
                    NDLNegCentroidFormula = ((((NDLEndLoc[CountNDLSign]- NDLStartLoc[CountNDLSign])*2)/3)+NDLStartLoc[CountNDLSign])
                    NDLCentroidDistanceList.Append(NDLNegCentroidFormula)
                CountPLDistance -= 1
                CountNDLSign += 1
            #Point load for UDL and NDL
            while CountPL > 0:
                if NDLStartMag != 0 or NDLEndMag != 0:
                    #only for the sharp UDL
                    NDLPointLoadFormula = (abs(EndMag - NDLStartMag)*(NDLEndLoc-NDLStartLoc))/2
                    NDLPointLoad.Append(NDLPointLoadFormula)
                    #only for flat UDL
                    NDLToUDLFormula = NDLStartMag*(NDLEndLoc - NDLStartLoc)
                    NDLToUDL.Append(NDLToUDLFormula)
            #while CountNDLPointLen > 0:'''


    return render(request,'first_app/index.html',{'BeamView':BeamForm})
