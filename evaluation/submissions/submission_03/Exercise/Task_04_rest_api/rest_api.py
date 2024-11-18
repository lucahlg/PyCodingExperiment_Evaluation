class RestAPI:
    def __init__(self, database=None):
        # Wenn keine Datenbank übergeben wird, eine leere Benutzer-Datenbank initialisieren
        self.database = database if database is not None else {}

    def get(self, url, payload=None):
        # Verarbeite die GET-Anfrage je nach URL
        if url == "/users":
            if payload:
                users_to_fetch = payload.get('users', [])
                result = {user: self.database[user] for user in users_to_fetch if user in self.database}
            else:
                result = self.database
            return {"users": result}

    def post(self, url, payload=None):
        # Verarbeite die POST-Anfragen je nach URL
        if url == "/add":
            user_name = payload.get('user')
            if user_name in self.database:
                return {"error": "User already exists"}, 400
            # Erstelle einen neuen Benutzer mit leeren Werten für 'owes', 'owed_by' und 'balance'
            self.database[user_name] = {
                'name': user_name,
                'owes': {},
                'owed_by': {},
                'balance': 0.0
            }
            return self.database[user_name]

        elif url == "/iou":
            lender = payload.get('lender')
            borrower = payload.get('borrower')
            amount = payload.get('amount')

            if lender == borrower:
                return {"error": "A user cannot owe themselves"}, 400
            if lender not in self.database or borrower not in self.database:
                return {"error": "Both users must exist in the system"}, 400

            # Update the 'owes' and 'owed_by' values for both users
            self.database[lender]['owes'][borrower] = self.database[lender]['owes'].get(borrower, 0) + amount
            self.database[borrower]['owed_by'][lender] = self.database[borrower]['owed_by'].get(lender, 0) + amount

            # Recalculate the balances for both users
            self.database[lender]['balance'] = self.calculate_balance(self.database[lender])
            self.database[borrower]['balance'] = self.calculate_balance(self.database[borrower])

            return {"users": [self.database[lender], self.database[borrower]]}

    def calculate_balance(self, user):
        # Calculate the user's balance: (total owed by others) - (total they owe to others)
        total_owed_by = sum(user['owed_by'].values())
        total_owes = sum(user['owes'].values())
        return total_owed_by - total_owes


# Beispielaufruf und Test:
api = RestAPI()

# Benutzer hinzufügen
print(api.post("/add", {"user": "Adam"}))  # Erstellt den Benutzer Adam
print(api.post("/add", {"user": "Bob"}))  # Erstellt den Benutzer Bob

# IOU hinzufügen
print(api.post("/iou", {"lender": "Adam", "borrower": "Bob", "amount": 5.25}))  # Adam leiht Bob 5.25

# Benutzerinformationen abrufen
print(api.get("/users", {"users": ["Adam", "Bob"]}))
