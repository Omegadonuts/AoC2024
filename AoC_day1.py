inputfilepath = r"C:\Users\Jan\Downloads\input1.txt"

firstNumbers = []
secondNumbers = []

with open(inputfilepath, 'r', encoding='utf-8') as infile:
    for line in infile:
        firstDig = int(line.split()[0])
        secondDig = int(line.split()[1])
        firstNumbers.append(firstDig)
        secondNumbers.append(secondDig)
        pass

def calc_distance_sum():
    firstNumbers.sort()
    secondNumbers.sort()
    counter = 0
    sum = 0
    if len(firstNumbers) == len(secondNumbers):
        for element in firstNumbers:
            distance = abs(secondNumbers[counter]-element)
            sum = sum+distance
            counter = counter+1
    return sum

print('distance sum: ' + str(calc_distance_sum()))

def calc_similarity_score():
    times = 0
    sim_score = 0
    for number in firstNumbers:
        times = secondNumbers.count(number)
        sim_score = sim_score + (number * times)

    return sim_score

print('similarity score: '+ str(calc_similarity_score()))