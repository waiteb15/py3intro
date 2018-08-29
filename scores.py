#!/usr/bin/env python


datascores={}
with open('DATA/testscores.dat') as scores_in:
    for raw_line in scores_in:
        (name, score) = raw_line.rstrip('\n\r').split(":")
        score = int(score)
        if score >= 95:
            letter_grade = 'A'
        elif score < 95 or score >= 89:
            letter_grade = 'B'
        elif score < 89 or score >= 83:
            letter_grade = 'C'
        elif score < 83 or score >= 75:
            letter_grade = 'D'
        elif score < 75 :
            letter_grade = 'F'
        datascores[name] = score , letter_grade

count = 0
total = 0
new_list =  sorted(datascores.items())
for name, item in new_list:
    print(name, item[0], item[1])
    count += 1
    total += item[0]

average = total/count

print(f"\n The average score of the class is {average:0.2f}\n")
