# RWay Tries
For every character (256 bits) at a level create nodes
at the last char of the key set the value

## Problem
For unicode character 65546 the huge amount of space will be empty.

# Ternary Search Tries
- Store the characters and values in nodes not keys
- Each node has 3 children;
    - smaller (left)
    - equal (middle)
    - larger (right)
## Algorithm
Follow the links corresponding to each character
- If less, take left link; if greater, take right link
- if equal, take middle line and move to next charater.

**Search Hit**: Node where search ends has a nin-null value
**Search Miss**: Reach a null link or node where search ends has null value