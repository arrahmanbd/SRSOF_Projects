import qrcode
import image
import random as rand
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
qr=qrcode.QRCode(
        version=15,
        box_size=10,
        border=5
)
data=input('Enter a data to generate qrcode :')

qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill='black',back_colour='white')
file_name=f'sanim_qr_{rand.randint(1,1000)}.jpg'
img.save(file_name)
plt.title("QR Code")
plt.xlabel("X pixel scaling")
plt.ylabel("Y pixels scaling")
image = mpimg.imread(file_name)
plt.imshow(image)
plt.show()