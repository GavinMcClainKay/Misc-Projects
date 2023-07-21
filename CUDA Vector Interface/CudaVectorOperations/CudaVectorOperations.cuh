//Gavin Kay 2023
//Basic interface to easily create custom vector operations that leverage the CUDA Cores in NVIDIA Graphics Cards.
#pragma once
#include "cuda_runtime.h"
#include "device_launch_parameters.h"
//A kernal vector operation is a function pointer to a CUDA kernal.
//@param	output	= pointer to an output integer or integer array.
//@param	in_a	= pointer to a constant integer array.
//@param	in_b	= pointer to a constant integer array.
typedef void (*KernalVectorOperation) (int* output, const int* in_a, const int* in_b);

//Manages memory and errors for any passed CUDA kernal vector operation function.
//@param	output		= pointer to an output integer or integer array.
//@param	int_a		= pointer to a constant integer array.
//@param	int_b		= pointer to a constant integer array.
//@param	size		= size of input arrays.
//@param	operation	= CUDA kernal vector operation to perform.
cudaError_t performVectorOperation(int* ouput, const int* in_a, const int* in_b, unsigned int size, KernalVectorOperation operation);