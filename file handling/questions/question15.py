# Remove single-line comments

f = open("program.py", "r")
out = open("without_comments.py", "w")

for line in f:
    if not line.strip().startswith("#"):
        out.write(line)

f.close()
out.close()

print("Comments removed successfully.")