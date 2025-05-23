student_data = {'id1':
                {'name':['Suhana'], 'class':['5'], 'subject': ['maths, physics, arts/design'],},
                
                'id2':
                {'name': ['Zarif'], 'class': [5], 'subject': ['law, politcal science, philosophy']},
                
                 'id3':
                 {'name': ['Suhana'],'class': ['5'], 'subject': ['maths, physics, arts/design']},

                 'id4':
                 {'name': ['Zafira'], 'class': [5], 'subject': ['mathematics, physics, english']}
}
result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)