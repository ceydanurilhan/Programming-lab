import numpy as np
import matplotlib.pyplot as plt

def min_heapify(array,i): # Parametre olarak bir dizi ve indeks değeri alır.Dizideki i indeksinden başlayıp tüm elemanları sağ ve sol düğümleri ile karşılaştırıp gerekli yer değişimlerini yaparak diziyi heape dönüştürmemizi sağlar.
  left = 2 * i + 1
  right = 2 * i + 2
  length = len(array) - 1
  smallest = i
  if left <= length and array[i] > array[left]:
    smallest = left
  if right <= length and array[smallest] > array[right]:
    smallest = right
  if smallest != i:
    array[i],array[smallest] = array[smallest],array[i]
    min_heapify(array,smallest)

def build_min_heap(array): #Parametre olarak bir dizi alır. Diziyi heap haline getirmek için n/2 den 0 a kadar tüm elemanlara minheapify uygular
  for i in reversed(range(len(array)//2)):
    min_heapify(array,i)

my_array_1 = [8,10,3,4,7,15,1,2,16]
build_min_heap(my_array_1)
print(my_array_1)

def heapsort(array): # Parametre olarak bir dizi alır. Dizinin kopyasını alıp sıralama işlemi yapar
    array = array.copy()
    build_min_heap(array)
    sorted_array = []
    for _ in range(len(array)):
        array[0], array[-1] = array[-1], array[0]
        sorted_array.append(array.pop())
        min_heapify(array, 0)
    return sorted_array

my_array_1 = [8,10,3,4,7,15,1,2,16]
my_array_2 = heapsort(my_array_1)
print(my_array_1 , my_array_2)

def insertItemToHeap(myheap_1,item): # Parametre olarak bir heap yapısı ve eklenecek bir item alır. Heape gönderilen itemi ekler
    myheap_1.append(item)
    index = len(myheap_1)-1
    if index <= 0 :
        return
    parent = (index-1)//2
    while parent>=0 and myheap_1[parent] > myheap_1[index]:
        myheap_1[parent] , myheap_1[index] = myheap_1[index] , myheap_1[parent]
        index = parent
        parent = (index-1)//2

insertItemToHeap(my_array_1,6)
print(my_array_1)

def removeItemFrom(myheap_1): # Parametre olarak bir heap alır. Heap yapısından son elemanı silmemizi sağlar
    length = len(myheap_1)
    if length == 0:
        print("Heapte hiç eleman yok!")
        return myheap_1
    heapArray = heapsort(myheap_1)
    heapArray[0] , heapArray[-1] = heapArray[-1] , heapArray[0]
    heapArray.pop()
    build_min_heap(heapArray)
    return heapArray

removeItemFrom(my_array_1)
print(my_array_1)
