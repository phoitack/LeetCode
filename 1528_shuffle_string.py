def restoreString(s, indices):
    
    new_string = list(s)
    count = 0

    for idx in indices:

        new_string[idx] = s[count]
        count += 1
        
    return (''.join(new_string))
    
ss = 'codeleet'
indices = [4, 5, 6, 7, 0, 2, 1, 3]

#ss = "aaiougrt"
#indices = [4, 0, 2, 6, 7, 3, 1, 5]


print(restoreString(ss, indices))

# Another solution from the discussion is really beautifil
# Apparently, it is O(nlog(n)) in time

return(''.join(x[0] for x in sorted(zip(s,indices), key=(lambda x: x[1]))))