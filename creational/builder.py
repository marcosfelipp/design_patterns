class Form():
	
	def __init__(self):
		self.name		= None
		self.age 		= None
		self.address 	= None
		self.identity 	= None
		self.phone 		= None

class FormBuilder():
	
	def __init__(self):
		self.form = Form()

	def set_name(self, name):
		self.form.name = name
		return self

	def set_age(self, age):
		self.form.age = age
		return self

	def set_address(self, address):
		self.form.address = address
		return self

	def set_identity_card(self, id_number):
		self.form.identity = id_number
		return self

	def set_phone(self, phone):
		self.form.phone = phone
		return self

	def build(self):
		return self.form 


class CreateForm():
	
	def __init__(self):
		form = self.set_data()
		self.print_data(form)

	def set_data(self):
		form_builder = FormBuilder()
		return form_builder.set_name('Heisenberg B. B').set_phone('3228863').build()

	def print_data(self, form):
		print(form.name)
		print(form.phone)

if __name__ == "__main__":
	CreateForm()