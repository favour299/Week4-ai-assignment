A list is a collection of items stored in order and can be accessed using its position (index).

Example

Python

phones=["Samsung", "iPhone", "Tecno", "Nokia"]

Here:

"Samsung" is index 0

"iPhone" is index 1

"Tecno" is index 2

You access items using the index:

Python

print(phones[0]) # Samsung

A dictionary stores data as key–value pairs. Instead of using positions, you access values using their keys.

Python

phone={
"brand": "Samsung",
"model": "A12",
"price": 15000
}
Here:

"brand" → key

"Samsung" → value

You access values using the key:

Python print(phone["brand"]) # Samsung

Simple way to remember

List = items in order
Dictionary = items with labels (keys).
