
# encoding: utf-8
def OctEncrypt(data):
    key = generateOctKey(data)
    data = [ord(c) for c in data]
    encryptedData = ''
    for i in range(len(data)):
        val = data[i] - (key[i]*(-1))

        encryptedData += chr(val)
    return encryptedData

def decryptOctData(encryptedData: str):
    key = generateOctKey(encryptedData)
    encryptedData = [ord(c) for c in encryptedData]
    password = ''
    for i in range(len(encryptedData)):
        val = encryptedData[i] + (key[i]*(-1))
        password += chr(val)
    return password

def generateOctKey(text: str):
    key = []
    num = 0
    for c in text:
        key.append((11-num))
        num += 2
    return key
encrypted_data = '_jk87130'
decrypted_data = decryptOctData(encrypted_data)
print(decrypted_data)