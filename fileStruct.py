import os, sys

lastArg = sys.argv[0]
userLimit = lastArg if isinstance(lastArg,int) else 0

def showFileStructure(curdir, lvl=0, prefix=''):
    try:
        if os.path.isdir(prefix+curdir):
            content = [(item,lvl) for item in list(os.listdir(prefix + curdir))]
            subfolds = [showFileStructure(fld[0], lvl+1, prefix=prefix+("\\" if prefix else "")+curdir+"\\") if '.' not in fld else (fld,lvl) for fld in content]

            return (curdir, subfolds, lvl)
        else:
            return (curdir,lvl)
    except (NotADirectoryError,PermissionError) as e:
        return (curdir, lvl)

folds = showFileStructure(os.getcwd())   
        
def printer(lst, limit=45):
    target = lst
    
    while target:
        if len(target) >= 3 and isinstance(target[0],str):
            print(" "*3*target[-1]+target[0]+("\\" if '.' not in target[0] else ''))
            target = target[1]
        elif len(target) >= 2 and isinstance(target[0],tuple):
            for tar in (target if limit==0 else target[:limit]):
                printer(tar)
            if limit > 0 and len(target)>limit: print("................")
            target = None
        elif len(target) == 2:
            print(" "*3*target[-1]+target[0]+("\\" if '.' not in target[0] else ''))
            target = None
        elif len(target) == 1:
            target = target[0]

    
print("\n################### File Structure ###################\n")            

if userLimit:
    printer(folds, userLimit)
else:
    printer(folds)

print("\n######################################################")

