#!/bin/bash

# Set the number of iterations
iterations=10
progress_interval=10

# Measure start time
start_time=$(date +%s.%N)

# Loop for the specified number of iterations
for ((i=1; i<=$iterations; i++))
do
    python t1.py
    python t2.py
    python t3.py
    python t4.py
    python t5.py
    python t6.py
    python t7.py

    # Display progress every 1000 iterations
    if [ $((i % progress_interval)) -eq 0 ]; then
        echo "Progress: $i / $iterations iterations"
    fi
done

# Measure end time
end_time=$(date +%s.%N)

# Calculate elapsed time
elapsed_time=$(echo "$end_time - $start_time" | bc)

# Calculate throughput (transactions per second)
throughput=$(echo "scale=2; $iterations / $elapsed_time" | bc)

# Calculate latency (time per transaction in milliseconds)
latency=$(echo "scale=4; $elapsed_time * 1000 / $iterations" | bc)

# Print results
echo "Iterations: $iterations"
echo "Elapsed Time: $elapsed_time seconds"
echo "Throughput: $throughput transactions per second"
echo "Latency: $latency milliseconds per transaction"
