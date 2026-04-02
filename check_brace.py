content = open('/Users/liaowang/Desktop/需求56/index.html', encoding='utf-8').read()
script_start = content.find('<script>\nconst PAGE')
script_end = content.rfind('</script>')
script = content[script_start:script_end]
depth = 0
for i,c in enumerate(script):
    if c == '{':
        depth += 1
    elif c == '}':
        depth -= 1
        if depth < 0:
            print('Extra } at script pos:', i)
            print('Context:', repr(script[max(0,i-80):i+30]))
            depth = 0
print('Final depth:', depth)
