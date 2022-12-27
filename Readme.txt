*_*_*_*_*_*_*_*_*_*__*---AES-128----*_*_*_*_*_*_*_*_*_*_*_*


input file--->
                input.pt includes the input plain text
key----->
                key.key includes the key
encryptionTextFile --->
                includes the encrypted text after 10 rounds of AES
decryptedTextFile------>
                includes the decrypted text after 10 rounds



main.py is the driver file of this AES-128 implementation
place the text to encrypted in the input file and run the main.py file.
main.py will generate the 10 keys for the 10 rounds of encryption and decryption
and the outputs will be stored in the different file i.e encryptionTextFile and decryptedTextFile