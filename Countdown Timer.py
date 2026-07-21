import time

seconds = int(input("Seconds: "))

while seconds:
    mins = seconds // 60
    secs = seconds % 60

    print(f"{mins:02d}:{secs:02d}", end="\r")

    time.sleep(1)
    seconds -= 1

print("Time's Up!")