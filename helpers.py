
def calculate_change(previous, current):
    if previous == 0 :
        print("fail")
    change = current - previous
    return change/previous

def growth(df,processor_name):
    growth = []
    for i in df:
        if i == 0:
            pass
        else :
            change = calculate_change(i-1, i)
            growth.append(change)

    growth_avg = sum(growth)/len(growth)
    print('avg {} growth.....'.format(processor_name))
    print(growth_avg)
    #print(growth)
    return growth_avg