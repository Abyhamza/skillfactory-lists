last_names = {
  "john": "johnson",
  "tom": "zimmerman",
  "tim": "goldman",
  "jane": "jones",
  "jack": "jackson",
  "joseph": "josephson",
  "maria": "van der merwe",
  "kate": "fredrickson",
  "phillip": "phillips",
  "jody": "jodyson",
  "arthur": "arthurson"
}
ages = [('john', 25), ('tom', 30), ('tim', 1), ('jane', 5), ('jack', 45), ('joseph', 60), ('maria', 8), ('kate', 12), ('phillip', 17), ('jody', 18), ('arthur', 73)]


def nameAges(last_names, ages):
  for i in ages:
    if i[1] >= 18:
      print(i[0], last_names[i[0]], i[1])

nameAges(last_names, ages)



