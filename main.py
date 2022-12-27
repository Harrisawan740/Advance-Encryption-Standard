

INV_SBOX= [
    [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb],
    [0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb],
    [0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e],
    [0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25],
    [0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92],
    [0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84],
    [0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06],
    [0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b],
    [0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73],
    [0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e],
    [0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b],
    [0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4],
    [0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f],
    [0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef],
    [0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61],
    [0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]
]

RCJ_128 = [
    [0x01, 0x00, 0x00, 0x00],
    [0x02, 0x00, 0x00, 0x00],
    [0x04, 0x00, 0x00, 0x00],
    [0x08, 0x00, 0x00, 0x00],
    [0x10, 0x00, 0x00, 0x00],
    [0x20, 0x00, 0x00, 0x00],
    [0x40, 0x00, 0x00, 0x00],
    [0x80, 0x00, 0x00, 0x00],
    [0x1B, 0x00, 0x00, 0x00],
    [0x36, 0x00, 0x00, 0x00]
]
SBOX = [
    [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
    [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
    [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
    [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
    [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
    [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
    [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
    [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
    [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
    [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
    [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
    [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
    [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
    [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
    [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
    [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]
]
IRP = int("00011011",2)
def convert_to_hex_list(li):
    ret= []
    # print(li)
    for i in range(0,len(li)):
        temp_list = []
        for j in range(0,len(li[i])):
            temp = hex(int(li[i][j]))
            temp_list.append(temp)
        ret.append(temp_list)
        # if(len(temp)== 3):
        #     index1 = 0
        #     index2 = int(temp[2],16)
        # else:
        #     index1 = int(temp[2],16)
        #     index2 = int(temp[3],16)
        
    print('ret:',ret)

def convert_to_hex_and_display(li):
    for i in range(0,len(li)):
        for j in range(0,4):
            print(hex(li[i][j]),end=' ')
        print()
def make_key(w4,w5,w6,w7):
    temp = [[w4[0],w5[0],w6[0],w7[0]],
            [w4[1],w5[1],w6[1],w7[1]],
            [w4[2],w5[2],w6[2],w7[2]],
            [w4[3],w5[3],w6[3],w7[3]]
            ]
    return temp

def ret_key(key):
    
    expanded_keys = [key]
    for i in range(0,10):
        ret = g_func(expanded_keys[i],i)
        # print("Returned Value")
        # print(ret)
        expanded_keys.append(ret)
    # convert_to_hex_and_display(expanded_keys[3])
    return expanded_keys
def g_func(key,round_no):

    ret = ret_column(key,3)

    # print("last col: ", ret)

    ret = shift_rows(ret , 1)

    # print("Shift rows: ",ret)

    ret = sbox(ret)

    # print("sbox: ",ret)

    ret = rcj(ret,round_no)

    # print("RCJ: ",ret)

    w0 = ret_column(key,0)
    w1 = ret_column(key,1)
    w2 = ret_column(key,2)
    w3 = ret_column(key,3)
    # print("Words")
    # print(w0)
    # print(w1)
    # print(w2)
    # print(w3)    
    w4 = XOR(w0,ret)

    w5 = XOR(w1,w4)

    w6 = XOR(w2,w5)

    w7 = XOR(w3,w6)

    # print("w4: ",w4)
    # print("w5: ",w5)
    # print("w6: ",w6)
    # print("w7: ",w7)

    ret = make_key(w4,w5,w6,w7)
    # print('key->',ret)
    return ret
    #return w'

def inv_SBOX_for_round(li):
    ret = []
    index1 = -1
    index2 = -1
    for i in range(0,len(li)):
        ret.append(inv_sbox(li[i]))
    return ret

def inv_sbox(col):
    ret = []
    index1 = -1
    index2 = -1
    for i in range(0,len(col)):
        temp = hex(int(col[i]))
        # print("temp in hex: ",temp)
        if(len(temp)== 3):
            index1 = 0
            index2 = int(temp[2],16)
        else:
            index1 = int(temp[2],16)
            index2 = int(temp[3],16)
        # print(index1,index2)
        ret.append(INV_SBOX[index1][index2])
    return ret
def SBOX_for_round(li):
    ret = []
    index1 = -1
    index2 = -1
    for i in range(0,len(li)):
        ret.append(sbox(li[i]))
    return ret
def sbox(col):

    ret = []
    index1 = -1
    index2 = -1
    for i in range(0,len(col)):
        temp = hex(int(col[i]))
        # print("temp in hex: ",temp)
        if(len(temp)== 3):
            index1 = 0
            index2 = int(temp[2],16)
        else:
            index1 = int(temp[2],16)
            index2 = int(temp[3],16)
        # print(index1,index2)
        ret.append(SBOX[index1][index2])
    return ret
def XOR(col1,col2):
    ret = []
    for i in range(0,len(col1)):
        ret.append(int(col1[i]) ^ col2[i])
    return ret
def rcj(col,round_no):
    rcj_row = RCJ_128[round_no]
    # print(rcj_row)
    ret = XOR(col,rcj_row)
    return ret
def inv_shift_for_rounds(li):
    ret = []
    for i in range(0,len(li)):
        ret.append(inv_shift_rows(li[i],i))
    return ret
def inv_shift_rows(col,n):
    n = n * -1
    return col[n:] + col[:n]
def shift_for_rounds(li):
    ret = []
    for i in range(0,len(li)):
        ret.append(shift_rows(li[i],i))
    return ret
def shift_rows(col,n):
    return col[n:] + col[:n]

def inv_mix_columns(state):
    # print(state)
    fix = [
        [0xE, 0xB, 0xD, 0x9],
        [0x9, 0xE, 0xB, 0xD],
        [0xD, 0x9, 0xE, 0xB],
        [0xB, 0xD, 0x9, 0xE]
        ]
    mix_res = []
    for i in range(0,len(fix)):
        temp_list = []
        for j in range(0,4):
            result = int('0',2)
            for k in range(0,4):
                # print (state[i][k],hex(fix[k][j]))
                ret = GF(state[i][k],fix[k][j])

                # print("GF ret:",ret)
                result ^= ret
            temp_list.append(result)
                # print('temp_list: ',hex(temp_list[0]))
            # print("result: ",hex(result))
        mix_res.append(temp_list)
    return mix_res
def mix_columns(state):

    fix = [[0x2,0x3,0x1,0x1],
          [0x1,0x2,0x3,0x1],
          [0x1,0x1,0x2,0x3],
          [0x3,0x1,0x1,0x2]
        ]
    mix_res = []
    for i in range(0,len(fix)):
        temp_list = []
        for j in range(0,4):
            result = int('0',2)
            for k in range(0,4):
                # print (hex(fix[i][k]),hex(state[k][j]))
                ret = GF(fix[i][k],state[k][j])

                # print("ret: ",'{:08b}'.format(ret))
                result ^= ret
            temp_list.append(result)
                # print('temp_list: ',hex(temp_list[0]))
            # print("result: ",hex(result))
        mix_res.append(temp_list)
    return mix_res
def left_shift(s):
    carry = s[0]
    s = s[1:]
    s = s +'0'
    return s
def GF(a,b):
    f_x = -1
    g_x = -1

    if(a > b):
        f_x = a
        g_x = b
    else:
        g_x = a
        f_x = b

    g_x = bin(g_x)[2:]
    f_x = '{:08b}'.format(f_x)

    val = []
    count = 0
    for bit in reversed(g_x):
        # print("bit->",bit)
        if(bit == '1' and count < 1):
            val.append(f_x)
        elif(bit == '1' and count >= 1):
            carry = f_x [0]
            # print("carry->",carry)
            f_x = left_shift(f_x)
            # print("shifted f_x-->>",f_x)
            if carry == '1':
                f_x = int(f_x,2) ^ IRP
                # print('F_x in carry--->',bin(f_x))
                val.append('{:08b}'.format(f_x))
                f_x = '{:08b}'.format(f_x)
            else:
                val.append(f_x)
        count+=1
    result = int('0',2)
    # print("val->>",val)
    for value in val:
        result ^= int(value,2)
        # print('result in loop--->','{:08b}'.format(result))

    return result
def add_round_key(pt,key):
    ret = []
    for i in range(0,len(pt)):
        temp_list = []
        for j in range(0,len(pt[i])):
            temp_list.append(pt[i][j] ^ key[i][j])
        ret.append(temp_list)
    return ret

def ret_column(key,col_no):

    last = [key[0][col_no],key[1][col_no],key[2][col_no],key[3][col_no]]

    return last
def read_file(path):
    readfile = open(path,'r')
    key_list = []
    temp_list=[]
    count = 0
    while True:
        temp = readfile.read(2)
        if not temp:
            break
        temp_list.append(int("0x"+temp,16))
        count+=1
        if(count == 4):
            key_list.append(temp_list)
            temp_list=[]
            count = 0
    return key_list
def Encryption(Plain_text,expanded_keys):
    ret_round = add_round_key(Plain_text,expanded_keys[0])
    print("after add round key 0 : ",ret_round)
    # round1
    
    for i in range(0,10):
        print(f"_*_*_*_*_*_*_Round-{i+1}_*_*_*_*_*_*_*")
        ret_sbox = SBOX_for_round(ret_round)
        print(f"After SBOX{i+1}: ",ret_sbox)
        ret_shift = shift_for_rounds(ret_sbox)

        print(f"After ShiftRows{i+1}: ",ret_shift)
        ret_mix = mix_columns(ret_shift)
        if(i == 9):
            ret_mix = ret_shift
        if(i!=9):
            print(f"After MixCols{i+1}: ",ret_mix)
        ret_round = add_round_key(ret_mix,expanded_keys[i+1])
    
        print(f"After add round key {i+1} : ",ret_round)
    return ret_round

def Decryption(EncryptedText,expanded_keys):
    
    print("_*_*_*_*_*_*_*-Decryption-*_*_*_*_*_*_* ")
    
    # round10
    for i in range(10,0,-1):
        print(f"_*_*_*_*_*_*_Round-{i}_*_*_*_*_*_*_*")
        
        ret_round = add_round_key(EncryptedText,expanded_keys[i])

        print(f"After add round key {i} : ",ret_round)

        ret_mix = inv_mix_columns(ret_round)
        if(i == 10):
            ret_mix = ret_round
        if(i != 10):
            print(f"After MixCols{i}: ",ret_mix)
    
        ret_shift = inv_shift_for_rounds(ret_mix)

        print(f"After ShiftRows{i}: ",ret_shift)

        ret_sbox = inv_SBOX_for_round(ret_shift)
        print(f"After SBOX{i}: ",ret_sbox)
       
        EncryptedText = ret_sbox

    #last
    ret_round = add_round_key(ret_round,expanded_keys[0])
    
    return ret_round
def write_cipher(cipher):
    f = open("encryptionTextFile.enc", "w")
    for i in range (len(cipher)):
        for j in range(0,4):
            f.write(str(hex(cipher[i][j])[2:]))
    f.close()
def write_decryptedText(text):
    f = open("decryptedTextFile.dec", "w")
    for i in range (len(text)):
        for j in range(0,4):
            f.write(str(hex(text[i][j])[2:]))
    f.close()
def main():


    key = read_file('Key.key')

    expanded_keys = ret_key(key)



    Plain_text = read_file('input.pt')


    cipher = Encryption(Plain_text,expanded_keys)

    write_cipher(cipher)

    print("Cipher---> ",cipher)


    read_cipher = read_file ('encryptionTextFile.enc')


    print("Read cipher--->",read_cipher)

    decrypt = Decryption(cipher,expanded_keys)

    write_decryptedText(decrypt)

    print ("Decrypted Text--->",decrypt)

if __name__ == '__main__':
    main()
