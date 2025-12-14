#Practice with dictionaries
A = {"Ιταμός": "Προκλητικός,Αυθάδης,Αναιδής",
     "Όνειδος": "Ντροπή,Καταισχύνη",
     "Πομφόλυγες": "Αερολογίες,Ανοησίες"}
print(A)
A["Φληναφήματα"] = "Ανοησίες,Σαχλαμάρες"
print(A)
input_key = input("Δώσε ένα Key")
input_value = input("Δώσε ένα value")
A[input_key] = input_value
print(A)
