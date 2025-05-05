""""
Leetcode 271: Encode and Decode Strings

Problem Description:
Design an algorithm to encode a list of strings to a single string. The encoded string should be decodable back to the original list of strings.

Approach:
1. **Encoding**:
   - Iterate through the list of strings.
   - For each string, append its length followed by a special delimiter (e.g., `#`) and the string itself.
   - This ensures that even strings with `#` inside them can be safely encoded.
2. **Decoding**:
   - Iterate through the encoded string.
   - Extract the length of each string, then use slicing to extract the string based on that length.
3. **Efficiency**: Both encoding and decoding operations run in **O(n)** time complexity, where `n` is the total length of all strings.
"""

class Codec:
    def encode(self, strs):
        """
        Encodes a list of strings to a single string.
        :type strs: List[str]
        :rtype: str
        """
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + '#' + s
        return encoded_str

    def decode(self, s):
        """
        Decodes a single string to a list of strings.
        :type s: str
        :rtype: List[str]
        """
        decoded_strs = []
        i = 0
        while i < len(s):
            # Find the delimiter '#'
            j = s.find('#', i)
            length = int(s[i:j])  # Extract length
            i = j + 1  # Move past '#'
            decoded_strs.append(s[i:i + length])  # Extract the string
            i += length  # Move to the next encoded string
        return decoded_strs

# Example usage
codec = Codec()
encoded = codec.encode(["hello", "world"])
print("Encoded:", encoded)

decoded = codec.decode(encoded)
print("Decoded:", decoded)


