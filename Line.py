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

os.system('rm 313')


with open(location) as file:
    line = file.read().splitlines()

def equal():
    number = 0
    for show in line:
        if len(show) == Equal:
            number+=1
            print('{} : {}' . format(number , show))
            f = open('313' , 'a')
            f.write(show + '\n')

def big():
    number = 0
    for show in line:
        if len(show) > Big:
            number+=1
            print('{} : {}' . format(number , show))
            f = open('313' , 'a')
            f.write(show + '\n')
            
def short():
    number = 0
    for show in line:
        if len(show) < Short:
            number+=1
            print('{} : {}' . format(number , show))
            f = open('313' , 'a')
            f.write(show + '\n')

if Equal:
    equal()

if Big:
    big()

if Short:
    short()
