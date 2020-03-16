def parseMethodInfo(method_info):
	script = ""

	m_info = method_info.split(' ')

	ret_type = m_info[1]
	method_name = m_info[2]
	method_offset = m_info[len(m_info)-1]
	

	# print(ret_type)

	index = method_name.find('(')
	method_name = method_name[0:index]
	
	# print(method_name)
	# print(method_offset)


	arg_count = 0

	for i in range(3, len(m_info)):
		if(m_info[i] == '{') :
			# print('FIND!!!')

			break

		arg_count = arg_count + 1

	arg_count = (arg_count+1) / 2

	# print(arg_count)


	# print("#######################")

	script += "// " + method_info + "\n\n"
	script += "var offset = " + method_offset + ";\n"
	script += "var " + method_name + " = il2cpp.add(offset);\n\n"
	script += "Interceptor.attach(" + method_name + ",\n"
	script += "{\n"
	script += "    onEnter: function(args)\n"
	script += "    {\n"
	script += '        console.log("[+] ' + method_name + ' Hook onEnter()");\n'

	for c in range(0, arg_count+1):
		script += '        console.log("    args[' + str(c) + '] : " + args[' + str(c) + ']);\n'
	
	script += "    },\n"
	script += "    onLeave: function(retVal)\n"
	script += "    {\n"

	if(ret_type != 'void'):
		script += '        console.log("    retVal : " + retVal);\n'
	script += '        console.log("");\n'
	script += "    }\n"
	script += "});\n\n\n\n"

	print(script)

	return script




f_method_symbols = open("methodSymbol.txt", 'r')
f_script_output = open("scriptOutput.txt", 'w')

count = 1


while True :
	method_info = f_method_symbols.readline()[:-1]
	
	if not method_info : break

	print("[" + str(count) + "] " + method_info + "\n\n\n")
	script = parseMethodInfo(method_info)

	f_script_output.write(script)

	count = count + 1


f_method_symbols.close()
f_script_output.close()

