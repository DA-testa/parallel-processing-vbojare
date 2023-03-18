# python3

def parallel_processing(n, m, data):
    output = []
    x = [0] *  n 

    for i in range(m):
        y = min(x)
        th = x.index(y)
        st = x[th]
        x[th] = x[th] + data[i]
        output.append((th, st))
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    count = list(map(int, input().split()))
    n = count[0]
    m = count[1]

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))
   

    
    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i, j in result :
        print(i,j)


if __name__ == "__main__":
    main()
