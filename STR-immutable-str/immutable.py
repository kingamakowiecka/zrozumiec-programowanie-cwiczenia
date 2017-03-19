baseString = "test"

print("baseString:", baseString, id(baseString))
print("baseString + test2: testtest2", id(baseString + "test2"))
baseString = baseString + "test2"
print("baseString = baseString + \"test2\":",  baseString, id(baseString))
print("baseString.upper(): TESTTEST2", id(baseString.upper()))
baseString = baseString.upper()
print ("baseString = baseString.upper():", baseString, id(baseString))
baseString = "test3"
print("baseString = test3:", baseString, id(baseString))
print("baseString.replace(\"3\", \"6\"): test6", id(baseString.replace("3", "6")))
baseString = baseString.replace("3", "6")
print("baseString = baseString.replace(\"3\", \"6\"):", baseString, id(baseString))
