import time

try:
    f = open("poem.txt")
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        time.sleep(2)
        print(line, end='')
        time.sleep(2)
except KeyboardInterrupt:
    print("You cancelled the reading.")
finally:
    f.close()
    print("File is closed.")
