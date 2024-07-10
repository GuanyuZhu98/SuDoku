#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 21:25:38 2022

@author: DanielZhu
"""

import numpy as np
import random

class SuDoku:
    def __init__(self):
        self.refer = [1.,2.,3.,4.,5.,6.,7.,8.,9.]
        
    
    def BDgenerator(self):
        
        ##=== Initialize All parameters===##
        refer = self.refer
        bd = np.zeros((9,9))
        choices = []
        for i in range(9*9):
            choices.append(refer.copy())
        Total_steps = len(choices)
        bd = bd.reshape(-1)
        steps = 0
        
        
        while steps!=Total_steps:
            ## A back tracking method
            ## Trémaux's algorithm. 
            
            while choices[steps] == []:
                
                ##No choice for current step, reset current choice&num then go back to former step.
                bd[steps] = 0.0
                choices[steps] = refer.copy()
                steps -=1
                

            elem = random.choice(choices[steps])
            choices[steps].remove(elem)
            bd[steps] = elem
            tbd = bd.reshape(9,9)
            
            ## Test validation. If valid, go to the next step.
            ## Otherwise, try another number in remained choices.
            if self.Valid(tbd):
                steps+=1
            else:
                pass
        
        ## After finishing all steps, return the board.
        return(tbd)
    
        
    def Valid(self,bd):
        ## Test validation of board
        ## Column Validation(Transpose of Row); Row Validation; Box Validation
        '''Series Circuit'''
        if self.RowValid(bd.T) and self.RowValid(bd) and self.BoxValid(bd):
            return(True)
        else:
            return(False)
        
    def RowValid(self,rbd):   
        dum = True
        for row in rbd:
            l_row = list(row)
            for i in range(9):
                if l_row.count(float(i+1))>1:
                    dum  = False
            ##test whether there's a repeated number
        return(dum)
        
    def BoxValid(self,bbd):
        bbd = bbd.reshape(-1)
        nbd = np.zeros((1,81))
        count = 0
        nbd = nbd[0]
        
        ##Slower and Might return wrong value#
   
        '''
        for i in range(3):
            i*=27
            for j in range(3):
                j*=3
                nbd[count:count+2] = bbd[i+j:i+j+2]
                nbd[count+3:count+5] = bbd[i+j+9:i+j+11]
                nbd[count+6:count+8] = bbd[i+j+18:i+j+20]
                count+=9
        '''
        for i in range(3):
            i*=27
            for j in range(3):
                j*=3
                nbd[count] = bbd[i+j];nbd[count+1] = bbd[i+j+1];nbd[count+2] = bbd[i+j+2];
                nbd[count+3] = bbd[i+j+9];nbd[count+4] = bbd[i+j+10];nbd[count+5] = bbd[i+j+11];
                nbd[count+6] = bbd[i+j+18];nbd[count+7] = bbd[i+j+19];nbd[count+8] = bbd[i+j+20];
                count+=9

        nbd = nbd.reshape(9,9)

        return(self.RowValid(nbd))
    
    
    def Gime_A_Game(self,level):
        bd = self.BDgenerator()
        row = [0,1,2,3,4,5,6,7,8]
        column = row.copy()
        Total_delet_num = level## this can be changed later
        delet_num = 0
        bd0 = bd.copy()
        

        
        while delet_num!=Total_delet_num:
            
            r = random.choice(row)
            c = random.choice(column)
           
                
                
            if bd0[r,c] != 0.:
                
                bd0[r,c] = 0
                
                if self.Solve(bd0,'valid'):
                    delet_num+=1
                else:
                    bd0[r,c] = bd[r,c]

        return(bd0)
'''
    def Solve(self,bd,mthod):
        bd1 = bd.copy()
        row = 0
        col = 0
        refer = self.refer
        blank = []
        
        for i in bd1:
            for j in i:
                if j == 0.:
                    blank.append([row,col,refer.copy()])
                
                col+=1
            row+=1;col-=9
        
        # Primary elimination
        dum = 0
        for i in blank:
            valid_choices = []
            for j in range(9):
                bd1[int(blank[dum][0])][int(blank[dum][1])] = blank[dum][2][j]
                if self.Valid(bd1):
                    valid_choices.append(blank[dum][2][j])
                bd1[int(blank[dum][0])][int(blank[dum][1])] = 0.
            blank[dum][2] = valid_choices
            dum+=1
         
        # All possibility
        poss = 1
        count = 0
        not_1_layers = []
        for i in range(len(blank)):
            poss*=len(blank[i][2])
            if len(blank[i][2]) != 1:
                not_1_layers.append(count)
            count+=1
            
        ## Back tracking method
        step = 0
        ans = 0
        dumblank = blank.copy()
        
        switch = True
        if not_1_layers == []:
            return(True)
        
 
        while switch:
            print(not_1_layers)
            if blank[not_1_layers[step]][2]==[]:
                blank[not_1_layers[step]]=dumblank[not_1_layers[step]].copy()
                bd1[int(blank[not_1_layers[step]][0])][int(blank[not_1_layers[step]][1])] = 0.
                step-=1
            
            print(step,blank[not_1_layers[step]][2])
            elem = random.choice(blank[not_1_layers[step]][2])
            blank[not_1_layers[step]][2].remove(elem)
            bd1[int(blank[not_1_layers[step]][0])][int(blank[not_1_layers[step]][1])] = elem

            if self.Valid(bd1):
                if step == len(not_1_layers)-1:
                    ans+=1 ; step-=1
                else:
                    step+=1
            else:
                pass
            
            if mthod == 'valid' and ans>1:
                return(False)
            
            retard = 0
            for i in range(len(not_1_layers)):
                if blank[not_1_layers[i]][2] == []:
                    retard+=1
                if retard == len(not_1_layers):
                    switch = False
        if ans == 1:
            return(True)
                    
            
            

    
        
        print('\n')
        return(True)

            


'''
            
            
            
                

                
a = SuDoku()

print(a.BDgenerator())
#print(a.Gime_A_Game(30))





