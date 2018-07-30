import solutions as s

if __name__ == "__main__":
    print("Available modules: ")
    for m in s.modules:
        mx = s.modules[m]
        print("", mx[0][-3::], mx[1])

    y = ""
    while 1:
        x = int(input("Please type a number to start the corrsponding Euler script:\n"))
        module = "euler" + ("000" + str(x))[-3::]

        if module not in s.modules:
            print("Unknown module, please try again...")
            continue
        break

    m = s.modules[module]
    print("Running '{}'.\nGathering inputs ...\n".format(m[1]))
    inputs = m[2].split('\t')
    inst = []
    for i in inputs:
       tmp = i.split(';')
       q = input(tmp[1] + '\n')
       if tmp[2] == 'int':
           q = int(q)
       else:
           pass

       inst.append(q)

    ret = eval("s.{}.run(*inst)".format(module))
    print(ret)
