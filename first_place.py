'''Programmer : Emily Morales
Description : Write a program that asks for the names of three runners and the time it took each of them to ﬁnish a race. The program should display who came in ﬁrst, second, and third place.
Think about how many test cases are needed to verify that your problem works correctly.
Date : 06/26/20'''



runner1 = "Connor"
runner2 = "Seiry"
runner3 = "Emily"

runner1 = str(input("Please enter runner one name:"))
runnertime = float(input("Enter runner's race time:"))
runner2 = str(input("Please enter runner two name:"))
runnerTime = float(input("Enter runner's race time:"))
runner3 = str(input("Please enter runner three name:"))
RunnerTime = float(input("Enter runner's race time:"))


if (runnertime < runnerTime < RunnerTime):
    print(str(runner1 +' ' "finished race in 1st place," +" " +runner2 +" " +str("finished the race 2nd place,") +" " +runner3 +" " +str("3rd place.")))
elif (RunnerTime < runnerTime < runnertime):
    print(str(runner3 +" " "finished race in 1st place," +" " +runner2 +" "+str("finished the race 2nd place,") +" " + runner1 +" "+str("3rd place.")))
elif (runnerTime < RunnerTime < runnertime):
     print(str(runner2 +" " "finished race in 1st place," +" " +runner3 +" "+str("finished the race 2nd place,") +" " + runner1 + " "+str("3rd place.")))
elif (runnertime > RunnerTime > runnerTime):
    print(str(runner1 +" " "finished race in 1st place," +" " +runner3 +" "+str("finished the race 2nd place,") +" " + runner1 + " "+str(" 3rd place.")))
elif (runnertime < RunnerTime < runnerTime):
    print(str(runner1 +' ' "finished race in 1st place," +" " +runner3 +"  "+str("finished the race 2nd place,") +" " + runner2 +" "+str("3rd place.")))
else :
    print(str(runner3 +' ' +str("finished race in 1st place,")+' ' +runner1 +" "+str("finished the race 2nd place,") + ' ' +runner2 + " "+str("3rd place.")))
