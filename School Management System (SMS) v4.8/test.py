import ascii_magic
print()
output=ascii_magic.from_image_file("images.jpg",columns=100,char='@')
ascii_magic.to_terminal(output)
print()
output=ascii_magic.from_image_file("images (1).jpg",columns=130,char='@')
ascii_magic.to_terminal(output)
print()