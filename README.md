# YQuantum 2025: Superquantum Challenge

## Files

* Quantum hashing code: [`main.py`](https://github.com/mschubs/yquantum2025/blob/main/main.py) and [`nature.ipynb`](https://github.com/mschubs/yquantum2025/blob/main/nature.ipynb)
* Front-end app: [`app.py`](https://github.com/mschubs/yquantum2025/blob/main/app.py) and [`/public`](https://github.com/mschubs/yquantum2025/tree/main/public)
* Requirements: [`requirements.txt`](https://github.com/mschubs/yquantum2025/blob/main/requirements.txt)
* Report: [`writeup.pdf`](link)

## Get Started

```py
# Install requirements 
pip install -r requirements.txt
# Run app
python -m flask --app app run
# Run main.py
python main.py 'Quantum hashing!'
```

Output:
```
Hash of "Quantum hashing!":
  * Base 2: 0000000110000100011000000010101100001100101110011101100010110111111001010000101001101011010100011001010001100100100100101100001000011010101101101101000011110101111100010000101010100101010110100100001101111000110000101111000001010100000100100001001000100011
  * Base 10: 686200389401212040221455499146774065590495791561769778809310574733018927651
  * Base 16: 184602b0cb9d8b7e50a6b51946492c21ab6d0f5f10aa55a4378c2f054121223
```

## Demo

![demo](https://raw.githubusercontent.com/mschubs/yquantum2025/refs/heads/main/public/images/demo.png)

## Results

### Preservation of Entropy
Comparison of the input and output distributions:
<p align = "center">
   <img src="https://raw.githubusercontent.com/mschubs/yquantum2025/refs/heads/main/public/images/result-1.png" width = "50%" />
</p>

### Computation Time
<p align = "center">
   <img src="https://raw.githubusercontent.com/mschubs/yquantum2025/refs/heads/main/public/images/result-2.png" width = "50%" />
</p>

### Preimage Resistance
Measuring difference between the hashed output and the input message (bits converted to integers):
<p align = "center">
   <img src="https://raw.githubusercontent.com/mschubs/yquantum2025/refs/heads/main/public/images/result-3.png" width = "50%" />
</p>





