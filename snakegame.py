
langauages = ['java','c','c++','python','javascript']

for language in langauages [2:4]:
    if language != 'python':
        print(f'Are you sure you want to program in {language.title()}?')
    else:
        print(f'choose{language.upper()} instead')    
