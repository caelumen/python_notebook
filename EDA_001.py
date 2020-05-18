

# %%

strFile = 'nagios_dataset.log'
rawData = [x.rstrip() for x in open(strFile)]
len(rawData)



# %%


# %%
def head(n):
      val = [ x for idx,x in enumerate(rawData) if idx < n ]
  for idx,x in enumerate(val):
    print(" {} - {}".format(idx,x) )

head(10)


# %%



# %%
import time
start = time.time()
arrayData = [x.split(":") for x in rawData[2:] ]
print("- duration : {}".format(time.time()-start) )


# %%

# %%






#%%









