import re

class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        if self.properties != other.properties:
            return False
        if len(self.children) != len(other.children):
            return False
        return all(c1 == c2 for c1, c2 in zip(self.children, other.children))

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    if not input_string.startswith('(') or not input_string.endswith(')'):
        raise ValueError("Invalid SGF format")

    def parse_node(node_str):
        properties = {}
        key_value_pattern = re.compile(r'([A-Z]+)\[([^\]]+)\]')
        matches = re.findall(key_value_pattern, node_str)
        for key, value in matches:
            if key in properties:
                properties[key].append(value)  # Append to existing key (multiple values)
            else:
                properties[key] = [value]  # New key
        return properties

    def find_matching_paren(s, start_index):
        """ Find the index of the matching closing parenthesis. """
        stack = 1  # Start with one open parenthesis
        for i in range(start_index + 1, len(s)):
            if s[i] == '(':
                stack += 1
            elif s[i] == ')':
                stack -= 1
                if stack == 0:
                    return i
        raise ValueError("Mismatched parentheses")

    def parse_tree(sgf_str):
        nodes = []
        current_node = SgfTree()
        i = 0

        while i < len(sgf_str):
            char = sgf_str[i]
            if char == ';':  # Start of a new property
                if current_node.properties:
                    nodes.append(current_node)  # Save the current node if it has properties
                current_node = SgfTree()  # Create a new node
                i += 1
            elif char == '(':  # Start of a new subtree/variation
                subtree_end = find_matching_paren(sgf_str, i)
                child_tree = parse_tree(sgf_str[i + 1:subtree_end])  # Parse the subtree
                current_node.children.append(child_tree)  # Add child to the current node
                i = subtree_end  # Move index to the end of the subtree
            elif char == ')':  # End of the node
                if current_node.properties:  # Ensure the last node has properties before adding
                    nodes.append(current_node)
                break  # Exit the loop on closing parenthesis
            else:
                # Handle node properties
                prop_end = sgf_str.find(';', i)
                if prop_end == -1:
                    prop_end = len(sgf_str)
                properties = parse_node(sgf_str[i:prop_end])  # Parse properties
                current_node.properties.update(properties)  # Update properties in the current node
                i = prop_end - 1  # Set index to the end of properties
            i += 1

        # If there is still a current node, append it to the nodes list
        if current_node.properties:
            nodes.append(current_node)

        print(nodes)

        if len(nodes) > 1:
            raise ValueError("Multiple roots detected")
        return nodes[0] if nodes else None

    # Remove outer parentheses before parsing
    return parse_tree(input_string[1:-1])

# Test
sgf_string_1 = "(;FF[4]C[root]SZ[19];B[aa];W[ab])"
sgf_string_2 = "(;FF[4](;B[aa];W[ab])(;B[dd];W[ee]))"

# Parse the SGF strings
parsed_tree_1 = parse(sgf_string_1)
parsed_tree_2 = parse(sgf_string_2)

# Expected trees can be created for comparison
expected_tree_1 = SgfTree(
    properties={'FF': ['4'], 'C': ['root'], 'SZ': ['19']},
    children=[
        SgfTree(properties={'B': ['aa']}, children=[SgfTree(properties={'W': ['ab']})])
    ]
)

expected_tree_2 = SgfTree(
    properties={'FF': ['4']},
    children=[
        SgfTree(properties={'B': ['aa']}, children=[SgfTree(properties={'W': ['ab']})]),
        SgfTree(properties={'B': ['dd']}, children=[SgfTree(properties={'W': ['ee']})])
    ]
)


# Check if the parsed trees match the expected trees
print(parsed_tree_1 == expected_tree_1)  # Should print True
print(parsed_tree_2 == expected_tree_2)  # Should print True
