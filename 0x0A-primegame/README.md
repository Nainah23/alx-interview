### Problem Breakdown

1. **Game Rules**:
   - Maria and Ben take turns choosing prime numbers from a set of consecutive integers starting from 1 up to and including `n`.
   - After a prime is chosen, that number and all its multiples are removed from the set.
   - The player who cannot make a move loses the game.

2. **Objective**:
   - Determine the winner of each game given multiple rounds, where `n` may differ in each round.
   - Identify who won the most rounds after all rounds are played.

3. **Constraints**:
   - You can't use any external libraries.
   - `n` and `x` will not be larger than 10,000.

### Approach

1. **Prime Number Computation**:
   - Use the Sieve of Eratosthenes to compute all prime numbers up to the maximum possible value of `n` (which is 10,000).

2. **Game Simulation**:
   - For each round:
     - Initialize the set of numbers from 1 to `n`.
     - Simulate the game by removing primes and their multiples in turns.
     - Track who wins the round based on the availability of prime numbers to choose.

3. **Determine Winner**:
   - Count the wins for Maria and Ben.
   - Return the name of the player who won the most rounds.

### Implementation

Here is the implementation in Python:

```python
def sieve(n):
    """ Return a list of primes up to n, using the Sieve of Eratosthenes. """
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if (is_prime[p] == True):
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]

def isWinner(x, nums):
    if x == 0 or not nums:
        return None
    
    max_n = max(nums)
    primes = sieve(max_n)
    
    def play_game(n):
        """ Determine the winner for a given n """
        numbers = set(range(1, n + 1))
        turn = 0  # 0 for Maria, 1 for Ben
        
        while True:
            prime_found = False
            for p in primes:
                if p > n:
                    break
                if p in numbers:
                    prime_found = True
                    for multiple in range(p, n + 1, p):
                        if multiple in numbers:
                            numbers.remove(multiple)
                    turn = 1 - turn  # Switch turn
                    break
            
            if not prime_found:
                return 'Ben' if turn == 0 else 'Maria'
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        winner = play_game(n)
        if winner == 'Maria':
            maria_wins += 1
        elif winner == 'Ben':
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
```

### Explanation

1. **Sieve Function**:
   - Computes all prime numbers up to the largest `n` in the `nums` list.

2. **Game Simulation**:
   - For each round, simulate the game by iterating through the primes and removing them and their multiples until no more moves are possible.

3. **Result Calculation**:
   - Count the wins for Maria and Ben and determine the player with the most wins.
