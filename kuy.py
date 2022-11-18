from utils import *
from logic import *

kb_wumpus = PropKB()

# Deklarasi Fakta
P = {}  # Pit
B = {}  # Breeze
S = {}  # Stench
W = {}  # Wumpus
G = {}  # Gold

# Deklarasi Symbol
for i in range(1, 5):
    for j in range(1, 5):
        i_j = "[{},{}]".format(i, j)
        P[i, j] = Symbol("P" + i_j)
        B[i, j] = Symbol("B" + i_j)
        S[i, j] = Symbol("S" + i_j)
        W[i, j] = Symbol("W" + i_j)
        G[i, j] = Symbol("G" + i_j)

# 1
# Knowledge Base di 1, 1
kb_wumpus.tell(~P[1, 1])
kb_wumpus.tell(B[1, 1] | '<=>' | ((P[1, 2]) | P[2, 1]))
kb_wumpus.tell(B[1, 2] | '<=>' | ((P[1, 1]) | P[2, 2] | P[3, 1]))
kb_wumpus.tell(~B[1, 1])
kb_wumpus.tell(B[1, 2])

print("\nKotak (1,1)-----")
# Ada Pit di P[1,1] --> Salah
print("Ada Pit di 1,1? ", kb_wumpus.ask_if_true(P[1, 1]))
# Ada Pit di P[1,2] --> Salah
print("Ada Pit di 1,2? ", kb_wumpus.ask_if_true(P[1, 2]))
# Tidak ada Pit di P[1,2] dan P[2,1] --> Benar
print("Tidak Ada Pit di 1,2 dan 2,1? ", kb_wumpus.ask_if_true(~P[1, 2] & ~P[2, 1]))
# ada Pit di P[2,2] atau P[3,1] --> Benar
print("Ada Pit di 2,2 atau 3,1? ", kb_wumpus.ask_if_true(P[2, 2] | P[3, 1]))

kb_wumpus.retract(B[1, 2])
kb_wumpus.retract(~P[1, 1])
kb_wumpus.retract(~B[1, 1])

# 2
# Agent berjalan ke 1,2
# Knowledge Base di 1,2
kb_wumpus.tell(~P[1, 2])
kb_wumpus.tell(B[1, 2] | '<=>' | (P[2, 2] | P[1, 3]))
kb_wumpus.tell(S[1, 2] | '<=>' | (W[2, 2] | W[1, 3]))
kb_wumpus.tell(S[1, 2])

print("\nKotak (1,2)-----")
# Ada Breeze di B[1,2] --> Salah
print("Ada Breeze di 1,2? ", kb_wumpus.ask_if_true(B[1, 2]))
# Ada Stench di S[1,2] --> Benar
print("Ada Stench di 1,2? ", kb_wumpus.ask_if_true(S[1, 2]))

# 3
# Agent kembali ke 1,1
# Agent berjalan ke 2,1
# Knowledge base di 2,1
kb_wumpus.tell(B[2, 1] | '<=>' | (P[2, 2] | P[3, 1]))
kb_wumpus.tell(S[2, 1] | '<=>' | (W[2, 2] | W[3, 1]))
kb_wumpus.tell(~P[2, 2])
kb_wumpus.tell(B[2, 1])
kb_wumpus.tell(~S[2, 1])

print("\nKotak (2,1)-----")
# Ada Pit di P[3,1] --> Benar
print("Ada Pit di 3,1? ", kb_wumpus.ask_if_true(P[3, 1]))
# Ada Wumpus di W[2,2] --> Salah
print("Ada Wumpus di 2,2? ", kb_wumpus.ask_if_true(W[2, 2]))
# Ada Wumpus di W[1,3] --> Benar
print("Ada Wumpus di 1,3? ", kb_wumpus.ask_if_true(W[1, 3]))

# 4
# Agent berjalan ke 2,2
# Knowledge base di 2,2
kb_wumpus.tell(P[3, 1] | '<=>' | (B[3, 2] & B[4, 1]))
kb_wumpus.tell(W[1, 3] | '<=>' | (S[2, 3]) & S[1, 4])
kb_wumpus.tell(B[2, 2] | '<=>' | (P[2, 3] | P[3, 2]))
kb_wumpus.tell(~B[2, 2])

print("\nKotak (2,2)-----")
# Ada Pit di P[3,2] --> Salah
print("Ada Pit di 3,2? ", kb_wumpus.ask_if_true(P[3, 2]))
# Ada Breeze di B[3,2] --> Benar
print("Ada Breeze di 3,2? ", kb_wumpus.ask_if_true(B[3, 2]))

kb_wumpus.tell(B[3, 2] | '<=>' | (P[4, 2] | P[3, 3] | P[2, 2]))
kb_wumpus.tell(P[2, 2] | '<=>' | (B[1, 2] & B[2, 1] & B[3, 2] & B[2, 3]))

# Ada Pit di P[2,2] --> Salah
print("Ada Pit di 2,2? ", kb_wumpus.ask_if_true(P[2, 2]))

kb_wumpus.tell(~P[2, 2])

# 5
# Agent berjalan ke 2,2
# Knowledge base di 2,2
kb_wumpus.tell(B[2, 2] | '<=>' | (P[3, 2]))
kb_wumpus.tell(P[3, 2] | '<=>' | ~B[3, 2])
kb_wumpus.tell(W[1, 3] | '<=>' | (S[1, 2] & S[2, 3] & S[1, 4]))
kb_wumpus.tell(B[2, 2])

# Ada Pit di 3,3 --> Benar
print("Ada Pit di 3,3? ", kb_wumpus.ask_if_true(P[3, 3]))

# 6
# Agent berjalan ke 2,3
# Knowledge base di 2,3
kb_wumpus.tell((B[2, 3] & S[2, 3]) | '<=>' | (G[2, 3]))

print("\nKotak (2,3)-----")
# Ada Gold di 2,3 --> True
print("Ada Gold di 2,3? ", kb_wumpus.ask_if_true(G[2, 3]))

# Mission completed!
print("Mission Completed!")
