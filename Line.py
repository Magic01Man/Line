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
parser.add_argument('-O' , action = "store" , dest= 'output', required = True , help = "for you'r location's output ") 

give_args = parser.parse_args() 
location = give_args.location
Big = give_args.Big
Short = give_args.Short
Equal = give_args.Equal
out = give_args.output


try:
    with open(location) as file:
        line = file.read().splitlines()
except IOError:
    print("Please enter you'r location's file")
    sys.exit()

def equal(filename):
    number = 0
    for show in line:
        if len(show) == Equal:
            number+=1
            try:
                f = open(filename , 'a')
            except IOError:
                print("you should enter name's you'r text file in location's output")
                sys.exit()
            print('{} : {}' . format(number , show))
            f.write(show + '\n')

def big(filename):
    number = 0
    for show in line:
        if len(show) > Big:
            number+=1
            try:
                f = open(filename , 'a')
            except IOError:
                print("you should enter name's you'r text file in location's output")
                sys.exit()
            print('{} : {}' . format(number , show))
            f.write(show + '\n')
            
def short(filename):
    number = 0
    for show in line:
        if len(show) < Short:
            number+=1
            try:
                f = open(filename , 'a')
            except IOError:
                print("you should enter name's you'r text file in location's output")
                sys.exit()
            print('{} : {}' . format(number , show))
            sys.exit()
            f.write(show + '\n')


if Equal:
    equal(out)


if Big:
    big(out)

if Short:
    short(out)
