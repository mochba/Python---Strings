""""Write code using find() and string slicing to extract the number at the end
of the line below. Convert the extracted value to a floating point number and print 
it out."""

# ------using split()-----
# text = "X-DSPAM-Confidence:    0.8475"
# text = text.split()
# print(text)
# print(float(text[1]))
# ------using find() and slicing

text = "X-DSPAM-Confidence:    0.8475"
pos = text.find(' ')
print(pos)
value = text[pos:].lstrip()
print(float(value)+45)