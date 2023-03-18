# python3

def parallel_processing(n, m, data):
    output = []
    th = [0] * n 
    t = 0
    i = 0
    j = 0

    while j < len(data):
        for i in range (len(th)):
            if th[i] == 0:
                th[i] = data[j] - 1
                output.append([i, t])
                if j < lan(data):
                    j += 1
                else:
                    th[i] -= 1
        t += 1
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    i = "i"
    if "i" in i.lower():
        n, m = map(int, input().split())
        data = list(map(int, input().split()))

    else "f" in i.lower() :
        name = input()

        if "a" not in name:
            with open(name, mode = 'r', encoding = "utf8") as fail:
                n, m = map(int, fail.readline().split())
                data = list(map(int, fail.readline().split()))
        else :
            return
    
    else:
        return

    
    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i, j in result :
        print(i,j)


if __name__ == "__main__":
    main()
