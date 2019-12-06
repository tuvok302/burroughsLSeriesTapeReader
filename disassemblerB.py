#ssg = self study guide instructions not in series manual
import sys
import binascii

machineOp = {
  "88" : "ADA",
  "A-" : "ADB", #ssg
  "54" : "ADIR",
  "8F" : "ADK",
  "80" : "ADM",
  "ED" : "AL",
  "09" : "ALARM",
  "EF" : "ALR",
  "E9" : "ALTO",
  "E5" : "ALTP",
  "EE" : "AR",
  "EA" : "ARTO",
  "70" : "BRU", #7- in ssg
  "EC" : "CC",
  "B2" : "CDC",
  "B3" : "CDV",
  "66" : "CHG",
  "8E" : "CLA",
  "D8" : "CLM",
  "DA" : "CPA",
  "5C" : "DIR",
  "9A" : "DIV",
  "E1" : "DUP",
  "A9" : "EAM",
  "A7" : "EL",
  "4-" : "EX",
  "4-" : "EXE",
  "6-" : "EXL",
  "4-" : "EXZ",
  "58" : "IIR",
  "9E" : "INK",
  "1A" : "IRCP",
  "A7" : "LA", #ssg
  "34" : "LBN", #ssg
  "50" : "LIR",
  "CD" : "LCD",
  "DC" : "LCFR",
  "34A8" : "LGN", #ssg
  "F0" : "LKBR",
  "E0" : "LLCR",
  "E4" : "LLLR",
  "64" : "LOD",
  "34AD" : "LPF",
  "FC" : "LPKR",
  "F8" : "LPNR",
  "324A" : "LPR",
  "34B1" : "LRA",
  "18" : "LRBR",
  "E2" : "LRCR",
  "E6" : "LRLR",
  "34B2" : "LSA",
  "B700" : "LSCR", #ssg
  "B4" : "LSER", #ssg
  "B740" : "LSLR", #ssg
  "34A7" : "LSN",
  "642" : "LSR",
  "34AA" : "LTF", #ssg
  "34A6" : "LTN",
  "CD" : "LXC",
  "6000" : "MOD",
  "8A" : "MUL",
  "8C" : "MULR",
  "A6" : "NK",
  "A2" : "NKCM",
  "A4" : "NKR",
  "A0" : "NKRCM",
  "0800" : "NOP",
  "E8" : "OC",
  "0910" : "OFF",
  "C8" : "PA",
  "18" : "PA2", #ssg doubel entry?
  "1D" : "PAB",
  "BC00" : "PBA", #ssg has code BC00
  "A500" : "PAS", #ssg
  "C0--" : "PC",
  "C4--" : "PC+",
  "C5--" : "PC-",
  "C1--" : "PCP",
  "F6" : "PKA",
  "F7" : "PKB",
  "F5" : "PKC",
  "D4" : "PN",
  "D0" : "PNS+",
  "D1" : "PNS-",
  "0110" : "POF", #ssg
  "0120" : "PON",
  "EB" : "POS",
  "CC00" : "RCD",
  "3CA9" : "RBN", #ssg
  "CC00" : "RCD",
  "1C" : "RCP",
  "B9" : "REAM",
  "0100" : "REL",
  "3A41" : "REM",
  "3B41" : "REM2", #ssg ref 13
  "B0" : "RNK",
  "3CAD" : "RPF",
  "3A8A" : "RPR",
  "0700" : "RP",
  "3CB1" : "RRA",
  "3CB2" : "RSA",
  "3CA7" : "RSN",
  "65" : "RST",
  "3CA0" : "RTH",
  "BC" : "RTK",
  "BD" : "RTKM",
  "3CA6" : "RTN",
  "BB" : "RXEAM",
  "BE" : "RXTK",
  "BF" : "RXTKM",
  "14" : "SCP",
  "67-" : "SET",
  "4-*" : "SK",
  "4-" : "SKE",
  "6-" : "SKL",
  "4-!" : "SKZ",
  "E3" : "SKP",
  "02" : "SLRO",
  "03" : "SLROS",
  "20" : "SRJ",
  "04" : "SRR",
  "0000" : "STOP",
  "98" : "SUA",
  "9F" : "SUK",
  "90" : "SUM",
  "9C0" : "TAIR",
  "AC" : "TK",
  "AD" : "TKM",
  "38" : "TRA",
  "150" : "TRAB",
  "1E0" : "TRB",
  "1B0" : "TRBA",
  "B80" : "TRCA",
  "16" : "TRCB",
  "B90" : "TRCM",
  "17" : "TRF",
  "30" : "TRM",
  "1F0" : "TSB",
  "C6" : "XA",
  "0C" : "XB",
  "BA" : "XBA",
  "C2" : "XC",
  "AB" : "XEAM",
  "0A00" : "XMOD",
  "D7" : "XN",
  "CA" : "XPA",
  "BE" : "XPBA",
  "D6" : "XPN",
  "D2" : "XPNS+",
  "D3" : "XPNS-",
  "AE" : "XTK",
  "AF" : "XTKM"
}

