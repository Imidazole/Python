def get_info(name, surname, birth_year, city_of_residence, email, phone_number):
	res = "Имя: {0} Фамилия: {1} Год рождения: {2} Город проживания: {3} e-mail: {4} Телефон: {5}"\
			.format(
				name,
				surname,
				birth_year,
				city_of_residence,
				email,
				phone_number
			)
	return res


nm = input("Введите имя:\n")
snm = input("Введите фамилию:\n")
by = input("Введите год рождения:\n")
cr = input("Введите город проживания:\n")
em = input("Введите e-mail:\n")
pn = input("Введите номер телефона:\n")

r = get_info(surname = snm, name = nm, birth_year = by, city_of_residence = cr, email = em, phone_number = pn)

print(r)
