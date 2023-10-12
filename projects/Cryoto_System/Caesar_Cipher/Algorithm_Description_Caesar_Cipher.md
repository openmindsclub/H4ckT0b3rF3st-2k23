# CESAR

In cryptography, the shift cipher, also known as Caesar's cipher or Caesar's code (see different names), is a very simple encryption method used by Julius Caesar in his secret correspondence.

The ciphertext is obtained by replacing each letter of the original plaintext with a letter at a fixed distance, always on the same side, in the order of the alphabet. For the last letters (in the case of a shift to the right), we start from the beginning ( modulo % ).

# Example

Encryption can be represented by the superposition of two alphabets, the plain alphabet presented in the normal order and the encrypted alphabet shifted, to the left or to the right, by the desired number of letters. Below is an example of encoding 3 letters to the right. The offset parameter (here 3) is the encryption key:

    clear:     ABCDEFGHIJKLMNOPQRSTUVWXYZ .

    encrypted: DEFGHIJKLMNOPQRSTUVWXYZABC .

To encode a message, just look at each letter of the plain message, and write the corresponding encoded letter. To decipher, we simply do the opposite.

    Encryption :E(x) = (x+n) % [26]
    Decryption :D(x) = (x-n) % [26]

