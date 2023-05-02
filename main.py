def AchieveCertainPercentagePerSubject(targetPercentage, totalWorkingDays, presentDays):
    targetPercentage = targetPercentage / 100
    numberOfDaysToAttendClasses = (
        (totalWorkingDays * targetPercentage) - presentDays
    ) / (1 - targetPercentage)
    return numberOfDaysToAttendClasses


def MaxAchievableAttendance(totalWorkingDays, presentDays, tenure):
    return (presentDays + tenure) / (totalWorkingDays + tenure)


def menu():
    print("Enter 1 for achieving particular percentage in a subject")
    print("Enter 2 to get Maximum achievable Percentage")


if __name__ == "__main__":
    menu()
    try:
        choice = int(input(":"))
        if choice == 1:
            # AchieveCertainPercentagePerSubject
            targetPercentage = int(input("Target % (like 80) : "))
            totalWorkingDays = int(input("Total Working Days (Old) : "))
            presentDays = int(input("How many days we attended classes : "))
            ans = AchieveCertainPercentagePerSubject(
                targetPercentage=targetPercentage,
                totalWorkingDays=totalWorkingDays,
                presentDays=presentDays,
            )
            print(
                f"We need to attend {int(ans)} classes continuously to achieve {targetPercentage} percent attendance "
            )
        elif choice == 2:
            # MaxAchievableAttendance
            totalWorkingDays = int(input("Total Working Days (Old) : "))
            presentDays = int(input("How many days we attended classes : "))
            tenure = int(input("Calculate for how many days? : "))
            ans = MaxAchievableAttendance(totalWorkingDays, presentDays, tenure)
            ans = "{:0.2f}".format(ans * 100)
            print(
                f"If we go to college everyday for {tenure} days we can achieve {ans}  percent attendance"
            )
        else:
            print("Please Enter a valid option")
    except Exception:
        print("Some Internal Error Ocurred !")
