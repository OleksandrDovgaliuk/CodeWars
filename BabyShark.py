def baby_shark_lyrics():
    sharks = ['Baby shark', 'Mommy shark', 'Daddy shark', 'Grandma shark', 'Grandpa shark', 'Let\'s go hunt'] 
    output = ''
    for s in sharks:
        output += (s + ',' + ' doo'*6 + '\n')*3 + s + '!\n'
    return output + 'Run away,…'
