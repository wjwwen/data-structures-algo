'''
Mentor List with Object-Oriented Programming (OOP)
'''

class Staff:
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept
    def __str__(self):
        return self.name + "(" + self.dept + ")"
    
mentorlist = []
mentorlist.append(Staff("Big Big Boss", "HQ"))
mentorlist.append(Staff("Big Boss", "HQ"))
mentorlist.append(Staff("2nd Boss", "HQ"))
mentorlist.append(Staff("3rd Boss", "HQ"))
mentorlist.append(Staff("Sales Director", "Sales"))
mentorlist.append(Staff("Financial Clerk", "Sales"))
mentorlist.append(Staff("CFO", "HQ"))

for each in mentorlist:
    print(each)
    
# print(mentorlist[2].dept)

def findStaff(staffNo):
    if type(staffNo) is str:
        for i in range(len(mentorlist)):
            if mentorlist[i].name == staffNo:
                staffNo = i
                break
    bossid = (staffNo-1)//3
    mm = staffNo*3+1
    mmnames = ""
    for y in range(3):
        if mm < len(mentorlist):
            mmnames += "\n\t\t\t" + mentorlist[mm].name
            mm += 1
    return f"""
    Staff: {mentorlist[staffNo]}
    reporting to: {mentorlist[bossid]}
    taking care of: {mmnames}
    """
    
print(findStaff(1))
print(findStaff("Big Boss"))