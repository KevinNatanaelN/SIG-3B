import shapefile #import kelas shapefile
sibin = shapefile.Writer('soal3', shapeType=1) #buat nama file 'soal3' dan menggunakan shapetype=1
sibin.shapeType

sibin.field("col1","C") #membuat tabel pertama
sibin.field("col2","C") #membuat tabel kedua

sibin.record("hiyak","satu") #membuat isi tabel hiyak
sibin.record("hiyok","dua") #membuat isi tabel hiyok

sibin.point(1,1) #titik di poin x dan y
sibin.point(2,1.5) #titik di poin x dan y

sibin.close() #mengakhiri kode