# Nama          : Jusuf Junior Athala
# NIM           : 13519174
# Mata kuliah   : IF2211 - Strategi Algoritma
# Kelas         : K-04
# Tugas         : Tugas Kecil 02
# Nama file     : Tucil02_13519174.py


#fungsi untuk membaca file dan mengembalikan isi dari file dalam bentuk string
def bacaFile():

    fileinput=input("Masukkan nama file (contoh: 'input1.txt'): ")
    f=open("../test/"+fileinput, "r")
    contents =f.read()
    return contents

#fungsi membuat dictionary dari matakuliah yang muncul
def makeDictionary(matkul,sentence):
    separator =', '
    mydict = { }
    for mat in matkul:
        count = 0
        value = 0
        temp=mat
        for sen in sentence :
            if (sen.find(mat)==0):                  #jika matkul berada pada posisi awal, matkul lainnya akan menjadi value untuk dictionary dari matkul posisi awal
                value = sen.count(separator)        #, matkul lainnya akan menjadi value untuk dictionary dari matkul posisi awal
        mydict[mat]=value
    return mydict

#fungsi topoogical Sort
def topoSort(mydict,key_list,val_list,sentence,matkul):
    count=1
    while (len(mydict)>0):
        first = True
        print ("Semester ",count," :", end =" ")
        for i in range(len(val_list)):
            if (val_list[i]==0):                #Mencari mata kuliah dengan value prerequisite bernilai 0
                if (first) :                    
                    print(key_list[i], end ="")
                    first = False
                else :
                    print(",",key_list[i], end="")

                temp=key_list[i]                #Mengakses nama kunci pada index i

                for sen in sentence:            #Jika mata kuliah merupakan prerequisite dari matkul lain, value dari matkul lain tersebut berkurang 1
                    if (sen.find(temp)>1):
                        for mat in matkul:
                            if (sen.find(mat)==0):
                                mydict[mat]= mydict.get(mat)-1
                                
                del mydict[temp]                #Penghapusan kode matkul dari dictionary
        count+=1
        print("")
        key_list = list(mydict.keys())          #Mengupdate list kode matkul dan value prerequisite setelah dilakukan 
        val_list = list(mydict.values())        #pengurangan value dan penghapusan kode matkul dari dictionary

        
if __name__ == '__main__':
#Memulai program dengan membaca masukan file
    contents = bacaFile()   

#contents yang berupa string akan diolah dan dipisahkan  
    sentence = contents.replace(".","").split("\n")     #setiap line dipisah menjadi bentuk <kode_kuliah_1>,<kode kuliah prasyarat - 1>, <kode kuliah prasyarat - 2>, dst.                       
    muncul = contents.replace (", ","\n").replace(".","").split("\n")     #penghapusan karakter yang tidak digunakan dan setiap kode kuliah akan dipisahkan masing-masing
    matkul = set(muncul)        #menghapus duplikat dari mata kuliah yang muncul menggunakan set
    matkul = list(matkul)       #mengubah set menjadi list

#Membuat list dan dictionary dari hasil pengolahan string
    mydict = makeDictionary(matkul,sentence)    
    key_list = list(mydict.keys())      #kode matkul dalam bentuk list
    val_list = list(mydict.values())    #value prerequisite dari setiap kode matkul dalam bentuk list
                                        #list kode matkul dan value dari setiap kode matkul sesuai

    print ("Hasil topological sort adalah: ")
#Melakukan topological sort
    topoSort(mydict,key_list,val_list,sentence,matkul)
    selesai = input('Tekan Enter untuk keluar dari program')
