# racecar
#Random racecar speed calculations
laptimes = [360, 358, 362, 370, 350, 355, 359, 365, 360, 358]

def paceperlap(seconds, laps):
    pace = seconds / laps
    conmin = int(pace / 60)
    consec = int(pace % 60)

    # Formatting to MM:SS
    if conmin < 10:
        conmin = "0" + str(conmin)
    else:
        conmin = str(conmin)

    if consec < 10:
        consec = "0" + str(consec)
    else:
        consec = str(consec)

    print("Pace per lap: " + conmin + ":" + consec)

paceperlap(3600, 10)
paceperlap(7214, 10)


def timeoflaps(laptimes):
    deviationtimes = []

    fastest = laptimes[0]
    slowest = laptimes[0]
    lap = 1
    average = sum(laptimes) / len(laptimes)

    print("\nAverage lap time: " + str(round(average, 2)) + " seconds")

    for time in laptimes:
        print("Lap " + str(lap) + ": " + str(time) + " seconds")

        if time < average:
            print("  Faster than average")
        elif time > average:
            print("  Slower than average")
        else:
            print("  Equal to average")

        if time < fastest:
            fastest = time
        if time > slowest:
            slowest = time

        deviationtimes.append(abs(time - average))
        lap += 1

    averagedeviation = sum(deviationtimes) / len(deviationtimes)

    print("\nAverage deviation: " + str(round(averagedeviation, 2)) + " seconds")
    print("Fastest lap: " + str(fastest) + " seconds")
    print("Slowest lap: " + str(slowest) + " seconds")

timeoflaps(laptimes)

