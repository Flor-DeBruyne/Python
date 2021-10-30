appel = int(input())
crate = int(appel // 20) 
pallet = int(crate //35)
rest = int(appel % 20)

print(f"{pallet}\n{crate % 35}\n{rest}")