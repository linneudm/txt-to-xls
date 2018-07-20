import xlsxwriter

file_path = ""
workbook = xlsxwriter.Workbook('contatos.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A', 40)
worksheet.set_column('B:B', 20)
bold = workbook.add_format({'bold': True})

worksheet.write('A1', 'Nome', bold)
worksheet.write('B1', 'Contato', bold)

file = open("c-tb.txt", "r")
text = file.read()
bar = 0
name_list = []
name = ""
contact_list = []
contact = ""
add_name = True
add_contact = True
for i,t in enumerate(text):
	if(text[i]== ' ' and (text[i+1] == ' ' or text[i+1]=='|')):
		if(bar == 1 and add_name):
			name_list.append(name)
			add_name = False
		elif(bar == 2 and add_contact):
			contact_list.append(contact)
			add_contact = False
	if(t=='\n'):
		name = ""
		contact = ""
		bar = 0
		add_name=True
		add_contact = True
	elif(t=='|'):
		bar += 1
	#Verifica se é o indice
	elif(bar == 0 and t.isdigit()):
		pass
	elif(bar == 1):
		name += t
	elif(bar == 2):
		contact += t

for i, nome in enumerate(name_list):
	row = i+1
	worksheet.write(row,0, nome)

for i, contato in enumerate(contact_list):
	row = i+1
	contato = "+55 " + contato
	if (contato == "Null"):
		contato = "000"
	worksheet.write(row,1, contato)

workbook.close()
