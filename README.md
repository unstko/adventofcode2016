# adventofcode2016
My solutions for [adventofcode.com (2016)](http://adventofcode.com/2016) with Python.

## My base classes
### Solution
- Solution for a day can calculate part 1 and 2
- Input is loaded from file `input.txt` inside the folder of the day
- Solutions of a day have to define their own calculate method

### Test
- Sets up and tears down calculation of a solution for a day
- Mocks the input from the `input.txt` by an input string

## My modules
### Point2D
- 2D point inside cartesian coordinate system
- Set and get x and y coordinates
- Add, sub and neg points
- Calc euclidean and manhattan distances between points
- Print point coordinates

### Map
- Map based on Image class ([Pillow](http://python-pillow.org))
- Set and get values for 2D points
- Get minimum and maximum coordinates of set points
- Show map image
- Image output gets flipped depend on coordinate origin

### Keypad
- Standard is 9-button keypad
- Load custom keypad from JSON file
- Move finger in direction
- Press button and append code

### Triangle
- Set and get side lengths
- Check if triangle is possible

### Dict
- Sortable dictionary
- Get sorted strings with arbitrary length

## My solutions
| Day | Task | Python modules | My modules |
| --- | ---- | -------------- | ---------- |
| 01 | Find shortest path and cross point | copy, math, PIL | Point2D, Map |
| 02 | Find codes at keypads | os, json | Keypad |
| 03 | Check triangles | re | Triangle |
| 04 | Encrypt and check room names | re, collections, operator | Dict |
| 05 | Create password from MD5 hashes | hashlib | - |
