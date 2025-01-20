# print("For File Not Found Handling")
# fname = input("Enter filename :");
# print(fname)
# try:
#     with open(fname) as file_buildin_obj:
#         lines = file_buildin_obj.read()
# except FileNotFoundError:
#     print("The file",fname,"was not found.")
# else:
#     words = lines.split();
#     print(words)
#     count = len(words)
#     print("Count :",count)


# Refactor
def countWords(fname):
    """To Count Words """
    try:
        with open(fname) as file_obj:
            context = file_obj.read()
    except FileNotFoundError:
        # print("The file <",fname,"> was not found.")
        pass
    else:
        wordsCount = len(context.split());
        print("Total Count of file: <"+fname+"> is :",wordsCount);

filenames = ['Card_1','Hello','nth','info.txt'];

for fname in filenames:
    countWords(fname=fname)