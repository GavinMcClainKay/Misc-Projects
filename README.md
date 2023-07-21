# Misc Projects #
A ton of small personal projects, most of which are unfinished.

## Included Projects: ##
- [CUDA Vector Interface]()<sup> *Check me out!* </sup>
- [Taxbot-9000]()
- [Text-to-GPT]()
- [Valorant Stat Project]()<sup> *Check me out!* </sup>
- [Voice to Voice Translator]()<sup> *Check me out!* </sup>
- [Gap Learning Timer]()

## Descriptions: ##

### [CUDA Vector Interface]() ###
### <sup> The goal of this project was to learn a simple way to interact with my GPU for programming purposes. <sup/> ###
- The CUDA Vector Interface manages memory and distribution of single-dimensional vector-operation function pointers across all CUDA Cores in modern Nvidia Graphics cards.
> **An example of a single-dimensional vector-operation function:**

```c++
__global__ void addKernel(int* output_vector, const int* input_vectorA, const int* input_vectorB) {
    int i = threadIdx.x;
    output_vector[i] = input_vectorA[i] + input_vectorB[i];
    printf("%d + %d = %d\n", input_vectorA[i], input_vectorB[i], output_vector[i]);
}
```

> **...And it's pointer:**

```c++
KernalVectorOperation kvOPAdd = *addKernel;
```

> **...It's Parameters:**
 - *output_vector:*
   - A pointer to an empty vector allocated in the heap.
   - The output of the function passes into this vector.
 - *input_vector(A/B):*
   - Pointers to two vectors of the same size, on which the operation is performed.
   - (In this example the operation is vector addition.)
 - **NOTE:** All vector pointers passed must point to vectors of the same size.

> **How to use it:**
  - Simply pass your vectors and function pointer into:
    
 ```c++
//Manages memory and errors for any passed CUDA kernal vector operation function.
//@param	output		= pointer to an output integer or integer array.
//@param	int_a		= pointer to a constant integer array.
//@param	int_b		= pointer to a constant integer array.
//@param	size		= size of input arrays.
//@param	operation	= CUDA kernal vector operation to perform.
cudaError_t performVectorOperation(int* ouput, const int* in_a, const int* in_b, unsigned int size, KernalVectorOperation operation);
```
> **Dependencies:**
  - CUDA v12.2 libraries and compiler: [https://developer.nvidia.com/cuda-toolkit](https://developer.nvidia.com/cuda-toolkit)
