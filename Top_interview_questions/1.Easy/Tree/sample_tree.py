pattern = "man"
string = "dhimanmanman"

print(pattern[0:len(pattern)])

count = 0
for i in range(len(string)-len(pattern)+1):
    if string[i] == pattern[0]:
        if string[i:i+len(pattern)] == pattern:
            count += 1
print(count)