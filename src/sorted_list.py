

words = ["Monday", "Tuesday", "Wednesday"]

months = ["January", "Febuary", "March"]

combined_list = []
#combined_list = separate_list.extend(months)
combined_list = words + months
#for w in words:
#    combined_list.append(w)

#for m in months:
#    combined_list.append(m)

print("combined_list", combined_list)

print("sorted words", sorted(words))


print("sorted months", sorted(months))


print("combined_list sorted", sorted(combined_list))


pattern1 = 'Febuary'
pattern2 = 'January'

result = ['Febuary', 'January', 'March', 'Monday', 'Tuesday', 'Wednesday','Febuary', 'January' ]

first = result[0]

for r in range(len(result[1:])):
    print("r is ", result[r])
    if first ==  pattern1 and result[r] == pattern2:
        print("we got pattern")

    #first = result[r]
    pattern1 = result[r]
    pattern2 = result[r+1]
    first = pattern1
    print("new pattern", pattern1, pattern2)


        
