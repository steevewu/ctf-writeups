from sage.all import *
import ast
import os, sys
sys.path.append(os.path.dirname(__file__))


def mod_inv(inp):
    res = []
    for n in inp:
        fs = list(factor(n))
        fs = [(p ** (e - 1) * (p - 1)) for p, e in fs]
        res += [prod(fs)]
    return [pow(0x10001, -1, phi) for phi in res]


def reverse_char(char):
    if char == "e":
        return "_"
    if char.isupper():
        return chr(155 - ord(char))
    elif char.islower():
        return chr(219 - ord(char))


def googly(number, position):
    mask = 1 << position
    return number ^ mask


file = open(os.path.dirname(__file__) + '/out.txt', 'r')

cipher, cs, ns = file.read().strip().split("\n")

cs = ast.literal_eval(cs)
ns = ast.literal_eval(ns)

lang = {
    'A': 'Α', 'a': 'α',
    'B': 'Β', 'b': 'β',
    'C': 'Σ', 'c': 'σ',
    'D': 'Δ', 'd': 'δ',
    'E': 'Ε', 'e': 'ε',
    'F': 'Φ', 'f': 'φ',
    'G': 'Γ', 'g': 'γ',
    'H': 'Η', 'h': 'η',
    'I': 'Ι', 'i': 'ι',
    'J': 'Ξ', 'j': 'ξ',
    'K': 'Κ', 'k': 'κ',
    'L': 'Λ', 'l': 'λ',
    'M': 'Μ', 'm': 'μ',
    'N': 'Ν', 'n': 'ν',
    'O': 'Ο', 'o': 'ο',
    'P': 'Π', 'p': 'π',
    'Q': 'Θ', 'q': 'θ',
    'R': 'Ρ', 'r': 'ρ',
    'S': 'Σ', 's': 'ς',  
    'T': 'Τ', 't': 'τ',
    'U': 'Υ', 'u': 'υ',
    'V': 'Ω', 'v': 'ω',
    'W': 'Ψ', 'w': 'ψ',
    'X': 'Χ', 'x': 'χ',
    'Y': 'Υ', 'y': 'υ',
    'Z': 'Ζ', 'z': 'ζ'
}
language = {v: k for k, v in lang.items()}


pt = []

ds = mod_inv(ns)

for i, ch in enumerate(cipher):
    if ch.isascii():
        pt += [reverse_char(ch)]
        continue
    eng = language.get(ch)
    c = googly(cs[i], cs[i].bit_length() - ord(eng))
    pt += [chr(pow(c, ds[i], ns[i]))]


print("".join(pt))