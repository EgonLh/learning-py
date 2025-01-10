try:
    print(5/0)
except ZeroDivisionError:## don't know don't add any keys
    print("This is Error")

while True:
    f_num = input("Enter Your First Number :");
    s_num = input("Enter Your Second Number: ");
    if (f_num == 'q') or (s_num == 'q'):
        print("Quit ....")
        break;
    try:
        answer = int(f_num)/int(s_num);
    except ZeroDivisionError:
        print("This is Error Here : can't divied by 0 ")
    else:
       print(answer)

