stuks = int(input())
kostprijs = float(input())
barcodes = int(input())
mijlen = int(input())
totaal = int(stuks/barcodes) 

print("Phillips spendeerde ${} voor {} frequent flyer mijlen.".format(stuks*kostprijs,int((totaal)*mijlen)))