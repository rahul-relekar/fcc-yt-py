"""
    Basic methods of concatenating string in a string

"""
# Choose first, second, third, fourth, fifth or final
print("Let us play Madlibs")
year = input("Your current year of study (ex. Final): ")
degree = input("Your complete current degree (ex. BEng): ")
university = input("Your University Name (ex. CityUHK) : ")
major = input ("Your major (ex. CDE / Computer and Data Engineering) : ")
intern = input("Your Internship period in months (ex. 8) : ")
hobby = input("Your favourite hobby (ex. Binge watch shows) : ")

# print("I am " + year + " year student")
# print("I am {} year student".format(year))
print("\n<----------- Basic Introduction about yourself ----------->")
print(f"I am a {year}-year student pursuing {degree} at {university} specializing in {major}.\nI have had {intern} months of technical experience in my field so far.\nMy favourite hobby being {hobby}.\n")