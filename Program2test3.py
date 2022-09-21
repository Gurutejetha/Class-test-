test_str=input("enter any string")
all_freq={}
for i in test_str:
     if(i in all_freq):
         all_freq[i]+=1
     else:
         all_freq[i]=1
         print("The count of all chacters in string is",str(all_freq))
