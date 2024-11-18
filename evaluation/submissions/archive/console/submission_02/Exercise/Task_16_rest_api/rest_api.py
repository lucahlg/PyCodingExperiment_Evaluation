class RestAPI:
    def __init__(self, database=None):
        pass

    def get(self, url, payload=None):
        if url == '/users':
            return {'users': list(self.users.keys())}
        return {'error': 'Invalid URL'}, 404


    def post(self, url, payload=None):
        if url == '/add':
            user_name = payload.get('user')
            if user_name and user_name not in self.users:
                self.users[user_name] = {'owes': {}, 'owed_by': {}}
                return self.users[user_name], 201
            return {'error': 'User already exists or invalid name'}, 400
        elif url == '/iou':
            lender = payload.get('lender')
            borrower = payload.get('borrower')
            amount = payload.get('amount')
            if lender in self.users and borrower in self.users:
                self.users[lender]['owes'][borrower] = self.users[lender]['owes'].get(borrower, 0) + amount
                self.users[borrower]['owed_by'][lender] = self.users[borrower]['owed_by'].get(lender, 0) + amount
                return {'users': [self.users[lender], self.users[borrower]]}, 200
            return {'error': 'Invalid lender or borrower'}, 400
        return {'error': 'Invalid URL'}, 404

