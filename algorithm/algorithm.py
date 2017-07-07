import random, time

def get_arr(n=10):
    l = [x for x in range(1, n+1)]
    random.shuffle(l)
    return l

def test_sort(sort):
    "装饰器，用于测试排序"
    def wrapper(*args, **kwargs):
        arr = get_arr()
        print(arr)
        t1 = time.time()
        f = sort(arr)
        t2 = time.time()
        print(arr)
        print("[%s] cost %dms." %(sort.__name__, (t2-t1)))
        return f
    return wrapper

############################################################
# 1.排序算法                                                #
############################################################

# 1.1 直接插入排序
@test_sort
def insert_sort(a):
    for i in range(1, len(a)):   # 从第二个元素开始遍历到最后一个
        k = a[i]            # 定义 key 值
        j = i - 1           # 定义已排序列表的最大索引值
        while j >= 0 and a[j] > k:  # 遍历已排序列表
            a[j+1] = a[j]
            j -= 1
        a[j+1] = k

# 1.2 希尔排序
@test_sort
def shell_sort(a):
    n = len(a)
    d = n >> 1     # x 右移 n 位，表示 x / 2^n
    while d > 0:
        for i in range(d, n):
            j = i-d
            while j >= 0 and a[j] > a[j+d]:
                a[j], a[j+d] = a[j+d], a[j]
                j = j-d
        d = d >> 1

# 1.3 冒泡排序
@test_sort
def bubble_sort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]

# 1.4 快速排序
def quick_sort(a, left, right):
    if left < right:
        povit = a[left]
        low = left
        high = right
        while low < high:
            while low < high and a[high] > povit:
                high -= 1
            a[low] = a[high]
            while low < high and a[low] <= povit:
                low += 1
            a[high] = a[low]
        a[low] = povit
        quick_sort(a, 0, low-1)
        quick_sort(a, low+1, right)
        
# 1.5 直接选择排序
@test_sort
def select_sort(a):
    n = len(a)
    for i in range(n-1):
        k = i
        for j in range(i+1, n):
            if a[k] > a[j]:
                k = j
        if k != i:
            a[i], a[k] = a[k], a[i]

# 1.6 堆排序
@test_sort
def heap_sort(a):
    # 初始化堆
    n = len(a)
    for i in range(n):
        create_heap_top(a, (n-1)-i)
        swap(a, 0, (n-1)-i)

def swap(a, i, j):
    if i == j:
        return
    else:
        a[i] = a[i] + a[j]
        a[j] = a[i] - a[j]
        a[i] = a[i] - a[j]
    pass

def create_heap_top(a, l):
    n = (l - 1) // 2
    for i in range(n, -1, -1):
        k = i   # 保存当前正在判断的节点
        # 若当前节点的子节点存在
        while 2*k+1 <= l:
            # bigger 总是记录较大节点的值,先赋值为当前判断节点的左子节点
            bigger = 2*k+1
            if bigger < l:
                # 若右子节点存在，否则此时biggerIndex应该等于 lastIndex
                if a[bigger] < a[bigger+1]:
                    # 若右子节点值比左子节点值大，则biggerIndex记录的是右子节点的值
                    bigger += 1
            if a[k] < a[bigger]:
                # 若当前节点值比子节点最大值小，则交换2者得值，交换后将biggerIndex值赋值给k
                swap(a, k, bigger)
                k = bigger
            else:
                break

# 1.7 归并排序
def merge_sort(a, low, high):
    n = len(a)
    if low < high:
        mid = (low + high) >> 1
        merge_sort(a, low, mid)
        merge_sort(a, mid+1, high)
        merge(a, low, mid, high)

def merge(a, low, mid, high):
    i, j, tmp = low, mid + 1, []
    while i <= mid and j <= high:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    while i <= mid:
        tmp.append(a[i])
        i += 1
    while j <= high:
        tmp.append(a[j])
        j += 1
    a[low:high + 1] = tmp

# 1.8 基数排序



############################################################
# 2.查找算法                                                #
############################################################

if __name__ == "__main__":
    a = get_arr()
    print(a)
    merge_sort(a, 0, len(a)-1)
    print(a)
    
    # merge_sort()