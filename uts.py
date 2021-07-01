import cv2
#membaca gambarnya dulu
#1 untuk warna
img = cv2.imread ('ilham.jpg',1)
#0 untuk abu-abu
imgGray = cv2.imread ('ilham.jpg',0)
#resize ukuran menjadi 400x400 px
width = 400
height= 400
size = (width,height)
newSize = cv2.resize(img,size)
#membuat fungsi warna cerah dan inversi
cerah= newSize-5
inversi = 255-newSize
#menampilkan gambar resize asli,resize cerah,dan resize inversi
cv2.imshow('ilham 400x400',newSize)
cv2.imshow('ilham 400x400 Cerah',cerah)
cv2.imshow('ilham 400x400 Inversi',inversi)
#fungsi close dan simpan gambar
k= cv2.waitKey(0)& 0xFF
# esc tanpa save gambar
if k == 27:
    cv2.destroyAllWindows()
#jika menekan s menyimpan 3 gambar yaitu asli,cerah,dan inversi ukuran 400x400
elif k == ord ('s'):
    cv2.imwrite('ilham 400x400.jpg',newSize)
    cv2.imwrite('ilham 400x400 Cerah.jpg',cerah)
    cv2.imwrite('ilham 400x400 Inversi.jpg',inversi)
    cv2.destroyAllWindows()
#jika menekan g menyimpan gambar abu-abu ukuran normal
elif k == ord ('g'):
    cv2.imwrite('ilhamGray.jpg',imgGray)
    cv2.destroyAllWindows()
