import streamlit as st
from trie import load_identifiers_into_trie
from bst import load_identifiers_into_balanced_bst
from AVL import build_avl_tree_from_file
from rbt import load_identifiers_into_rbt

trie=load_identifiers_into_rbt('venv_identifiers.txt')
bst=load_identifiers_into_balanced_bst('venv_identifiers.txt')
tree,root=build_avl_tree_from_file('venv_identifiers.txt')
rbt=load_identifiers_into_rbt('venv_identifiers.txt')


# Sidebar for Tree Selection
st.sidebar.title('Select Tree Type')
tree_type = st.sidebar.selectbox('Tree Type', ('Trie', 'BST', 'AVL', 'RBT'))

# Input box for autocomplete
st.title(f'{tree_type} Autocomplete Interface')
query = st.text_input('Enter a query:')

# Search and display results
if query:
    if tree_type == 'Trie':
        results = trie.autocomplete(query)
    elif tree_type == 'BST':
        results = bst.autocomplete(query)
    elif tree_type == 'AVL':
        results = tree.autocomplete(root,query)
    elif tree_type == 'RBT':
        results = rbt.autocomplete(query)

    if results:
        st.write('Autocomplete Suggestions:')
        for result in results:
            st.write(result)
    else:
        st.write('No suggestions found.')
