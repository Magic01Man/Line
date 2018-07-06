import argparse
import os
import sys

os.system('clear')
print """

                                          ////////////
                                             /////
                ////                        /////        /////////        ////                ///////////////////  
                ////                       /////         /////////        ////               ///////////////////
                ////                      /////          ////  ////       ////              //////   
                ////                     /////           ////   ////      ////             //////             
                ////                    /////            ////    ////     ////            //////////////////////              
                ////                   /////             ////     ////    ////           //////////////////////               
                ////                  /////              ////      ////   ////          //////                 
                ////              ////////////           ////       ////  ////         //////                      
                ////                                     ////        //// ////        ///////////////////////     
                ///////////////////                      ////          ///////       ///////////////////////


                                                Author ------> Magic Man
                                                Author's Email -----> magicmangit@gmail.com
                                                     
        """


parser = argparse.ArgumentParser(description='Process some integers.') 
parser.add_argument('-L' , action = "store" , dest= 'location', required = True , help = "for you'r location's file ") 
parser.add_argument('-B' , action = "store" , dest = 'Big' , type = int , required = False, help = "for biger than you'r number   > ")
parser.add_argument('-S' , action = "store" , dest = 'Short' , type = int,required = False, help =  "for short than you'r number  <" )
parser.add_argument('-E' , action = "store" , dest = 'Equal' , type = int , required = False, help = "for equal you'r number  =")

give_args = parser.parse_args() 
location = give_args.location
Big = give_args.Big
Short = give_args.Short
Equal = give_args.Equal 

try:
    fo = open(location , 'r+') 
    text = fo.read()
except IOError:
    print("location's file not find")
    sys.exit()

step = -1
new_text = []

for i in text:
    count = len(text)
    count = count-1
    step+=1
    if step>count:
        break

    words = text[step]
    if i == '\n':
        words = text[0:step]
        new_text.append(words)
        words = text[0:step+1]
        text=text.replace(words , '')
        step=-1

print(new_text)

make = os.system('rm 313')
make = os.system('touch 313')

if Equal:
    for text_2 in new_text:
        if len(text_2) == Equal:
            file_1 = open('313' , 'a')
            print(text_2)
            text_new = text_2 + '\n'
            file_1.write(text_new)
        

if Big:
    for text in new_text:
        if len(text) > Big:
            file_1 = open('313' , 'a')
            print(text)
            text_new = text + '\n'
            file_1.write(text_new)

if Short: 
    for text_1 in new_text:
        if len(text_1) < Short:
            file_1 = open('313' , 'a')
            print(text_1)
            text_new = text_1 + '\n'
            file_1.write(text_new)