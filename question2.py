# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 20:42:15 2020

@author: Mohammadali
"""
import numpy as np
import pandas as pd

MT = pd.read_csv('MT_cleaned.csv')
VT = pd.read_csv('VT_cleaned.csv')

def chi2_distance(A, B):
    chi = 0.5 * np.sum([((a - b) ** 2) / (a + b)  
                      for (a, b) in zip(A, B)]) 
    return chi
    

#q2-part1
total_gender_num = MT['driver_gender'].size
male_gender_num = MT['driver_gender'][MT['driver_gender']=='M'].size

proportion = male_gender_num/total_gender_num

print('answer of part 1: {}'.format(proportion))

#################################################

#q2-part2
out_of_state_arrested = MT['is_arrested'][MT['is_arrested']==True][MT['out_of_state']==True].size
out_of_state_not_arrested = MT['is_arrested'][MT['is_arrested']==False][MT['out_of_state']==True].size
in_state_arrested = MT['is_arrested'][MT['is_arrested']==True][MT['out_of_state']==False].size
in_state_not_arrested = MT['is_arrested'][MT['is_arrested']==False][MT['out_of_state']==False].size

a = [out_of_state_arrested, out_of_state_not_arrested]
b = [in_state_arrested, in_state_not_arrested]

print('answer of part 2: {}'.format(chi2_distance(a, b)))

################################################

#q2-part3
speeding_num = MT['violation'][MT['violation']=='Speeding'].size
total_num = MT['violation'].size

proportion = speeding_num/total_num

print('answer of part 3: {}'.format(proportion))

################################################

#q2-part4
#MT_DUI = MT['violation'][MT['violation'].dropna().contains('DUI')]
#VT_DUI = VT['violtion'][VT['violation'].str.contains('DUI')].dropna().size
#
#print('answer of part 4: {}'.format(MT_DUI/VT_DUI))

################################################

#q2-part5
year_num = MT['vehicle_year'][MT['id'].str.contains('2016')].size
w = MT['vehicle_year'][MT['id'].str.contains('2016')].dropna()
w = w[w!='UNK']
year_sum = w.astype(int).sum()

year_mean = year_sum/year_num

print('answer of part 5: {}'.format(year_mean))




