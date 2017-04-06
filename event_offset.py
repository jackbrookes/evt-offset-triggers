import pandas as pd
from tkinter.filedialog import askopenfilename

# offset in us (microseconds)
offset_amount_t = 200000
offset_amount_e = 500

# read file
event_fname = askopenfilename(title="Select .evt file")
event_data = pd.read_csv(event_fname, sep='\t')

# offset
event_data['Tmu         '] += offset_amount_t
event_data['TriNo'] += offset_amount_e

# resave
new_fname = event_fname[:-4] + "_offset" + event_fname[-4:]
event_data.to_csv(new_fname, sep='\t', index=False)

# done
print("New file saved at {}".format(new_fname))
