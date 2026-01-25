chai_type = "Ginger Tea"
customer_name = "Ahmad Zia"

print(f"Order for {customer_name} : {chai_type} Please!!")

chai_description = "Aromatic and Strong"

print(f"Id before : {id(chai_description)}")

# chai_description[0] = 'B' //Error because string is immutable
chai_description = "Ahmad at Selection Marks"
print(f"Id after : {id(chai_description)}")

print(f"First word of Chai description : {chai_description[0:8]}") #gives chars from 0th index to  (8-1 = 7th index).
print(f"First word of Chai description : {chai_description[0:8:1]}") #gives 8 characters from 0th index to 7th index. 1 after second : means give each character without skipping any character.
print(f"First word of Chai description : {chai_description[0:8:2]}") #gives characters from 0th index to 7th index. 2 after second : means skip every 2nd character starting from 0th index uptil 8-1 = 7th index.
print(f"First word of Chai description : {chai_description[:8:2]}") #give all characters before and including 8-1 = 7th index. 2 after second : means skip every 2nd character starting from 0th index uptil 8-1 = 7th index.NOTE:Cant skip starting colon.
print(f"First word of Chai description : {chai_description[3::2]}") #give all characters starting from 3rd index uptil end of string. 2 after second : means skip every 2nd character starting from 0th index uptil 8-1 = 7th index.
print(f"First word of Chai description : {chai_description[::-1]}") #gives each character from back of the string. Basically reverses the string.
print(f"First word of Chai description : {chai_description[8:1:-1]}") #gives characters from back of the string starting from index 8 going backwards to index 1 + 1.(last index is not included)


label_text = "Chai Spécial"
encoded_label = label_text.encode("utf-8") #encoding actually ensures that proper meaning is conveyed through string.
print(f"Non Encoded Label : {label_text}")
print(f"Encoded Label : {encoded_label}")

decoded_label = encoded_label.decode("utf-8")
print(f"Decoded Label : {decoded_label}")