Tap Code Translation
Tap code is a way to communicate messages via a series of taps (or knocks) for each letter in the message. Letters are arranged in a 5x5 polybius square, with the letter "K" being moved to the space with "C".

   1  2  3  4  5
1  A  B C\K D  E
2  F  G  H  I  J
3  L  M  N  O  P
4  Q  R  S  T  U
5  V  W  X  Y  Z
Each letter is translated by tapping out the row and column number that the letter appears in, leaving a short pause in-between. If we use "." for each tap, and a single space to denote the pause:

text = "break"

"B" = (1, 2) = ". .."
"R" = (4, 2) = ".... .."
"E" = (1, 5) = ". ....."
"A" = (1, 1) = ". ."
"K" = (1, 3) = ". ..."
Another space is added between the groups of taps for each letter to give the final code:

"break" = ". .. .... .. . ..... . . . ..."
Write a function that returns the tap code if given a word, or returns the translated word (in lower case) if given the tap code. When translating from tap-code, default to the letter "c" if the tap-code ". ..." is found.

Examples
tap_code("break") ➞ ". .. .... .. . ..... . . . ..."

tap_code(".... ... ... ..... . ..... ... ... .... ....") ➞ "spent"

Notes
For more information on tap code, please see the resources section. The code was widely used in WW2 as a way for prisoners to communicate.

source --> https://edabit.com/challenge/EWZqYT4QGMYotfQTu