def character_extension():  # 将文本以text.txt的形式放入python所在的文件夹

  extention_dic={             #E\F\G extension,list是extension的開頭字和結束字的16進制unicode
      "E":["0x2B820","0x2CEAF"],
      "F":["0x2CEB0","0x2EBEF"],
      "G":["0x30000","0x3134F"],
  }
  text_addr = "text.txt"
  chr_dic={}
  f = open(text_addr)
  text = f.read()           #將文本內容存為字符串

  for i in text:           #開始檢索每一個文本的字
    unicode=ord(i)           #將字轉化為unicode
    for j in ["E","F","G"]:     #檢索3個extension
      if unicode in range(eval(extention_dic[f"{j}"][0]),eval(extention_dic[f"{j}"][1])):  #如果字的unicode在某個extention範圍內
        chr_dic[i]=j
      else: 
        continue
  print(chr_dic)
character_extension()
