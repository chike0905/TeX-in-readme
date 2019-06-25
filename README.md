# TeX-in-readme
Converter TeX to image URL (via codecogs.com) in Markdown for Github README.md.

## Motivation
In README.md on Github repository, we cannot write formulas in TeX format. We want to show the sample of game theory(application user's incentive and so on). 

## Environment
- Python 3.6.5

## How to use
1. You write README.md with formulas in TeX format.
    - Markup TeX part with `$`.
    - You cannot use space in formulas.
```
We get benefit $S-P$.
```

2. Convert your README.md by `tex2img.py`
    - Converted README.md is printed.
```
$ python tex2img.py README.md
 We get benefit <img src="https://latex.codecogs.com/gif.latex?S-P">.
```

3. In GitHub README, we can see formulas written in TeX like follows;
    - We get benefit <img src="https://latex.codecogs.com/gif.latex?S-P">.
