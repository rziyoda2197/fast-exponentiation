def modul_bo'yicha_daraja(a, n, mod):
    if n == 0:
        return 1
    if n % 2 == 0:
        return modul_bo'yicha_daraja((a * a) % mod, n // 2, mod)
    else:
        return (a * modul_bo'yicha_daraja((a * a) % mod, n // 2, mod)) % mod
```

```python
def modul_bo'yicha_daraja_optimallashtirilgan(a, n, mod):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = (result * a) % mod
        a = (a * a) % mod
        n //= 2
    return result
```

```python
def modul_bo'yicha_daraja_binar_search(a, n, mod):
    result = 1
    while n > 0:
        if n % 2 == 1:
            result = (result * a) % mod
        a = (a * a) % mod
        n = n // 2
    return result
