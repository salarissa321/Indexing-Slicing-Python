
#------------------------------------------------------
#----------Strings Indexing & Slicing---------
# [1] All Data in Python is Obejct
# [2] Object contain Elements
# [3] every Elements has it Own Index
# [4] python use Zero Based Indexing (Index Start form Zero)
# [5] Use Square Brackets To Access Element
# [6] Enable Accsessing Parts Of Strings, Tuple or Lists 
#--------------------------------------------------------


# Indexing(Accsess Single Item)

myString = "I Love Python"
print(myString[0]) # Index 0 => I
print(myString[9]) # Index 9 => t

print(myString[-1]) # index -1 => n # First Character from End
print(myString[-6]) # index -6 => p # First Character from End


# Slicing (Accsess multiple Sequence Items)
# [Start:End] End not Included
# [Start:End:Steps]

print(myString[8:11]) # yth
print(myString[3:5]) # ov
print(myString[:10]) #  I Love Pyt # If Start is Not Here will Star form 0 
print(myString[5:]) # e Python  # If End  is Not Here will got to the End 
print(myString[:]) # I Love Python # Full Data  

# Steps

print(myString[0::1]) # I Love Python # Full Data
print(myString[::1]) # I Love Python # Full Data
print(myString[0::2]) # ILv yhn
print(myString[0::3]) # Io tn