f1 = open(str(sys.argv[1]), "r")
f2 = open("string" + str(sys.argv[1]), "w", encoding="utf-8")
f3 = open("_test" + str(sys.argv[1]), "w", encoding="utf-8")

fl = f1.readlines()
program = []
word = [None] * 8
count = 0
wordNum = 0

for x in fl:
  #print(count, x)
  #count = 0
  #word = [None] * 9
  if x == ("10100001\n") and count == 0:
    #word.append("Start Message Block 1")
    count += 1
  elif x == ("10100000\n") and count == 0:
    #word.append("Start Message Block 0")
    count += 1
  elif x == ("00000101\n") and count == 0:
    count += 1
  elif count == 1:
    wordNum = int(x,2)
    #word[8] = wordNum
    count += 1
  elif (count < 10 and count > 1):
    y = x[:4]
    z = x[4:8]
    y = hex(int(y,2))[2:]
    z = hex(int(z,2))[2:]
    y = y.upper()
    z = z.upper()
    word[7-(count-2)] = y + z
    count += 1
  elif count == 10:
    program.append(word)
    #f3.write(str(word))
    #f3.write('\n')
    print(str(word))
    count = 0
    word = [None] * 8
  # elif count == 2:
    # y = x[:4]
    # z = x[4:8]
    # y = hex(int(y,2))[2:]
    # z = hex(int(z,2))[2:]
    # y = y.upper()
    # z = z.upper()
    # word[1] = y + z
    # count += 1
  # elif count == 3:
    # y = x[:4]
    # z = x[4:8]
    # y = hex(int(y,2))[2:]
    # z = hex(int(z,2))[2:]
    # y = y.upper()
    # z = z.upper()
    # word[0] = y + z
    # count += 1
  # elif count == 4:
    # y = x[:4]
    # z = x[4:8]
    # y = hex(int(y,2))[2:]
    # z = hex(int(z,2))[2:]
    # y = y.upper()
    # z = z.upper()
    # word[3] = y + z
    # count += 1
  # elif count == 5:
    # y = x[:4]
    # z = x[4:8]
    # y = hex(int(y,2))[2:]
    # z = hex(int(z,2))[2:]
    # y = y.upper()
    # z = z.upper()
    # word[2] = y + z
    # count += 1
  # elif count == 6:
    # y = x[:4]
    # z = x[4:8]
    # y = hex(int(y,2))[2:]
    # z = hex(int(z,2))[2:]
    # y = y.upper()
    # z = z.upper()
    # word[5] = y + z
    # count += 1
  # elif count == 7:
    # y = x[:4]
    # z = x[4:8]
    # y = hex(int(y,2))[2:]
    # z = hex(int(z,2))[2:]
    # y = y.upper()
    # z = z.upper()
    # word[4] = y + z
    # count += 1
  # elif count == 8:
    # y = x[:4]
    # z = x[4:8]
    # y = hex(int(y,2))[2:]
    # z = hex(int(z,2))[2:]
    # y = y.upper()
    # z = z.upper()
    # word[7] = y + z
    # count += 1
  # elif count == 9:
    # y = x[:4]
    # z = x[4:8]
    # y = hex(int(y,2))[2:]
    # z = hex(int(z,2))[2:]
    # y = y.upper()
    # z = z.upper()
    # word[6] = y + z
    # count += 1
  # elif count == 10:
    # program.append(word)
    # #f3.write(str(word))
    # #f3.write('\n')
    # print(str(word))
    # count = 0
    # word = [None] * 8
  if count > 1 & count < 10:
    printme = x[0:-1]
    printme1 = printme[3::-1]
    printme2 = printme[8::-1][0:4]
    #print(printme, printme1, printme2)
    print('{0:02X}'.format(int(printme2,2)),'{0:02x}'.format(int(printme1,2)))



