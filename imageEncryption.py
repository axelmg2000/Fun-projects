# 28 de junio del 2021
# Axel Mercado Gasque

def encryptImg(filePath):
      # take path of image as a input
      path = filePath


      # taking encryption key as input
      key = int(input('Enter Key for encryption of Image : '))

      # print path of image file and encryption key that
      # we are using
      print('The path of file : ', filePath)
      print('Key for encryption : ', key)

      # open file for reading purpose
      fin = open(filePath, 'rb')

      # storing image data in variable "image"
      image = fin.read()
      fin.close()

      # converting image into byte array to 
      # perform encryption easily on numeric data
      image = bytearray(image)

      # performing XOR operation on each value of bytearray
      for index, values in enumerate(image):
            image[index] = values ^ key

      # opening file for writting purpose
      fin = open(filePath, 'wb')

      # writing encrypted data in image
      fin.write(image)
      fin.close()
      print('Encryption Done...')
  

def decryptImg(filePath):
      # taking decryption key as input
      key = int(input('Enter Key for encryption of Image : '))

      # print path of image file and decryption key that we are using
      print('The path of file : ', filePath)
      print('Note : Encryption key and Decryption key must be same.')
      print('Key for Decryption : ', key)

      # open file for reading purpose
      fin = open(filePath, 'rb')

      # storing image data in variable "image"
      image = fin.read()
      fin.close()

      # converting image into byte array to perform decryption easily on numeric data
      image = bytearray(image)

      # performing XOR operation on each value of bytearray
      for index, values in enumerate(image):
            image[index] = values ^ key

      # opening file for writting purpose
      fin = open(filePath, 'wb')

      # writing decryption data in image
      fin.write(image)
      fin.close()
      print('Decryption Done...')
  
  
def main():
      path = input('Enter path of file: ')
      option = input('Encrypt or Decrypt? (E/D)')

      while(option != 'E' and option != 'D'):
            option = input('Encrypt or Decrypt? (E/D)')

      if(option == 'E'):
            encryptImg(path)
      else:
            decryptImg(path)


# Execute main
main()