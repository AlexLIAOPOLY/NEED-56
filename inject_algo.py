import re

content = open('/Users/liaowang/Desktop/需求56/index.html', encoding='utf-8').read()
algo_js = open('/Users/liaowang/Desktop/需求56/algo_engine.js', encoding='utf-8').read()
scenario_js = open('/Users/liaowang/Desktop/需求56/scenario_engine.js', encoding='utf-8').read()

# Find old scenario engine block to replace
old_start_marker = '// Scenario engine'
old_end_marker = 'updateScenario();'

start = content.find(old_start_marker)
end = content.find(old_end_marker) + len(old_end_marker)

if start == -1:
    print('ERROR: Could not find old scenario engine start marker')
else:
    print(f'Replacing chars {start} to {end}')
    new_js = algo_js + '\n' + scenario_js
    content = content[:start] + new_js + content[end:]
    
    # Also add c-forecast canvas if missing (it's referenced in new code)
    if 'c-forecast' not in content:
        print('WARNING: c-forecast canvas not found in HTML')
    else:
        print('c-forecast canvas: OK')
    
    if 'c-algo-compare' not in content:
        print('WARNING: c-algo-compare canvas not found in HTML')
    else:
        print('c-algo-compare canvas: OK')
    
    open('/Users/liaowang/Desktop/需求56/index.html', 'w', encoding='utf-8').write(content)
    print(f'Done! lines: {content.count(chr(10))}, has </html>: {"</html>" in content}')