for i in range(len(program)-1):
  #f2.write("\nWord Number: %d" % i)
  #f2.write('\n')
  last_wrote_op = 0 #bytes written since last opcode
  for j in range(8):
    num = int(program[i][j],16)
    if last_wrote_op > 0:
        if program[i][j] in machineOp:
            last_wrote_op = 0
            f2.write('\n')
            char = chr(int(program[i][j],16))
            f2.write(machineOp[program[i][j]] + '\t')
            f2.write('{0:02X}'.format(num))     
            #print('{0:02X}'.format(num))
            f2.write('\t')
        else:
            f2.write('{0:02X}'.format(num))
    else:
        last_wrote_op += 1
        #if(num in range(32-128)):
        char = chr(int(program[i][j],16))
        f2.write('{0:02X}'.format(num))
    #else:
    #  #if(num in range(32-128)):
    #  char = chr(int(program[i][j],16))
    #  f2.write('{0:02X}'.format(num))
'''
for i in range(0,len(program)-1):
  f2.write("Word Number: %d\n" % i)
  f2.write("sy:    Hex:       opCode:      characters:")
  f2.write("%d     %s%s       " % (0, program[i][0], program[i][1]), end= " ")
  if program[i][0] in machineOp: 
    f2.write("%s %s       " % (machineOp[program[i][0]], program[i][1]), end=" ")
  else:
    f2.write("No opCode  ", end=" ")
  f2.write("%s%s" % ( chr(int(program[i][0],16)), chr(int(program[i][1],16)) ) )

  f2.write("%d     %s%s       " % (1, program[i][2], program[i][3]), end= " ")
  if program[i][2] in machineOp: 
    f2.write("%s %s       " % (machineOp[program[i][2]], program[i][3]), end=" ")
  else:
    f2.write("No opCode  ", end=" ")
  f2.write("%s%s" % ( chr(int(program[i][2],16)), chr(int(program[i][3],16)) ) )

  f2.write("%d     %s%s       " % (2, program[i][4], program[i][5]), end= " ")
  if program[i][4] in machineOp: 
    f2.write("%s %s       " % (machineOp[program[i][4]], program[i][5]), end=" ")
  else:
    f2.write("No opCode  ", end=" ")
  f2.write("%s%s" % ( chr(int(program[i][4],16)), chr(int(program[i][5],16)) ) )

  f2.write("%d     %s%s       " % (3, program[i][6], program[i][7]), end= " ")
  if program[i][6] in machineOp: 
    f2.write("%s %s       " % (machineOp[program[i][6]], program[i][7]), end=" ")
  else:
    f2.write("No opCode  ", end=" ")
  f2.write("%s%s" % ( chr(int(program[i][6],16)), chr(int(program[i][7],16)) ) )
'''


  #print("%d     %s%s       %s         " % (0,program[i][0], program[i][1], machineOp[program[i][0]] ))
  #print("%d     %s%s       %s         " % (1,program[i][2], program[i][3], machineOp[program[i][2]] ))
  #print("%d     %s%s       %s         " % (2,program[i][4], program[i][5], machineOp[program[i][4]] ))
  #print("%d     %s%s       %s         " % (3,program[i][6], program[i][7], machineOp[program[i][6]] ))


'''
for i in range(len(program)-1):
  print("word number %d\n" % i)
  #print(program[i])
  for j in range(8):
    if j%2 == 0:
      if program[i][j] in machineOp:
        print("opCode                         %s " % machineOp[program[i][j]])
      else:
        print("Possible Character             %s" % chr(int(program[i][j],16)))
    else:
       print("Hex: %s or possible Character: %s" %  (program[i][j], chr(int(program[i][j],16))))

  for j in range(8):
    if j%2 == 0:
      if program[i][j] in machineOp and machineOp[program[i][j]] == "SRJ":
        print("opCode: %s  | parameters: %s" % (machineOp[program[i][j]], chr(int(program[i][j+1],16))))
      elif program[i][j] in machineOp:
        print("opCode: %s  | parameters: %s" % (machineOp[program[i][j]], program[i][j+1]))
      elif program[i][j] not in machineOp:
        print("possible characters: %s %s" % (chr(int(program[i][j],16)), chr(int(program[i][j+1],16))))
    #f2.write("%s\n" % program[i])
'''
