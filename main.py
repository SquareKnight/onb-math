import solutions as s
import time

if __name__ == "__main__":
    print("Available modules: ")
    for m in s.modules:
        mx = s.modules[m]
        print("", mx[0][-3::], mx[1])

    y = ""
    while 1:
        x = int(input("Please type a number to start the corresponding Euler script:\n"))
        module = "euler" + ("000" + str(x))[-3::]

        if module not in s.modules:
            print("Unknown module, please try again...")
            continue
        break

    m = s.modules[module]
    print("Running '{}'.\nGathering inputs ...\n".format(m[1]))
    inputs = m[2].split('`')
    inst = []
    print("Inputs: ", inputs)
    for i in inputs:
       tmp = i.split(';')
       default = None if len(tmp) < 4 else tmp[3]
       q = input(tmp[1] + '{}\n'.format(' (default value: ' + default + ')' if default is not None else ''))
       if q == '' and default is not None:
           q = default

       if tmp[2] == 'int':
           q = int(q)
       else:
           pass

       inst.append(q)

    t = time.time()
    print("Now running program.")
    ret = eval("s.{}.run(*inst)".format(module))
    print()
    print(ret)
    print()
    print("It took {} seconds".format(time.time() - t))
