import sys
input,output=sys.argv[1],sys.argv[2]
def bubble_sort(my_list1):
    n = len(my_list1)
    for i in range(n):
        for j in range(0, n - i - 1):
            if my_list1[j] > my_list1[j + 1]:
                my_list1[j], my_list1[j + 1] = my_list1[j + 1], my_list1[j]
    return my_list1


def my_frequency_with_dict(list):
    frequency_dict1 = {}
    for item in list1:
        item=int(item)
        if item in frequency_dict1 :
            frequency_dict1[item] = frequency_dict1[item] + 1
        else:
            frequency_dict1[item] = 1
    print(frequency_dict1)
    return frequency_dict1

def my_mode_with_dict(my_hist_d):
    frequency_max = -1 
    mode = -1

    for key in my_hist_d.keys():
        if my_hist_d[key] > frequency_max:
            frequency_max = my_hist_d[key]
            mode = key
    return mode,frequency_max

def medyan_Bul(dizi):
    dizi= bubble_sort(dizi)
    if len(dizi)%2==1:
        orta = int(len(dizi)/2)+1
        return dizi[orta-1]
    else:
        orta1,orta2=dizi[int(len(dizi)/2)],dizi[int(len(dizi)/2)-1]
        return (orta1+orta2)/2



def liste_Ortalama(liste):
    toplam = 0
    s=0
    for item in liste:
        toplam += int(item)
        s += 1
    return int(toplam/s)



with open(input+"input_hw_2.csv", "r") as dosya:
    data = []
    data1 = dosya.read()
    data_line = data1.split(';')
    data.append(data_line)
    date = []
    ayir = []
    for i in range(3, len(data_line), 3):
        ayir.append(data_line[i].split("-"))

    aylar = []
    for i in range(len(ayir)):
        aylar.append(int(ayir[i][1]))

bubble_sort(aylar)
a = my_frequency_with_dict(aylar)
listeYeni = [a[i] for i in a]


with open(output+"180401018_hw_2_output.txt", "w") as dosya:

    dosya.write("Medyan :"+ "" + str(medyan_Bul(listeYeni))+"\n")
    dosya.write("Ortalama:" + ""+ str(liste_Ortalama(listeYeni)))
