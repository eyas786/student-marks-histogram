
# Student Marks Histogram

A simple Python script that generates random marks for a list of students and visualizes the score distribution using a Matplotlib histogram.

## Features
* Generates 10 random student scores between 1 and 99 using NumPy.
* Groups marks into custom score ranges (`1-20`, `20-40`, `40-60`, `60-80`, `80-100`).
* Plots a clean histogram with red bin borders using Matplotlib.
* Automatically saves the generated chart locally as `student histogram.png`.
* Prints the exact array of generated marks to the console.

## Prerequisites
Make sure you have Python installed along with the required libraries:

```bash
pip install numpy matplotlib
```

## Usage
1. Clone this repository or download the script file.
2. Run the Python script from your terminal:

```bash
python main.py
```

3. View the generated chart window and check your folder for the saved `student histogram.png` file.

## Code Overview
```python
import numpy as np
import matplotlib.pyplot as plt

name = ["khaqan", "eyas", "bacha", "salman", "babar", "saim", "sunny", "shayan", "abdullah", "asad"]
marks = np.random.randint(1, 100, 10)

plt.hist(marks, bins=[1, 20, 40, 60, 80, 100], edgecolor="red")
plt.title("student data")
plt.xlabel("range")
plt.ylabel("count")
plt.savefig("student histogram.png")
plt.show()

print(marks)
```
