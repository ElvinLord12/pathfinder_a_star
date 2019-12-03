infile = "data.txt"
outfile = "cleaned_data.txt"

delete_list = ["0:00:0"]
fin = open(infile)
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()