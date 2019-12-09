#!python
# Day1

# import pyperclip
import math

i,j = 0,0
sum = 0

def Fuel(k):
  global i,j,sum # Global all var
  j = math.trunc(k/3) - 2 # Use math.trunc to round down
  if j != 0 and j > 0:
    sum +=j # Sum counter to add all outputs after each run
    i = j
    return j
  else:
    return False

# To get all the numbers in a string, I used pyperclip module to paste the data in a variable.
# This way you can get the raw data and then split by '/r/n' to get the integers you need.

# inputs = pyperclip.paste()

inputs = '80228\r\n76027\r\n101696\r\n66033\r\n127249\r\n104564\r\n88957\r\n82536\r\n131331\r\n62571\r\n129935\r\n138764\r\n122011\r\n82908\r\n83358\r\n56584\r\n85483\r\n110398\r\n87103\r\n145728\r\n87305\r\n116387\r\n145243\r\n118656\r\n92624\r\n86152\r\n81056\r\n98776\r\n109949\r\n126863\r\n131046\r\n134570\r\n97818\r\n123881\r\n105902\r\n60102\r\n100226\r\n101041\r\n70950\r\n110903\r\n71779\r\n80531\r\n144679\r\n100346\r\n130079\r\n55606\r\n92984\r\n136022\r\n126633\r\n77104\r\n118037\r\n148426\r\n62327\r\n56250\r\n133496\r\n69308\r\n125495\r\n122131\r\n56864\r\n127532\r\n94194\r\n64268\r\n80166\r\n83250\r\n96506\r\n87668\r\n142137\r\n142915\r\n148287\r\n109471\r\n79349\r\n148270\r\n104627\r\n109657\r\n86225\r\n111411\r\n144666\r\n91402\r\n140834\r\n138587\r\n117809\r\n114288\r\n126467\r\n100089\r\n78745\r\n92180\r\n89969\r\n128868\r\n128085\r\n129931\r\n64047\r\n71968\r\n111512\r\n143771\r\n149658\r\n146102\r\n52655\r\n130193\r\n109013\r\n120465'
inputs = inputs.split('\r\n') # Split string into single number strings - Returns LIST
inputs = [int(i) for i in inputs] # List comprehension to convert each element of list from str to int

for i in inputs:
  while Fuel(i) > 3: #To stop execution so that the total sum is not affected
    if Fuel(i) == j: # If/else to stop if return is False and i != j
      Fuel(i)
    else:
      pass

print("The total sum is",sum)
