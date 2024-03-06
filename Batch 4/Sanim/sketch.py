from sketchpy import library as lib

print("Available sketches:\n 1. RDJ\n 2. Tom Holland\n 3. Gojo\n 4. Ironman")

picture = int(input('Enter sketch number: '))

if picture == 1:
    sketch = lib.rdj()
elif picture == 2:
    sketch = lib.ironman_ascii()
elif picture == 3:
    sketch = lib.gojo()
elif picture == 4:
    sketch = lib.tom_holland()
else:
    print('Invalid choice')
    exit()  
sketch.draw()
