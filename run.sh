#!/bin/bash

# List of transactions
transactions=("t1.py" "t2.py" "t3.py" "t4.py" "t5.py" "t6.py" "t7.py")

# Number of repetitions for each transaction
repetitions=2

# Measure start time
start_time=$(date +%s.%N)

# Function to run transactions
run_transactions() {
    for _ in $(seq $repetitions); do
        # Randomly shuffle the transactions
        shuffled_transactions=($(shuf -e "${transactions[@]}"))

        # Run each transaction
        for transaction in "${shuffled_transactions[@]}"; do
            python "$transaction" &
	    python "$transaction" &

	    # Wait for all transactions in this batch to finish
            wait
        done

        
    done
}

# Run transactions concurrently
parallel_processes=2
for _ in $(seq $parallel_processes); do
    run_transactions
done

# Measure end time
end_time=$(date +%s.%N)

# Calculate elapsed time
elapsed_time=$(echo "$end_time - $start_time" | bc)

# Calculate latency (time per transaction in milliseconds)
total_iterations=$((parallel_processes * repetitions * ${#transactions[@]}))
latency=$(echo "scale=4; $elapsed_time * 1000 / $total_iterations" | bc)

# Print results
echo "Transactions: ${transactions[@]}"
echo "Repetitions per Transaction: $repetitions"
echo "Parallel Processes: $parallel_processes"
echo "Total Iterations: $total_iterations"
echo "Elapsed Time: $elapsed_time seconds"
echo "Latency: $latency milliseconds per transaction"
