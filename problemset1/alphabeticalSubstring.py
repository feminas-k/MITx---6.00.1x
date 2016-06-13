result = s[0]
final = s[0]
for i in range(1,len(s)):
        if s[i] >= s[i-1]:
                result += s[i]
                if len(result) > len(final):
                        final = result
        else:
                result = s[i]
print "Longest substring in alphabetical order is: " + str(final)
