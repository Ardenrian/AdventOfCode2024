import re

def ReadFile(fname):
    file = open(fname, "r")
    lines = [line for line in file]
    file.close()
    my_data = [re.findall(r"[\d]+", line) for line in lines]
    constraints = [line for line in my_data if len(line)==2]
    updates = [line for line in my_data if len(line)>2]
    return constraints, updates

def UpdateFollowConstraint(update, constraint):
    gotthesecond = False
    for number in update:
        if number == constraint[1]:
            gotthesecond = True
        if (number == constraint[0])&gotthesecond:
            #print(update)
            #print(constraint)
            return False
    return True

def UpdateFollowsConstraints(update, constraints):
    for constraint in constraints:
        if not(UpdateFollowConstraint(update, constraint)):
            return (False,constraint)
    return (True, [])

def MakeUpdatesCompliant(updates, constraints):
    for update in updates:
        (compliant, constraint) = UpdateFollowsConstraints(update, constraints)
        while not(compliant):
            (update, constraint) = TryToMakeMoreCompliant(update, constraint)
            (compliant, constraint) = UpdateFollowsConstraints(update, constraints)
    return updates


def TryToMakeMoreCompliant(update, constraint):
    secondIndex = -1
    for i in range(len(update)):
        if update[i] == constraint[1]:
            secondIndex = i
        if (update[i] == constraint[0]):
            data = update[i]
            update[i] = update[secondIndex]
            update[secondIndex] = data
    return (update, constraints)

def ReturnMiddleValue(update):
    return update[int(len(update)/2)]

(constraints, updates) = ReadFile("Advent5input.txt")
#compliantUpdates = [update for update in updates if UpdateFollowsConstraints(update,constraints)[0]]
nonComplantUpdates = [update for update in updates if not(UpdateFollowsConstraints(update,constraints))[0]]
madeCompliantupdates = MakeUpdatesCompliant(nonComplantUpdates, constraints)
#print(madeCompliantupdates)
middleValues = [int(ReturnMiddleValue(update)) for update in madeCompliantupdates]
print(sum(middleValues))


