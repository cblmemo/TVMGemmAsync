with open('bin/temp.txt', 'r') as f:
    ls = f.readlines()
res = ''
for l in ls:
    res += l
    if l.startswith('def'):
        res += """    ConvModule = create_conv_module()
    sch = tir.Schedule(ConvModule)
    if cnt <= 0:
        return '=== start ===', sch
"""
        continue
    rawl = l.strip(' ').strip('\n')
    res += f"""    cnt -= 1
    if cnt <= 0:
        return '{rawl}', sch
"""
res += """    cnt -= 1
    if cnt <= 0:
        return '', sch
"""
with open('bin/temp_output.txt', 'w') as f:
    f.write(res)
