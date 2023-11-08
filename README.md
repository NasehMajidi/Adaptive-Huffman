# Adaptive-Huffman
Huffman coding necessitates an understanding of the original sequence's probabilities. If this information isn't accessible, Huffman coding becomes a two-pass method, with the first pass collecting statistics and the second one encoding the source. Adaptive Huffman coding (also known as Dynamic Huffman coding) is a Huffman-based adaptive coding technique. It allows for one-pass encoding and adaptability to changing conditions in data as the symbols are being conveyed, with no prior knowledge of the source distribution. The advantage of a one-pass technique is that the source can be encoded in real-time, though it becomes more susceptible to transmission faults, as even a single loss might corrupt the entire code. 


**Keywords**: Information Theory; Huffman Coding; Lossless Compression<br>**Course**: Data Compression<br>**Programming Language**: Python
