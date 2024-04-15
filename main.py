from PIL import Image


def main():
    with Image.open("grayson.jpg") as im:
        im_bytes = im.tobytes()  # Convert image to raw bytes

        print(len(im_bytes)/3)  # Length of im_bytes should be divisible by 3.

        new_im_bytes = bytearray(len(im_bytes))  # Make a byte array to store my modified data
        for i, b in enumerate(im_bytes):
            new_im_bytes[i] = b ^ 0b10010110

        new_im = Image.frombytes('RGB', im.size, new_im_bytes)  # Make a new image
        new_im.show()  # Let's see what we did!

        for bit in iter_bits(bytes([0b00001111,0b11110000])):
            print(bit)

#Return one bit at a time from a bytes or bytearray
def iter_bits(inbytes):
    for b in inbytes:
        for i in range(8):
            yield b >> (7-i) & 1


if __name__ == '__main__':
    main()