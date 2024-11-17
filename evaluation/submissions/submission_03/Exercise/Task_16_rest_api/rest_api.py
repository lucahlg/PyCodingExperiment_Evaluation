class RestAPI:
    def __init__(self, database=None):
        # Initialize an empty dictionary to hold user data
        self.users = {}

    def get(self, url, payload=None):
        if url == '/users':
            return {'users': list(self.users.keys())}
        return None

    def post(self, url, payload=None):
        if url == '/add':
            user = payload.get('user')
            if user and user not in self.users:
                self.users[user] = {'owes': {}, 'owed_by': {}}
                return self.users[user]
        elif url == '/iou':
            lender = payload.get('lender')
            borrower = payload.get('borrower')
            amount = payload.get('amount')
            if lender in self.users and borrower in self.users:
                self.users[lender]['owes'][borrower] = self.users[lender]['owes'].get(borrower, 0) + amount
                self.users[borrower]['owed_by'][lender] = self.users[borrower]['owed_by'].get(lender, 0) + amount
                return {'users': [self.users[lender], self.users[borrower]]}
        return None

    def get(self, url, payload=None):
        if url == '/users':
            return {'users': list(self.users.keys())}
        return None

    def post(self, url, payload=None):
        if url == '/add':
            user = payload.get('user')
            if user and user not in self.users:
                self.users[user] = {'owes': {}, 'owed_by': {}}
                return self.users[user]
        elif url == '/iou':
            lender = payload.get('lender')
            borrower = payload.get('borrower')
            amount = payload.get('amount')
            if lender in self.users and borrower in self.users:
                self.users[lender]['owes'][borrower] = self.users[lender]['owes'].get(borrower, 0) + amount
                self.users[borrower]['owed_by'][lender] = self.users[borrower]['owed_by'].get(lender, 0) + amount
                return {'users': [self.users[lender], self.users[borrower]]}
        return None
