""" solution for Human Readable Time challenge
convert second to human readable time"""

def make_readable(seconds):
    HH = 0
    MM = 0
    SS = 0
    SS = seconds % 60
    minutes = seconds // 60
    if minutes != 0:
        MM = minutes % 60
        hours = minutes // 60
        if hours % 60 != 0:
            HH = hours
    return str(HH).zfill(2) + ':' + str(MM).zfill(2) + ':' + str(SS).zfill(2)

# test
def main():
    print(make_readable(86399))
if __name__ == "__main__":
    main()
