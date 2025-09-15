#dictionsry=a collectiopn of {key : value} pairs
 #order and changable no duplicate
capitals={"usa":"moimoi","china":"singapoor",
          "japan":"korea","pakistan":"karachi"}
#print(capitals)

#(for colomn in capitals:
      #print(colomn)

      #print(capitals.get("japan")) if capitals.get("india") else print("not exist"))
#print(capitals.get("india"))
#for x in capitals:
    #print(capitals.get(x))#<-----x will be key here
capitals.update({"india":"karnataka"})
#capitals.update({"japan":"tailand"})
#print(capitals)
#for x in capitals:
  #    print(f"{x} {capitals.get(x)}")
#print()
#capitals.pop("pakistan")
#capitals.popitem()
#capitals.clear()
#print(capitals)
#keys=capitals.keys()<-----to get key of the given item
#for key in capitals.keys():
#    print(key)
#value=capitals.values()<-------to get the value of the given item
#for values in value:
#    print(values)
for key,value in capitals.items():#<-----to get the both item and value
    print({key},{value})
#print(dir(capitals))
#print(help(capitals))