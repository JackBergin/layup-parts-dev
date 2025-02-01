import logging
import time  # Add this import at the top with the other imports

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('sequence_log.txt', mode='w'),
        logging.StreamHandler()  # This will still print to console
    ]
)

def layup_sequence_iterative(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    s1, s2 = 1, 2  # Base cases: S(1) = 1, S(2) = 2

    for i in range(3, n + 1):
        if i % 2 == 0: # even
            s_next = s2 + s1
        else: # odd
            s_next = 2 * s2 - s1
        s1, s2 = s2, s_next  # Shift values for next iteration
    return s2

def test_layup_sequence():
    logging.info("Starting test...")

    # Base cases
    assert layup_sequence_iterative(1) == 1, "S(1) should be 1"
    logging.debug(f"S(1) = {layup_sequence_iterative(1)}")
    
    assert layup_sequence_iterative(2) == 2, "S(2) should be 2"
    logging.debug(f"S(2) = {layup_sequence_iterative(2)}")
    
    # Test case for n=4: S(4-1) + S(4-2) = S(3) + S(2) = 3+2 = 5
    assert layup_sequence_iterative(4) == 5, "S(4) should be 5"
    logging.debug(f"S(4) = {layup_sequence_iterative(4)}")
    
    # Test case for n=5: 2*S(5-1) - S(5-2) = 2*S(4) - S(3) = 2*5 - 3 = 7
    assert layup_sequence_iterative(5) == 7, "S(5) should be 7"
    logging.debug(f"S(5) = {layup_sequence_iterative(5)}")
    
    # Test case for n=6: S(6-1) + S(6-2) = S(5) + S(4) = 7+5 = 12
    assert layup_sequence_iterative(6) == 12, "S(6) should be 12"
    logging.debug(f"S(6) = {layup_sequence_iterative(6)}")
    
    logging.info("All tests passed!")

def main():
    test_layup_sequence()
    
    # Compute S(10,000)
    start_time = time.time()
    result = layup_sequence_iterative(10000)
    end_time = time.time()
    execution_time = end_time - start_time
    logging.info(f"S(10000) = {result}")
    logging.info(f"Calculation time: {execution_time:.4f} seconds")

if __name__ == "__main__":
    main()
