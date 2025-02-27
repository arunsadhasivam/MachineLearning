import torch
import numpy as np
import time

def test_performance(use_gpu=False):
    # Set device
    device = torch.device("cuda" if use_gpu and torch.cuda.is_available() else "cpu")
    print(f"Running on: {device}")
    
    # Create large matrices
    size = 5000
    matrix_a = torch.rand(size, size, device=device)
    matrix_b = torch.rand(size, size, device=device)
    
    # Measure matrix multiplication time
    start_time = time.time()
    result = torch.matmul(matrix_a, matrix_b)
    # Force computation to complete
    if use_gpu:
        torch.cuda.synchronize()
    elapsed = time.time() - start_time
    
    print(f"Matrix multiplication time: {elapsed:.4f} seconds")
    return elapsed

# Check if CUDA is available
if torch.cuda.is_available():
    print(f"GPU detected: {torch.cuda.get_device_name(0)}")
else:
    print("No GPU detected!")

# Run CPU test
print("\n--- CPU Test ---")
cpu_time = test_performance(use_gpu=False)

# Run GPU test if available
if torch.cuda.is_available():
    print("\n--- GPU Test ---")
    gpu_time = test_performance(use_gpu=True)
    
    # Show performance comparison
    speedup = cpu_time / gpu_time
    print(f"\nGPU is {speedup:.2f}x faster than CPU")
