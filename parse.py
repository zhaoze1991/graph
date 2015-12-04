import sys
f = open('a.data','r').readlines();
f1 = open('data2.tsv','w');
for line in f:
    element = line.split(' ')
    result = ''
    for ele in element:
        if ele == '':
            continue
        result += (ele + '\t')
    result = result[:-1]
    # print result
    f1.write(result)

