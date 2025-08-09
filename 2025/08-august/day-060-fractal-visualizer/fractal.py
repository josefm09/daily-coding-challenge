from PIL import Image
import io

def generate_mandelbrot(width, height, max_iter):
    """Generates a Mandelbrot set image."""
    img = Image.new('RGB', (width, height), 'black')
    pixels = img.load()

    for x in range(width):
        for y in range(height):
            zx, zy = x * (3.5 / width) - 2.5, y * (2.0 / height) - 1.0
            c = zx + zy * 1j
            z = c
            for i in range(max_iter):
                if abs(z) > 2.0:
                    break
                z = z * z + c

            # Color the pixel based on the number of iterations
            color = (i % 8 * 32, i % 16 * 16, i % 32 * 8)
            pixels[x, y] = color

    return img

def get_mandelbrot_image(width=800, height=600, max_iter=256):
    """Returns the Mandelbrot set as a PNG image in memory."""
    img = generate_mandelbrot(width, height, max_iter)

    # Save the image to a memory buffer
    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)

    return buf
