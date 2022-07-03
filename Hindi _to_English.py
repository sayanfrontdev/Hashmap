myDict={
    "Pankha": "Fan",
    "Aankh": "Eye",
    "Subha": "Evening",
}
print("Options are", myDict.keys())
a=input("Enter the hindi word\n")

#Below line will not throw an error if the key is not present in the dictionary.
print("The meaning of your word is:" , myDict.get(a))