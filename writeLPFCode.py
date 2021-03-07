# coding: UTF-8

def writeHeader(func_name, return_type):
  return return_type + " " + func_name + "(ImageBin raw_in, const int x, const int y)"

def writeIdx(idx, idy):
  if (idx >= 0): idx_str = "+" + str(idx)
  else         : idx_str = str(idx)
  if (idy >= 0): idy_str = "+" + str(idy)
  else         : idy_str = str(idy)

  return 'raw_in.getPix(x' + idx_str + ', y' + idy_str + ')'

def writeCodeOnce(fp, func_name, return_type, coeff_dict):
  flg = 0

  # header
  fp.write(writeHeader(func_name, return_type) + " {\n")

  # body
  cnt = 0
  fp.write("  " + return_type + " pix = (int)( (\n")
  for key in coeff_dict:
    idx = coeff_dict[key]

    for i in range(len(idx)):
      if (flg == 0): fp.write("    ")
      else:          fp.write("  + ")
      fp.write(writeIdx(idx[i][0], idx[i][1]) + " * " + str(key) + '\n')

      cnt += key
      flg += 1
  fp.write("  ) / (float)(" + str(cnt) + ") + 0.5);\n")

  # footer
  fp.write("  return pix;\n")
  fp.write("}\n\n")

def writeCodeProto(fp, func_name, return_type):
  fp.write(writeHeader(func_name, return_type) + ";\n")

def writeArrayFuncPointer(fp):
  fp.write("typedef int (*afpFunc)(ImageBin, const int, const int);\n\n")

def writeIncludeHeader(fp, header_filename):
  fp.write('#include "' + header_filename + '"\n\n')

def writeLPFCode(filename, return_type, all_filter):
  with open(filename + ".cpp", "w") as fp_cpp, \
       open(filename + ".h", "w") as fp_header:

    writeArrayFuncPointer(fp_header)
    writeIncludeHeader(fp_cpp, filename + ".h")

    for key in all_filter:
      func_name = key
      coeff_dict = all_filter[key]

      writeCodeProto(fp_header, func_name, return_type) # プロトタイプ宣言
      writeCodeOnce(fp_cpp, func_name, return_type, coeff_dict) # 関数