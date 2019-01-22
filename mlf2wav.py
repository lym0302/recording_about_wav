# coding = utf-8

import os
import re
import sys


if __name__ == "__main__":

  inwav_dir = sys.argv[1]
  outwav_dir = sys.argv[2]
  mlf_filename = sys.argv[3]
  raw_number = 0
  phone_number = 0
  for line in open(mlf_filename,encoding='utf-8').readlines():
    if 'lab' in line:
      filename = line.split('*/')[1].split('.')[0] 
      input_filename = inwav_dir + filename + '.wav'
      print(input_filename)
      raw_number += 1
    elif ('MLF'  not  in line) and (not line.startswith('.')):
      phone_number += 1
      start = float(line.split(' ')[0])/10000000.0
      end = float(line.split(' ')[1])/10000000.0
      length = end - start
      phoneme = line.split(' ')[2]
      number = line.split(' ')[3]
      output_filename = outwav_dir + filename + '_' + 'detail'+ '_' + str(start) + '_' + str(end) + '_' + phoneme + '.wav'
      os.system('sox %s %s trim  %f %f'%(input_filename, output_filename, start, length))
      os.system("cp %s %s " %(input_filename, outwav_dir))
  print("the total number of raw wav in this mlf is : %d \n" %(raw_number) )
  print("the total number of phone wav in this mlf is : %d \n" %(phone_number) )
