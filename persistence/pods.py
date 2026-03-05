#pod functions
import random as rand

#Using the number of people creates a number of pods to contain those people
def create_pods(people):
    length = len(people)
    total_pods = 0
    if length > 5:
        remainder = length % 4
        four_pods = 0
        three_pods = 0
        if remainder == 0:
            four_pods = length//4
            three_pods = 0
            total_pods = four_pods + three_pods
        elif remainder == 1:
            four_pods = (length-1)//4 - 2
            three_pods = 3
            total_pods = four_pods + three_pods
        elif remainder == 2:
            four_pods = (length-2)//4 - 1
            three_pods= 2
            total_pods = four_pods + three_pods
        elif remainder == 3:
            four_pods = (length-3)//4
            three_pods = 1
            total_pods = four_pods + three_pods
        return three_pods, four_pods, total_pods
    elif length >= 3:
        total_pods = 1
        return 0, 0, total_pods
    else:
        return 0, 0, 0

#Runs threw every player and assigns them to a random pod 
def assign_pods(three_pods, four_pods, total_pods, people):
    pods = []
    i = 0
    while i < total_pods:
        if i < four_pods:
            pods.append([None,None,None,None])
        elif (i - four_pods) < three_pods:
            pods.append([None, None,None, "Empty"])
        i += 1
    
    position = 0
    cur_pod = 0
    while people and cur_pod < len(pods):
        if cur_pod < four_pods:
            index = rand.randint(0,len(people)-1)
            temp = people[index]
            people.pop(index)
            pods[cur_pod][position] = temp
            position += 1
            if position >= 4:
                position = 0
                cur_pod += 1
                continue
        elif (cur_pod - four_pods) < three_pods:
            index = rand.randint(0,len(people)-1)
            temp = people[index]
            people.pop(index)
            pods[cur_pod][position] = temp
            position += 1
            if position >= 3:
                position = 0
                cur_pod += 1
                continue
    return pods

#unfinished duplicate checking currently only checks if any pod member one repeats games.
def check_dups(pods, all_pods):
    rounds = len(all_pods)
    i = 0
    while (i < rounds):
        if (pods[0] == all_pods[i][0]):
            j = 1
            while(j < 4):
                if pods[j] == all_pods[i][j]:
                    return True
    return False

#changes up the pods so players play new groups
def shuffle_pods(pods, total_pods, all_pods):
    all_pods.append([row[:] for row in pods])
    temp_pods = [row[:] for row in pods]
    i = 0
    j = 0
    while i < total_pods:
        j = 0
        while j < 4:
            if i+j >= total_pods:
                pods[(i+j)-total_pods][j] = temp_pods[i][j]
            else:
                pods[i+j][j] = temp_pods[i][j]
            j+=1
        i+=1
    return pods, all_pods


#main function to run all the individual functions
def main():
    with open("names.txt") as f:
        people = [line.strip() for line in f.readlines()]

    pods = []
    all_pods = []
    three_pods, four_pods, total_pods = create_pods(people)
    pods = assign_pods(three_pods, four_pods, total_pods, people)
    print(pods)
    pods, all_pods = shuffle_pods(pods, total_pods, all_pods)
    print(pods)
    pods, all_pods = shuffle_pods(pods, total_pods, all_pods)
    print(pods)
    pods, all_pods = shuffle_pods(pods, total_pods, all_pods)
    print(pods)

main()
