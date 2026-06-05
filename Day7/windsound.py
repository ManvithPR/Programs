C = 262
D = 294
E = 330
F = 349
G = 392
A = 440
B = 494
C2 = 523

#Opening notes of Jana Gana Mana
song = [
    (G, 500),
    (A, 500),
    (B, 500),
    (C2, 1000),   # Jana

    (C2, 500),
    (B, 500),
    (A, 500),
    (G, 1000),    # Gana

    (G, 500),
    (A, 500),
    (B, 500),
    (C2, 1000),   # Mana

    (B, 500),
    (A, 500),
    (G, 1000)     # Adhinayaka
]

for note, duration in song:
    winsound.Beep(note, duration)
    time.sleep(0.05)

print("Jana Gana Mana tune played!")