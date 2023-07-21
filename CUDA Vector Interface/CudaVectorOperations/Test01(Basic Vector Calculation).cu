//Basic Demonstration of how to use Kernal Vector Operations
#include <iostream>
#include "CudaVectorOperations.cuh"

__global__ void addKernel(int* c, const int* a, const int* b) {
    int i = threadIdx.x;
    c[i] = a[i] + b[i];
    printf("%d + %d = %d\n", a[i], b[i], c[i]);
}

__global__ void multiplyKernel(int* c, const int* a, const int* b) {
    int i = threadIdx.x;
    c[i] = a[i] * b[i];
    printf("%d * %d = %d\n", a[i], b[i], c[i]);
}

int main(void) {
    KernalVectorOperation kvOPAdd = *addKernel;
    KernalVectorOperation kvOPMult = *multiplyKernel;
    int* output = new int[50000];
    int* a = new int[50000];
    int* b = new int[50000];

    for (int i = 1; i <= 50000; i++) {
        a[i - 1] = i;
        b[i - 1] = i * 10;
    }

    performVectorOperation(output, a, b, 50000, kvOPAdd);

    performVectorOperation(output, a, b, 50000, kvOPMult);

    delete[] output;
    delete[] a;
    delete[] b;

    return 0;

}