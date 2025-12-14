#Dictionary and comprehension
merchandise = {"50 αποχρώσεων του γκρι": 10.18,
               "Ματσάκια μαϊντανού": 0.22,
               "Επισκευαστικό τσιμέντο": 5.17,
               "CD της Billie Eilish": 0.05,}
rate=float(input("Αξιολόγησε τον πελάτη"))

new_merchandise={key:merchandise[key]*(rate+1) for key in merchandise.keys() }
print(new_merchandise)