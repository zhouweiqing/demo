//位图排序
#include <iostream>
#include <bitset>
#define WIDTHWORD 32 //一个整数的宽度是32bit
#define SHIFT 5
#define MASK 0x1F    //0x1f == 31
#define N 100        //对十万个无重复的整数排序
using namespace std;

//申请一个N位的bitmap
int bitmap[1 + N / WIDTHWORD];

//将bitmap的第value设置为1
void set(int value) {
    bitmap[value >> SHIFT] |= (1 << (value & MASK));
}

//清除bitmap第value位上的1:设置为0
void clear(int value) {
    bitmap[value >> SHIFT] &= ~(1 << (value & MASK));
}

//测试bitmap第value位是否为1
int test(int value) {
    return bitmap[value >> SHIFT] & (1 << (value & MASK));
}

int main() {
    int a[] = {12, 5, 1, 89, 64, 49, 77, 91, 3, 0, 32, 50, 99};
    int length = sizeof(a) / sizeof(int);

    //将bitmap所有位设置为0
    for (int i = 0; i < N; ++i) {
        clear(i);
    }

    //bitmap中将待排序数组中值所在的位设置为1
    for (int i = 0; i < length; i++)
        set(a[i]);

    //输出排序后的结果
    for (int i = 0; i < N; ++i) {
        if (test(i))
            cout << i << " ";
    }
    cout << endl;
}
