# coding: UTF-8

import sys
import itertools

# local
from readExcel import GetGradFilter
from writeGradCode import writeGradCode
from writeLPFCode import writeLPFCode

if __name__ == "__main__":
  # set Excel Path
  filepath = sys.argv[1]
  mode = sys.argv[2]

  # get Filter
  filename, all_filter = GetGradFilter(filepath)

  # write Code
  return_type = "int"
  if (mode == 0): writeGradCode(filename, return_type, all_filter)
  else          : writeLPFCode(filename, return_type, all_filter)