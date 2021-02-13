import numpy as np
import matplotlib.pyplot as plt

def isValidConstant(constantRealAxis, constantImaginaryAxis):
  complexNumber = complex(0,0)
  for i in range(100):
    complexNumber = (complexNumber*complexNumber) + complex(constantRealAxis, constantImaginaryAxis)
    if(complexNumber.real< 1 and complexNumber.imag < 1 and complexNumber.real > -1 and complexNumber.imag> -1):
        continue
    else:
        return False
  return True

def getData():
    data = []
    for real1 in range(-100, 100):
        for imag1 in range(-100, 100):
            real1Decimal = real1/1000
            imag1Decimal = imag1/100
            if(isValidConstant(real1Decimal, imag1Decimal)):
                data.append([real1Decimal, imag1Decimal])

    for imag2 in range(-100, 100):
        for real2 in range(-100, 100):
            real2Decimal = real2/100
            imag2Decimal = imag2/100
            if(isValidConstant(real2Decimal, imag2Decimal)):
                data.append([real2Decimal, imag2Decimal])

    return np.array(data);

dataArray = getData()

plt.scatter(dataArray[:,0], dataArray[:,1])
plt.title('Mandelbrot Set')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.show()
