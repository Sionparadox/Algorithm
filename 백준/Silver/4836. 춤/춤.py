import sys

def validation(text):
    arr = text.split()
    steps = set(arr)
    res = []
    dips = []
    for i in range(len(arr)):
        if arr[i] == 'dip':
            flag = False
            if i>0 and arr[i-1] == 'jiggle':
                flag = True
                
            if i>1 and arr[i-2] == 'jiggle':
                flag = True
                
            if i<len(arr)-1 and arr[i+1] == 'twirl':
                flag = True
            
            if not flag:
                dips.append(i)
    if dips:
        res.append('1')
            
    if len(text)<15 or arr[-3:] != ['clap', 'stomp', 'clap']:
        res.append('2')
    
    if 'twirl' in steps and 'hop' not in steps:
        res.append('3')
    
    if arr[0] == 'jiggle':
        res.append('4')
    
    if 'dip' not in steps:
        res.append('5')
    
    return res, dips

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    arr = line.split()
    errors, dips = validation(line)
    if errors:
        text = line
        if dips:
            for i in dips:
                arr[i] = 'DIP'
            text = ' '.join(arr)
        
        if len(errors) == 1:
            output = f'form error {errors[0]}: {text}'
        else:
            err = ', '.join(errors[:-1])+' and '+errors[-1]
            output = f'form errors {err}: {text}'
    else:
        output = f'form ok: {line}'
        
    print(output)