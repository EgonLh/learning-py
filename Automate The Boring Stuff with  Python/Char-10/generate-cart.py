# python file manipulation practice

from card_operation import checkFile,writeMsg;

file_name = input(">Enter Your FileName :");
mode = checkFile(fileName=file_name);
writeMsg(mode,file_name);
