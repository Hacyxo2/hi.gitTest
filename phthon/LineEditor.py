# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 10:29:32 2021

@author: sh010
"""
class ArrayList:
    def __init__(self):
        self.items = []

    def insert(self, pos, elem):
        self.items.insert(pos, elem)

    def delete(self, pos):
        return self.items.pop(pos)

    def replace(self, pos, elem):
        self.items[pos] = elem
    
    def getEntry(self, pos):
        return self.items[pos]

    def size(self):
        return len(self.items)

    def find(self, item):
        return self.items.index(item)

def myLineEditor():
    list = ArrayList()
    while True:
        command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, f-찾기, q-종료 => ")
        
        if command =='i':
            pos = int(input(" 입력행 번호 :"))
            str = input("입력행 내용:")
            list.insert(pos,str)
            
        elif command =='d':
            pos = int(input(" 삭제행 번호 :"))
            list.delete(pos)
        
        elif command =='r':
            pos = int(input(" 변경행 번호 :"))
            str = input("변경행 내용:")
            list.replace(pos,str)
             
        elif command =='p':
            print('Line Editor')
            for line in range(list.size()):
                print('[%2d] '%line, end='')
                print(list.getEntry(line))
            print()
        
        elif command == 'l':
            filename = input('읽어올 파일: ')
            infile = open(filename, "r", encoding='UTF-8') 
            lines = infile.readlines()
            for line in lines:
                list.insert(list.size(), line.rstrip('\n'))
            infile.close()
        
        elif command == 's':
            filename = input('어느 파일에 저장하십니까? ')
            outfile = open(filename, "w")
            for i in range(list.size()):
                outfile.write(list.getEntry(i)+'\n')
            outfile.close()
        
        elif command =='f':
            word = input('찾을 문자나 문자열: ')
            for line in range(list.size()):
                if list.getEntry(line).find(word) > -1:
                    print('[%2d] '%line, end='')
                    print(list.getEntry(line))
                
        elif command =='q': return        

myLineEditor()
        
