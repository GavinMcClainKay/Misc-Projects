#include <iostream>
#include "CudaVectorOperations.cuh"

cudaError_t setGPU(int device) {
    // Choose which GPU to run on, change this on a multi-GPU system.
    cudaError_t cudaStatus = cudaSetDevice(device);
    if (cudaStatus != cudaSuccess) {
        fprintf(stderr, "cudaSetDevice failed!  Do you have a CUDA-capable GPU installed?");
    }
    return cudaStatus;
}

cudaError_t allocateMemory(void** devPTR, unsigned int size) {
    cudaError_t cudaStatus = cudaMalloc((void**)&devPTR, size * sizeof(int));
    if (cudaStatus != cudaSuccess) {
        fprintf(stderr, "cudaMalloc failed!");
    }
    return cudaStatus;
}

cudaError_t performVectorOperation(int* output, const int* in_a, const int* in_b, unsigned int size, KernalVectorOperation operation) {
    int* dev_a = 0;
    int* dev_b = 0;
    int* dev_c = 0;

    cudaError_t cudaStatus;
    
    cudaStatus = setGPU(0);

    // Allocate GPU buffers for three vectors (two input, one output).
    cudaStatus = allocateMemory((void**)&dev_a, size * sizeof(int));
    cudaStatus = allocateMemory((void**)&dev_b, size * sizeof(int));
    cudaStatus = allocateMemory((void**)&dev_c, size * sizeof(int));



    // Copy input vectors from host memory to GPU buffers.
    cudaStatus = cudaMemcpy(dev_a, in_a, size * sizeof(int), cudaMemcpyHostToDevice);
    if (cudaStatus != cudaSuccess) {
        fprintf(stderr, "cudaMemcpy failed!");
        goto Error;
    }

    cudaStatus = cudaMemcpy(dev_b, in_b, size * sizeof(int), cudaMemcpyHostToDevice);
    if (cudaStatus != cudaSuccess) {
        fprintf(stderr, "cudaMemcpy failed!");
        goto Error;
    }



    // Launch a kernel on the GPU with one thread for each element.
    operation<<<50, 1000>>>(dev_c, dev_a, dev_b);



    // Check for any errors launching the kernel
    cudaStatus = cudaGetLastError();
    if (cudaStatus != cudaSuccess) {
        fprintf(stderr, "addKernel launch failed: %s\n", cudaGetErrorString(cudaStatus));
        goto Error;
    }

    // cudaDeviceSynchronize waits for the kernel to finish, and returns
    // any errors encountered during the launch.
    cudaStatus = cudaDeviceSynchronize();
    if (cudaStatus != cudaSuccess) {
        fprintf(stderr, "cudaDeviceSynchronize returned error code %d after launching addKernel!\n", cudaStatus);
        goto Error;
    }

    // Copy output vector from GPU buffer to host memory.
    cudaStatus = cudaMemcpy(output, dev_c, size * sizeof(int), cudaMemcpyDeviceToHost);
    if (cudaStatus != cudaSuccess) {
        fprintf(stderr, "cudaMemcpy failed!");
        goto Error;
    }

Error:
    cudaFree(dev_c);
    cudaFree(dev_a);
    cudaFree(dev_b);

    return cudaStatus;
}
