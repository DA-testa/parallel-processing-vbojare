# python3

def parallel_processing(n, m, data):
    output = []
    x = [o] * n 
    t = 0
    i = 0
    j = 0

    while j < len(data):
        for i in range (len(x)):
            if x[i] == 0:
                x[i] = data[j] - 1
                output.append([i, x])
                if j < lan(data):
                    j += 1
                else:
                    x[i] -= 1
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
        nama = input()

        if "a" not in nama:
            with open(nama, mode = 'r', encoding = "utf8") as fail:
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
