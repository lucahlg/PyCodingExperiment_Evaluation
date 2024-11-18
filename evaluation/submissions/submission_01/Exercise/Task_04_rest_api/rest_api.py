import json
from copy import deepcopy

class RestAPI:
    def __init__(self, database=None):
        """Initialize the API with an optional database."""
        self.database = {"users": []} if database is None else database
        # Create a lookup dict for faster user access
        self.users_dict = {user["name"]: user for user in self.database["users"]}

    def get(self, url, payload=None):
        """Handle GET requests."""
        if url == "/users":
            if payload is None:
                # Return all users
                return json.dumps({"users": sorted(
                    self.database["users"],
                    key=lambda x: x["name"]
                )})
            else:
                # Return specific users
                payload = json.loads(payload)
                return json.dumps({
                    "users": sorted(
                        [self.users_dict[name] for name in payload["users"]],
                        key=lambda x: x["name"]
                    )
                })

    def post(self, url, payload=None):
        """Handle POST requests."""
        payload = json.loads(payload)

        if url == "/add":
            return self._add_user(payload["user"])
        elif url == "/iou":
            return self._create_iou(
                payload["lender"],
                payload["borrower"],
                payload["amount"]
            )

    def _add_user(self, name):
        """Create a new user."""
        new_user = {
            "name": name,
            "owes": {},
            "owed_by": {},
            "balance": 0.0
        }
        self.database["users"].append(new_user)
        self.users_dict[name] = new_user
        return json.dumps(new_user)

    def _create_iou(self, lender, borrower, amount):
        """Record an IOU between users."""
        # Get user objects
        lender_user = self.users_dict[lender]
        borrower_user = self.users_dict[borrower]

        # Update lender's records
        if borrower in lender_user["owes"] and lender_user["owes"][borrower] >= amount:
            # Reduce existing debt
            lender_user["owes"][borrower] -= amount
            if lender_user["owes"][borrower] == 0:
                del lender_user["owes"][borrower]
        else:
            # Calculate net amount after settling existing debts
            net_amount = amount
            if borrower in lender_user["owes"]:
                net_amount -= lender_user["owes"][borrower]
                del lender_user["owes"][borrower]

            # Add to owed_by
            if borrower in lender_user["owed_by"]:
                lender_user["owed_by"][borrower] += net_amount
            else:
                lender_user["owed_by"][borrower] = net_amount

        # Update borrower's records
        if lender in borrower_user["owed_by"] and borrower_user["owed_by"][lender] >= amount:
            # Reduce existing credit
            borrower_user["owed_by"][lender] -= amount
            if borrower_user["owed_by"][lender] == 0:
                del borrower_user["owed_by"][lender]
        else:
            # Calculate net amount after settling existing credits
            net_amount = amount
            if lender in borrower_user["owed_by"]:
                net_amount -= borrower_user["owed_by"][lender]
                del borrower_user["owed_by"][lender]

            # Add to owes
            if lender in borrower_user["owes"]:
                borrower_user["owes"][lender] += net_amount
            else:
                borrower_user["owes"][lender] = net_amount

        # Update balances
        self._update_balance(lender_user)
        self._update_balance(borrower_user)

        return json.dumps({
            "users": sorted(
                [lender_user, borrower_user],
                key=lambda x: x["name"]
            )
        })

    def _update_balance(self, user):
        """Update the balance for a user."""
        total_owed_by = sum(user["owed_by"].values())
        total_owes = sum(user["owes"].values())
        user["balance"] = total_owed_by - total_owes




# Initialize API
api = RestAPI({"users": []})

# Add users
api.post("/add", '{"user": "Adam"}')
api.post("/add", '{"user": "Bob"}')

# Create an IOU
api.post("/iou", '{"lender": "Adam", "borrower": "Bob", "amount": 5.25}')

# Get all users
print(api.get("/users"))

# Get specific users
print(api.get("/users", '{"users": ["Bob"]}'))