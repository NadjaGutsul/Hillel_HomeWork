a, b, c = int(input()),int(input()),int(input())
def temp(a,b,c):
    celsius=[c for c in range(a,b,c)]
    fahrenheit=[f*(9/5)+32 for f in range(a,b,c)]
    assert(len(celsius)==len(fahrenheit))
    for i in range(len(celsius)):
        print(f'{celsius[i]} °C corresponds to {fahrenheit[i]} °F')
temp(a,b,c)
