from PIL import Image


def main():
    with Image.open("grayson.jpg") as im:
        im_bytes = im.tobytes()  # Convert image to raw bytes
        message = "hello"
        new_im_bytes = encode_im(im_bytes, message) 
        new_im = Image.frombytes('RGB', im.size, new_im_bytes)  # Make a new image
        new_im.show()  # Let's see what we did!


#Return one bit at a time from a bytes or bytearray
def iter_bits(inbytes):
    for b in inbytes:
        for i in range(8):
            yield b >> (7-i) & 1

def encode_im(image, message):
    bits = list(iter_bits(image))
    bits[7:len(message) * 8:8] = message
    return bits_to_ints(bits)

def bits_to_ints(bits):
    return bytearray([int("".join(str(x) for x in bits[i:i + 8]), 2) for i in range(0, len(bits), 8)])

def make_im():
    message = iter_bits(bytearray("hello", encoding='utf-8'))
    with Image.open("grayson.jpg") as im:
        im_bytes = im.tobytes()  
        new_im_bytes = encode_im(im_bytes, list(message))
        return Image.frombytes('RGB', im.size, new_im_bytes)  


if __name__ == '__main__':
    main()