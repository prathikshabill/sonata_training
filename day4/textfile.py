try:
    file = open('prat.txt', 'r')
    print(file.read())
    file.close()
except(FileNotFoundError):
    print("NO SUCH FILE")


