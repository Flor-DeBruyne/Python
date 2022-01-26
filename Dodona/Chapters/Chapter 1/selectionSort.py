def selection_sort_vooraan(a):
    for i in range(0, len(a)-1):
        positie = i
        min = a[i]
        for j in range(i+1, len(a)):
            if a[j] < min:
                min = a[j]
                positie = j
        a[positie] = a[i]
        a[i] = min
        print(a)


a = [int(_) for _ in input().split()]
selection_sort_vooraan(a)