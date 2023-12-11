#!/usr/bin/env python3

# example data
# BTIME=[ 7, 15, 30 ]
# BDIST=[ 9, 40, 200 ]

# input data
BTIME=[ 49, 97, 94, 94 ]
BDIST=[ 263, 1532, 1378, 1851]
def main():
    winning_product=1
    for pos, btime in enumerate(BTIME):
        bdist=BDIST[pos]
        print(f"Time: {btime}")
        winning_count=0
        for speed in range(1, btime):
            if speed*(btime-speed)>bdist:
                winning_count+=1
        winning_product*=winning_count
    print(f"{winning_product}")

if __name__ == "__main__":
    main()
