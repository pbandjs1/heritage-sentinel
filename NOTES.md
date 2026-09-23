### Modularity Check

Output with first toy problem:

```
Restoration plan: ['stabilize_base', 'seal_crack', 'clean_surface', 'restore_pigment']
```
Output with second toy problem:

```
Restoration plan: ['just_look_at_it', 'focus', 'use_telekinesis_to_repair', 'scotch_tape', 'flex_tape']
```

#### Reflection:
 - Currently, everything is modular, and we get successful returns no matter the input/problem file.
-- even with multiple prerequisites.
 - The only issue right now is that creating a whole new file (like restoration_graph_2) is messy, and action files 
should probably be separated out to some other folder we can reference, and then bring in with functions. But,
for now, I just chose to be lazy
